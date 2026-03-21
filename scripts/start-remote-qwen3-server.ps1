[CmdletBinding()]
param(
    [Parameter()]
    [string]$RemoteHost = "MONOLITH-III",

    [Parameter()]
    [string]$RemoteIp = "100.66.64.45",

    [Parameter()]
    [int]$Port = 11434,

    [Parameter()]
    [string]$Model = "qwen3-coder:30b",

    [Parameter()]
    [PSCredential]$Credential,

    [Parameter()]
    [switch]$PromptForCredential,

    [Parameter()]
    [switch]$AddToTrustedHosts,

    [Parameter()]
    [switch]$ConfigureLocalWinRM,

    [Parameter()]
    [int]$StartupTimeoutSeconds = 60,

    [Parameter()]
    [int]$LocalVerifyTimeoutSeconds = 20
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Test-IsAdministrator {
    $id = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = [System.Security.Principal.WindowsPrincipal]::new($id)
    return $principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Ensure-LocalWinRM {
    if (-not (Test-IsAdministrator)) {
        throw "-ConfigureLocalWinRM requires an elevated PowerShell session (Run as Administrator)."
    }

    Write-Host "Configuring local WinRM for PowerShell remoting..."
    Enable-PSRemoting -Force -SkipNetworkProfileCheck | Out-Null
    Start-Service -Name WinRM -ErrorAction SilentlyContinue
    Set-Service -Name WinRM -StartupType Automatic -ErrorAction SilentlyContinue
}

function Add-TrustedHostEntries {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Hosts
    )

    $hostsToAdd = $Hosts | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -Unique
    if (-not $hostsToAdd) {
        return
    }

    $path = "WSMan:\localhost\Client\TrustedHosts"
    $current = ""
    $usedWinRmCli = $false

    try {
        $current = (Get-Item -Path $path -ErrorAction Stop).Value
    }
    catch {
        $usedWinRmCli = $true
    }

    $existing = @()
    if (-not [string]::IsNullOrWhiteSpace($current)) {
        $existing = $current.Split(",") | ForEach-Object { $_.Trim() } | Where-Object { $_ }
    }

    $merged = @($existing + $hostsToAdd) | Select-Object -Unique
    $newValue = ($merged -join ",")

    if (-not $usedWinRmCli) {
        try {
            Set-Item -Path $path -Value $newValue -Force -ErrorAction Stop | Out-Null
        }
        catch {
            throw "Failed to update TrustedHosts. Re-run PowerShell as Administrator or configure WinRM HTTPS."
        }
    }
    else {
        Write-Host "WSMan provider not available; using winrm.cmd fallback for TrustedHosts."
        $winrm = Get-Command -Name "winrm.cmd" -ErrorAction SilentlyContinue
        if (-not $winrm) {
            throw "winrm.cmd is required to update TrustedHosts in this session."
        }

        $setArg = '@{TrustedHosts="' + $newValue + '"}'
        try {
            $raw = & $winrm.Source set winrm/config/client $setArg 2>&1 | Out-String
            if ($LASTEXITCODE -ne 0) {
                throw "winrm.cmd returned exit code $LASTEXITCODE. Output: $raw"
            }
        }
        catch {
            throw "Failed to update TrustedHosts via winrm.cmd. Re-run PowerShell as Administrator and ensure WinRM is enabled."
        }
    }

    Write-Host "TrustedHosts updated: $newValue"
}

$remoteScript = {
    param(
        [int]$RemotePort,
        [string]$RemoteModel,
        [int]$RemoteStartupTimeoutSeconds
    )

    Set-StrictMode -Version Latest
    $ErrorActionPreference = "Stop"

    $ollama = Get-Command -Name "ollama" -ErrorAction SilentlyContinue
    if (-not $ollama) {
        throw "Ollama is not installed or not in PATH on the remote machine."
    }

    $isListening = $false
    try {
        $isListening = [bool](Get-NetTCPConnection -LocalPort $RemotePort -State Listen -ErrorAction SilentlyContinue)
    }
    catch {
        # Fallback for environments where Get-NetTCPConnection is unavailable/restricted.
        try {
            $tcpListeners = [System.Net.NetworkInformation.IPGlobalProperties]::GetIPGlobalProperties().GetActiveTcpListeners()
            $isListening = [bool]($tcpListeners | Where-Object { $_.Port -eq $RemotePort })
        }
        catch {
            $isListening = $false
        }
    }

    if (-not $isListening) {
        Start-Process -FilePath $ollama.Source -ArgumentList "serve" -WindowStyle Hidden

        $ready = $false
        $deadline = (Get-Date).AddSeconds($RemoteStartupTimeoutSeconds)
        while ((Get-Date) -lt $deadline) {
            Start-Sleep -Seconds 1
            try {
                $resp = Invoke-WebRequest -UseBasicParsing -Uri "http://127.0.0.1:$RemotePort/api/tags" -TimeoutSec 3
                if ($resp.StatusCode -eq 200) {
                    $ready = $true
                    break
                }
            }
            catch {
                # Keep waiting for startup.
            }
        }

        if (-not $ready) {
            throw "Remote Ollama did not become ready on port $RemotePort within $RemoteStartupTimeoutSeconds seconds."
        }
    }

    # Ensure model is available (safe if already pulled).
    & $ollama.Source "pull" $RemoteModel | Out-Null

    [PSCustomObject]@{
        Host = $env:COMPUTERNAME
        Port = $RemotePort
        Model = $RemoteModel
        Ready = $true
    }
}

$invokeParams = @{
    ComputerName = $RemoteHost
    ScriptBlock = $remoteScript
    ArgumentList = @($Port, $Model, $StartupTimeoutSeconds)
}

if ($PSBoundParameters.ContainsKey("Credential")) {
    $invokeParams.Credential = $Credential
}

if (-not $PSBoundParameters.ContainsKey("Credential") -and $PromptForCredential) {
    $invokeParams.Credential = Get-Credential -Message "Enter credentials for $RemoteHost"
}

if ($ConfigureLocalWinRM) {
    Ensure-LocalWinRM
}

if ($AddToTrustedHosts) {
    Write-Host "Adding $RemoteHost and $RemoteIp to WinRM TrustedHosts..."
    Add-TrustedHostEntries -Hosts @($RemoteHost, $RemoteIp)
}

function Get-WinRMPortState {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Target,

        [Parameter(Mandatory = $true)]
        [int]$Port
    )

    $tnc = Get-Command -Name "Test-NetConnection" -ErrorAction SilentlyContinue
    if ($tnc) {
        try {
            $probe = Test-NetConnection -ComputerName $Target -Port $Port -WarningAction SilentlyContinue
            return [bool]$probe.TcpTestSucceeded
        }
        catch {
            return $false
        }
    }

    try {
        $tcp = [System.Net.Sockets.TcpClient]::new()
        $iar = $tcp.BeginConnect($Target, $Port, $null, $null)
        $ok = $iar.AsyncWaitHandle.WaitOne(2500)
        if ($ok -and $tcp.Connected) {
            $tcp.EndConnect($iar)
            $tcp.Close()
            return $true
        }
        $tcp.Close()
        return $false
    }
    catch {
        return $false
    }
}

$targets = @($RemoteHost, $RemoteIp) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -Unique
$result = $null
$connectedTarget = $null
$attemptErrors = @()

foreach ($target in $targets) {
    $invokeParams.ComputerName = $target
    Write-Host "Starting remote Ollama on $target and ensuring model '$Model'..."
    try {
        $result = Invoke-Command @invokeParams
        $connectedTarget = $target
        break
    }
    catch {
        $attemptErrors += [PSCustomObject]@{
            Target = $target
            Error = $_
        }

        Write-Warning "WinRM connection attempt failed for ${target}: $($_.Exception.Message)"
    }
}

if (-not $result) {
    $accessDeniedFailure = $attemptErrors | Where-Object {
        $_.Error.FullyQualifiedErrorId -match "AccessDenied" -or
        ($_.Error.Exception -and $_.Error.Exception.Message -match "Access is denied")
    } | Select-Object -First 1

    if ($accessDeniedFailure) {
        throw @"
WinRM authentication failed for '$($accessDeniedFailure.Target)' (Access is denied).

Run with explicit credentials for the remote machine:
1) In your shell:
   `$cred = Get-Credential

2) Run the script with those credentials:
   .\scripts\start-remote-qwen3-server.ps1 -Credential `$cred -ConfigureLocalWinRM -AddToTrustedHosts

Notes:
- For local machine accounts, use username format '.\\username' or 'MONOLITH-III\\username'.
- For domain accounts, use 'DOMAIN\\username' or 'username@domain'.
- The account must be allowed for PowerShell remoting on the remote host.
"@
    }

    $trustFailure = $attemptErrors | Where-Object {
        $_.Error.FullyQualifiedErrorId -match "ServerNotTrusted" -or
        ($_.Error.Exception -and $_.Error.Exception.Message -match "TrustedHosts")
    } | Select-Object -First 1

    if ($trustFailure) {
        throw @"
WinRM trust validation failed for '$($trustFailure.Target)'.

Run one of these options, then try again:
1) Re-run this script with automatic TrustedHosts update:
   .\scripts\start-remote-qwen3-server.ps1 -AddToTrustedHosts

2) Manually add host and IP to TrustedHosts (elevated PowerShell):
   Set-Item WSMan:\localhost\Client\TrustedHosts -Concatenate -Value '$RemoteHost,$RemoteIp' -Force

3) Prefer a hardened setup by configuring WinRM over HTTPS on the remote host.
"@
    }

    $diagLines = @()
    foreach ($target in $targets) {
        $httpOpen = Get-WinRMPortState -Target $target -Port 5985
        $httpsOpen = Get-WinRMPortState -Target $target -Port 5986
        $diagLines += "- $target : 5985(open=$httpOpen), 5986(open=$httpsOpen)"
    }

    $diagText = ($diagLines -join [Environment]::NewLine)
    throw @"
Unable to establish WinRM to '$RemoteHost' or '$RemoteIp'.

Connectivity diagnostics:
$diagText

What to check on the remote machine:
1) WinRM is enabled: Enable-PSRemoting -Force
2) WinRM service is running: Get-Service WinRM
3) Firewall allows WinRM (TCP 5985/5986)
4) Name resolution for '$RemoteHost' from this machine (or use only -RemoteIp)
"@
}

Write-Host "Remote result: host=$($result.Host), port=$($result.Port), model=$($result.Model), ready=$($result.Ready)"
Write-Host "Connected via WinRM target: $connectedTarget"

$localVerifyUrl = "http://${RemoteIp}:$Port/api/tags"
Write-Host "Verifying endpoint from local machine: $localVerifyUrl"

$localDeadline = (Get-Date).AddSeconds($LocalVerifyTimeoutSeconds)
$localReady = $false
while ((Get-Date) -lt $localDeadline) {
    try {
        $resp = Invoke-WebRequest -UseBasicParsing -Uri $localVerifyUrl -TimeoutSec 3
        if ($resp.StatusCode -eq 200) {
            $localReady = $true
            break
        }
    }
    catch {
        Start-Sleep -Milliseconds 750
    }
}

if (-not $localReady) {
    throw "Remote endpoint did not respond at $localVerifyUrl within $LocalVerifyTimeoutSeconds seconds."
}

Write-Host "Success: remote qwen3 server is reachable at $localVerifyUrl"
