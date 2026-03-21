[CmdletBinding()]
param(
    [Parameter()]
    [int]$Port = 11434,

    [Parameter()]
    [string]$Model = "qwen3-coder:30b",

    [Parameter()]
    [int]$StartupTimeoutSeconds = 60,

    [Parameter()]
    [string]$BindHost = "0.0.0.0",

    [Parameter()]
    [string]$TailscaleIp = "100.66.64.45",

    [Parameter()]
    [switch]$VerifyTailscaleEndpoint,

    [Parameter()]
    [switch]$RestartOllama,

    [Parameter()]
    [switch]$EnsureFirewallRule

    ,
    [Parameter()]
    [string]$KeepAlive = "-1",

    [Parameter()]
    [switch]$SkipWarmup
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Ensure-FirewallRule {
    param(
        [Parameter(Mandatory = $true)]
        [int]$LocalPort
    )

    $ruleName = "Ollama API $LocalPort"
    try {
        $existing = Get-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue
        if (-not $existing) {
            New-NetFirewallRule -DisplayName $ruleName -Direction Inbound -Action Allow -Protocol TCP -LocalPort $LocalPort | Out-Null
            Write-Host "Created inbound firewall rule: $ruleName"
        }
        else {
            Write-Host "Firewall rule already present: $ruleName"
        }
    }
    catch {
        Write-Warning "Could not create firewall rule for port $LocalPort. Run as Administrator if remote access still fails."
    }
}

function Start-OllamaServe {
    param(
        [Parameter(Mandatory = $true)]
        [string]$OllamaExe,

        [Parameter(Mandatory = $true)]
        [string]$BindAddress,

        [Parameter(Mandatory = $true)]
        [int]$LocalPort,

        [Parameter(Mandatory = $true)]
        [string]$ModelKeepAlive
    )

    $ollamaHostValue = "${BindAddress}:$LocalPort"

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $OllamaExe
    $psi.Arguments = "serve"
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $psi.EnvironmentVariables["OLLAMA_HOST"] = $ollamaHostValue
    $psi.EnvironmentVariables["OLLAMA_KEEP_ALIVE"] = $ModelKeepAlive

    [System.Diagnostics.Process]::Start($psi) | Out-Null
}

function Warm-Model {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ModelName,

        [Parameter(Mandatory = $true)]
        [int]$LocalPort,

        [Parameter(Mandatory = $true)]
        [string]$ModelKeepAlive
    )

    $url = "http://127.0.0.1:$LocalPort/api/generate"
    $body = @{
        model = $ModelName
        prompt = ""
        stream = $false
        keep_alive = $ModelKeepAlive
    } | ConvertTo-Json

    try {
        Invoke-WebRequest -UseBasicParsing -Uri $url -Method Post -ContentType "application/json" -Body $body -TimeoutSec 120 | Out-Null
        Write-Host "Warmup complete: model '$ModelName' loaded with keep_alive=$ModelKeepAlive"
    }
    catch {
        Write-Warning "Warmup request failed for '$ModelName'. Model may still load on first chat. Error: $($_.Exception.Message)"
    }
}

function Test-OllamaReady {
    param(
        [Parameter(Mandatory = $true)]
        [int]$LocalPort,

        [Parameter()]
        [int]$TimeoutSec = 3
    )

    try {
        $resp = Invoke-WebRequest -UseBasicParsing -Uri "http://127.0.0.1:$LocalPort/api/tags" -TimeoutSec $TimeoutSec
        return ($resp.StatusCode -eq 200)
    }
    catch {
        return $false
    }
}

function Get-ListenAddresses {
    param(
        [Parameter(Mandatory = $true)]
        [int]$LocalPort
    )

    try {
        $rows = Get-NetTCPConnection -State Listen -LocalPort $LocalPort -ErrorAction SilentlyContinue
        if (-not $rows) {
            return @()
        }
        return @($rows | Select-Object -ExpandProperty LocalAddress -Unique)
    }
    catch {
        return @()
    }
}

function Test-BindHostSatisfied {
    param(
        [Parameter(Mandatory = $true)]
        [string]$DesiredHost,

        [Parameter(Mandatory = $true)]
        [int]$LocalPort
    )

    $addresses = @(Get-ListenAddresses -LocalPort $LocalPort)
    if (-not $addresses -or $addresses.Count -eq 0) {
        return $false
    }

    # Any-address listeners satisfy all bind targets.
    if ($addresses -contains "0.0.0.0" -or $addresses -contains "::") {
        return $true
    }

    if ($DesiredHost -eq "0.0.0.0") {
        return $false
    }

    return ($addresses -contains $DesiredHost)
}

$ollama = Get-Command -Name "ollama" -ErrorAction SilentlyContinue
if (-not $ollama) {
    throw "Ollama is not installed or not in PATH on this machine."
}

if ($EnsureFirewallRule) {
    Ensure-FirewallRule -LocalPort $Port
}

if ($RestartOllama) {
    Write-Host "Restart requested. Stopping existing Ollama processes..."
    Get-Process -Name "ollama" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 1
}

if (-not (Test-OllamaReady -LocalPort $Port)) {
    Write-Host "Ollama is not responding on localhost:$Port. Starting 'ollama serve' with OLLAMA_HOST=${BindHost}:$Port..."
    Start-OllamaServe -OllamaExe $ollama.Source -BindAddress $BindHost -LocalPort $Port -ModelKeepAlive $KeepAlive

    $deadline = (Get-Date).AddSeconds($StartupTimeoutSeconds)
    $ready = $false
    while ((Get-Date) -lt $deadline) {
        Start-Sleep -Seconds 1
        if ((Test-OllamaReady -LocalPort $Port) -and (Test-BindHostSatisfied -DesiredHost $BindHost -LocalPort $Port)) {
            $ready = $true
            break
        }
    }

    if (-not $ready) {
        $listenAddresses = (Get-ListenAddresses -LocalPort $Port) -join ", "
        throw "Ollama did not become ready with bind host '$BindHost' on localhost:$Port within $StartupTimeoutSeconds seconds. Listen addresses: $listenAddresses. If Ollama runs as a Windows service, set system env OLLAMA_HOST=${BindHost}:$Port and restart that service."
    }
}
else {
    if (Test-BindHostSatisfied -DesiredHost $BindHost -LocalPort $Port) {
        Write-Host "Ollama is already running on localhost:$Port with compatible bind host."
    }
    else {
        $listenAddresses = (Get-ListenAddresses -LocalPort $Port) -join ", "
        Write-Host "Ollama is running, but bind host is not compatible with '$BindHost' (current: $listenAddresses). Restarting with desired bind..."

        Get-Process -Name "ollama" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
        Start-Sleep -Seconds 1
        Start-OllamaServe -OllamaExe $ollama.Source -BindAddress $BindHost -LocalPort $Port -ModelKeepAlive $KeepAlive

        $deadline = (Get-Date).AddSeconds($StartupTimeoutSeconds)
        $ready = $false
        while ((Get-Date) -lt $deadline) {
            Start-Sleep -Seconds 1
            if ((Test-OllamaReady -LocalPort $Port) -and (Test-BindHostSatisfied -DesiredHost $BindHost -LocalPort $Port)) {
                $ready = $true
                break
            }
        }

        if (-not $ready) {
            $listenAddresses = (Get-ListenAddresses -LocalPort $Port) -join ", "
            throw "Ollama restarted, but bind host '$BindHost' is still not active on port $Port. Listen addresses: $listenAddresses. If Ollama runs as a Windows service, set system env OLLAMA_HOST=${BindHost}:$Port and restart that service."
        }
    }
}

Write-Host "Ensuring model '$Model' is available..."
& $ollama.Source "pull" $Model

if (-not $SkipWarmup) {
    Warm-Model -ModelName $Model -LocalPort $Port -ModelKeepAlive $KeepAlive
}
else {
    Write-Host "Skipping warmup request (-SkipWarmup set)."
}

Write-Host "Local endpoint ready: http://127.0.0.1:$Port/api/tags"

if ($VerifyTailscaleEndpoint) {
    $tailscaleUrl = "http://${TailscaleIp}:$Port/api/tags"
    Write-Host "Verifying Tailscale endpoint: $tailscaleUrl"
    try {
        $resp = Invoke-WebRequest -UseBasicParsing -Uri $tailscaleUrl -TimeoutSec 5
        if ($resp.StatusCode -eq 200) {
            Write-Host "Tailscale endpoint is reachable: $tailscaleUrl"
        }
        else {
            throw "Unexpected status code: $($resp.StatusCode)"
        }
    }
    catch {
        $listenAddresses = (Get-ListenAddresses -LocalPort $Port) -join ", "
        if (Test-BindHostSatisfied -DesiredHost $BindHost -LocalPort $Port) {
            Write-Warning "Tailscale self-check failed at $tailscaleUrl, but Ollama is listening with compatible bind host ($listenAddresses). This can happen when testing a machine against its own Tailscale IP. Verify from another client machine using: Invoke-WebRequest -UseBasicParsing -Uri '$tailscaleUrl'"
        }
        else {
            throw "Local Ollama is up, but Tailscale endpoint check failed at $tailscaleUrl and bind host is not compatible (current: $listenAddresses). Re-run with -RestartOllama -BindHost 0.0.0.0 -EnsureFirewallRule."
        }
    }
}
