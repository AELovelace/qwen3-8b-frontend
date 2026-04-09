param(
    [string]$BindAddress = "0.0.0.0",
    [int]$RadeonPort = 11434,      # Radeon (HIP_VISIBLE_DEVICES) - visible chat responses
    [int]$CudaPort = 11435,        # CUDA (CUDA_VISIBLE_DEVICES) - background tooling/agentic work
    [string[]]$NodeNames = @(),
    [int[]]$NodePorts = @(),
    [string[]]$NodeBindings = @(),
    [switch]$Abliterated,
    [switch]$Strict,
    [switch]$SkipFirewall,
    [switch]$LeaveExistingProcesses,
    [string]$WindowTitlePrefix = "Ollama Node"
)

$ErrorActionPreference = "Stop"
# qwen2.5:7b is kept on-disk as a rollback target; qwen3:4b and qwen3:8b are the
# active models. Only qwen3:4b is pre-loaded into accelerator memory at startup.
$PullModels = @(
    "qwen2.5:7b",   # rollback — stays on disk, not preheated
    "qwen3:4b",
    "qwen3:8b"
)
$DefaultPreloadModel = "qwen3:4b"   # only model loaded into accelerator memory at startup
$BlockedWarmModel = "qwen2.5:14b"  # too large for Titan X Maxwell; never load
$MaxLoadedModels = 1

function Get-OllamaCommand {
    $command = Get-Command ollama -ErrorAction SilentlyContinue
    if (-not $command) {
        throw "ollama.exe was not found in PATH. Install Ollama first or launch this script from a shell where Ollama is available."
    }
    return $command.Source
}

function Ensure-FirewallRule {
    param(
        [Parameter(Mandatory = $true)]
        [int]$Port
    )

    $existingRule = Get-NetFirewallRule -DisplayName "Ollama $Port" -ErrorAction SilentlyContinue
    if ($existingRule) {
        return
    }

    New-NetFirewallRule `
        -DisplayName "Ollama $Port" `
        -Direction Inbound `
        -Action Allow `
        -Protocol TCP `
        -LocalPort $Port | Out-Null
}

function Stop-ExistingOllamaProcesses {
    $running = Get-Process ollama -ErrorAction SilentlyContinue
    if ($running) {
        $running | Stop-Process -Force
        Start-Sleep -Seconds 1
    }
}

function Escape-SingleQuotedPowerShellString {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Value
    )

    return $Value.Replace("'", "''")
}

function ConvertTo-NodeEnvironment {
    param(
        [string]$Binding
    )

    $environment = [ordered]@{}
    if ([string]::IsNullOrWhiteSpace($Binding)) {
        return $environment
    }

    foreach ($segment in ($Binding -split ';')) {
        $entry = $segment.Trim()
        if (-not $entry) {
            continue
        }

        $parts = $entry -split '=', 2
        if ($parts.Count -ne 2 -or [string]::IsNullOrWhiteSpace($parts[0])) {
            throw "Invalid node binding '$Binding'. Use semicolon-separated KEY=VALUE pairs, for example: CUDA_VISIBLE_DEVICES=0;OLLAMA_FLASH_ATTN=0"
        }

        $environment[$parts[0].Trim()] = $parts[1].Trim()
    }

    return $environment
}

function Get-NodeBindingDescription {
    param(
        [Parameter(Mandatory = $true)]
        [System.Collections.IDictionary]$Environment
    )

    if ($Environment.Count -eq 0) {
        return "default backend detection"
    }

    return ($Environment.GetEnumerator() | ForEach-Object {
        "{0}={1}" -f $_.Key, $_.Value
    }) -join "; "
}

function ConvertTo-NodeSlug {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Value,
        [Parameter(Mandatory = $true)]
        [string]$Fallback
    )

    $slug = ($Value.ToLowerInvariant() -replace '[^a-z0-9]+', '-').Trim('-')
    if ([string]::IsNullOrWhiteSpace($slug)) {
        return $Fallback
    }

    return $slug
}

function Get-NvidiaNodeSeeds {
    $nvidiaSmi = Get-Command nvidia-smi -ErrorAction SilentlyContinue
    if (-not $nvidiaSmi) {
        return @()
    }

    try {
        $rows = & $nvidiaSmi.Source --query-gpu=index,name --format=csv,noheader 2>$null
        if ($LASTEXITCODE -ne 0 -or -not $rows) {
            return @()
        }
    }
    catch {
        return @()
    }

    $gpuIndices = @()
    $gpuNames = @()
    foreach ($row in $rows) {
        $trimmed = $row.Trim()
        if (-not $trimmed) {
            continue
        }

        $parts = $trimmed -split ',', 2
        if ($parts.Count -lt 1) {
            continue
        }

        $gpuIndex = 0
        if (-not [int]::TryParse($parts[0].Trim(), [ref]$gpuIndex)) {
            continue
        }

        $gpuIndices += $gpuIndex

        $gpuName = "nvidia"
        if ($parts.Count -eq 2 -and -not [string]::IsNullOrWhiteSpace($parts[1])) {
            $gpuName = $parts[1].Trim()
        }
        $gpuNames += $gpuName
    }

    if ($gpuIndices.Count -eq 0) {
        return @()
    }

    $poolName = "cuda-pool"
    if ($gpuNames.Count -eq 1) {
        $poolName = ConvertTo-NodeSlug -Value $gpuNames[0] -Fallback "cuda-pool"
    }

    return @(
        [pscustomobject]@{
            Name          = $poolName
            Binding       = "CUDA_VISIBLE_DEVICES=$($gpuIndices -join ',');HIP_VISIBLE_DEVICES=-1;ROCR_VISIBLE_DEVICES=-1"
            PreferredPort = $CudaPort
        }
    )
}

function Get-AmdNodeSeeds {
    $adapters = Get-CimInstance Win32_VideoController -ErrorAction SilentlyContinue |
        Where-Object {
            $_.Name -and
            $_.Name -notmatch 'Microsoft Basic Display' -and
            $_.Name -match '(AMD|Radeon)'
        }

    if (-not $adapters) {
        return @()
    }

    $amdIndex = 0
    $seeds = @()
    foreach ($adapter in $adapters) {
        $name = $adapter.Name.Trim()
        $seeds += [pscustomobject]@{
            Name          = ConvertTo-NodeSlug -Value $name -Fallback "radeon-$amdIndex"
            Binding       = "HIP_VISIBLE_DEVICES=$amdIndex;CUDA_VISIBLE_DEVICES=-1"
            PreferredPort = $RadeonPort
        }
        $amdIndex += 1
    }

    return $seeds
}

function Get-AutoDetectedNodeSeeds {
    $seeds = @()
    # Assign Radeon/AMD to port 11434 (visible chat on RX 6800 XT)
    # Assign CUDA devices to port 11435 (background tooling on Titan X Maxwell)
    $seeds += Get-AmdNodeSeeds
    $seeds += Get-NvidiaNodeSeeds

    if (-not $seeds) {
        throw (
            "No supported GPUs were detected for automatic node binding. " +
            "Install vendor tooling (for example nvidia-smi) or pass -NodeNames, -NodePorts, and -NodeBindings manually."
        )
    }

    return $seeds
}

function Test-AnyManualNodeInput {
    return ($NodeNames.Count -gt 0 -or $NodePorts.Count -gt 0 -or $NodeBindings.Count -gt 0)
}

function Get-OllamaNodes {
    $nodes = @()

    if (Test-AnyManualNodeInput) {
        if ($NodeNames.Count -eq 0) {
            throw "When using manual node configuration, NodeNames is required."
        }

        if ($NodeBindings.Count -eq 0) {
            throw "When using manual node configuration, NodeBindings is required."
        }

        if ($NodeNames.Count -ne $NodeBindings.Count) {
            throw "NodeNames and NodeBindings must contain the same number of entries."
        }

        if ($NodePorts.Count -gt 0 -and $NodeNames.Count -ne $NodePorts.Count) {
            throw "NodePorts must be empty (auto-assigned) or contain the same number of entries as NodeNames."
        }

        for ($index = 0; $index -lt $NodeNames.Count; $index++) {
            $port = $RadeonPort + $index
            if ($NodePorts.Count -gt 0) {
                $port = $NodePorts[$index]
            }

            $environment = ConvertTo-NodeEnvironment -Binding $NodeBindings[$index]
            $nodes += [pscustomobject]@{
                Name               = $NodeNames[$index]
                Port               = $port
                Environment        = $environment
                BindingDescription = Get-NodeBindingDescription -Environment $environment
            }
        }
    }
    else {
        $seeds = Get-AutoDetectedNodeSeeds
        $reservedPorts = @{}
        foreach ($seed in $seeds) {
            if ($null -ne $seed.PreferredPort) {
                $reservedPorts[[int]$seed.PreferredPort] = $true
            }
        }

        $nextPort = $RadeonPort
        for ($index = 0; $index -lt $seeds.Count; $index++) {
            $seed = $seeds[$index]
            $port = $null
            if ($null -ne $seed.PreferredPort) {
                $port = [int]$seed.PreferredPort
            }
            else {
                while ($reservedPorts.ContainsKey($nextPort)) {
                    $nextPort += 1
                }
                $port = $nextPort
                $nextPort += 1
            }

            $environment = ConvertTo-NodeEnvironment -Binding $seed.Binding
            $nodes += [pscustomobject]@{
                Name               = $seed.Name
                Port               = $port
                Environment        = $environment
                BindingDescription = Get-NodeBindingDescription -Environment $environment
            }
        }
    }

    if ($nodes.Count -eq 0) {
        throw "No Ollama nodes were configured."
    }

    $duplicatePorts = $nodes.Port | Group-Object | Where-Object { $_.Count -gt 1 }
    if ($duplicatePorts) {
        throw "NodePorts must be unique. Duplicate ports: $($duplicatePorts.Name -join ', ')"
    }

    return $nodes
}

function Wait-OllamaEndpoint {
    param(
        [Parameter(Mandatory = $true)]
        [string]$BaseUrl,
        [int]$TimeoutSeconds = 60
    )

    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)
    while ((Get-Date) -lt $deadline) {
        try {
            Invoke-RestMethod -Uri "$BaseUrl/api/tags" -Method Get -TimeoutSec 5 | Out-Null
            return
        }
        catch {
            Start-Sleep -Seconds 1
        }
    }

    throw "Ollama endpoint at $BaseUrl did not become ready within $TimeoutSeconds seconds."
}

# Pulls model blobs to disk without loading them into GPU memory.
function Pull-OllamaModel {
    param(
        [Parameter(Mandatory = $true)]
        [string]$OllamaExe,
        [Parameter(Mandatory = $true)]
        [string]$Model,
        [Parameter(Mandatory = $true)]
        [string]$Bind,
        [Parameter(Mandatory = $true)]
        [int]$Port
    )

    $baseUrl = "http://$Bind`:$Port"
    Wait-OllamaEndpoint -BaseUrl $baseUrl

    $previousHost = $env:OLLAMA_HOST
    try {
        $env:OLLAMA_HOST = "${Bind}:$Port"
        Write-Host "Pulling $Model blobs on $baseUrl" -ForegroundColor Cyan
        & $OllamaExe pull $Model | Out-Null
    }
    catch {
        if ($Strict) {
            throw "Failed to pull $Model on $baseUrl. $($_.Exception.Message)"
        }

        Write-Warning "Failed to pull $Model on $baseUrl. $($_.Exception.Message)"
    }
    finally {
        if ($null -eq $previousHost) {
            Remove-Item Env:OLLAMA_HOST -ErrorAction SilentlyContinue
        }
        else {
            $env:OLLAMA_HOST = $previousHost
        }
    }
}

# Sends a single generate call to load one model cleanly into accelerator memory.
# Only called for the default model so the node is never asked to evict-and-reload
# during startup, which fragments device memory and causes backend allocation failures.
function Preheat-OllamaModel {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Model,
        [Parameter(Mandatory = $true)]
        [string]$Bind,
        [Parameter(Mandatory = $true)]
        [int]$Port
    )

    $baseUrl = "http://$Bind`:$Port"
    $requestBody = @{
        model   = $Model
        prompt  = "warmup"
        stream  = $false
        options = @{ num_predict = 1 }
    } | ConvertTo-Json -Depth 4

    try {
        Write-Host "Preheating $Model on $baseUrl" -ForegroundColor Cyan
        Invoke-RestMethod -Uri "$baseUrl/api/generate" -Method Post -ContentType "application/json" -Body $requestBody -TimeoutSec 180 | Out-Null
    }
    catch {
        if ($Strict) {
            throw "Failed to preheat $Model on $baseUrl. $($_.Exception.Message)"
        }

        Write-Warning "Failed to preheat $Model on $baseUrl. $($_.Exception.Message)"
    }
}

function Stop-OllamaModel {
    param(
        [Parameter(Mandatory = $true)]
        [string]$OllamaExe,
        [Parameter(Mandatory = $true)]
        [string]$Model,
        [Parameter(Mandatory = $true)]
        [string]$Bind,
        [Parameter(Mandatory = $true)]
        [int]$Port
    )

    $previousHost = $env:OLLAMA_HOST
    try {
        $env:OLLAMA_HOST = "${Bind}:$Port"
        & $OllamaExe stop $Model | Out-Null
    }
    catch {
        if ($Strict) {
            throw "Failed to stop $Model on ${Bind}:$Port. $($_.Exception.Message)"
        }

        Write-Host "No running $Model model found on ${Bind}:$Port" -ForegroundColor DarkGray
    }
    finally {
        if ($null -eq $previousHost) {
            Remove-Item Env:OLLAMA_HOST -ErrorAction SilentlyContinue
        }
        else {
            $env:OLLAMA_HOST = $previousHost
        }
    }
}

function Start-OllamaWindow {
    param(
        [Parameter(Mandatory = $true)]
        [string]$OllamaExe,
        [Parameter(Mandatory = $true)]
        [int]$Port,
        [Parameter(Mandatory = $true)]
        [string]$Bind,
        [Parameter(Mandatory = $true)]
        [string]$TitlePrefix,
        [Parameter(Mandatory = $true)]
        [string]$NodeName,
        [Parameter(Mandatory = $true)]
        [System.Collections.IDictionary]$Environment,
        [Parameter(Mandatory = $true)]
        [string]$BindingDescription
    )

    $escapedTitle = Escape-SingleQuotedPowerShellString -Value "$TitlePrefix $NodeName"
    $escapedHost = Escape-SingleQuotedPowerShellString -Value "${Bind}:${Port}"
    $escapedOllamaExe = Escape-SingleQuotedPowerShellString -Value $OllamaExe
    $escapedStartupMessage = Escape-SingleQuotedPowerShellString -Value "Starting Ollama node $NodeName at ${Bind}:${Port} ($BindingDescription)"

    $commandSegments = @(
        ('{0} = ''{1}'';' -f '$Host.UI.RawUI.WindowTitle', $escapedTitle)
    )

    foreach ($entry in $Environment.GetEnumerator()) {
        $escapedValue = Escape-SingleQuotedPowerShellString -Value ([string]$entry.Value)
        $commandSegments += ('{0}:{1} = ''{2}'';' -f '$env', $entry.Key, $escapedValue)
    }

    $commandSegments += @(
        ('{0} = ''{1}'';' -f '$env:OLLAMA_HOST', $escapedHost),
        ('{0} = ''{1}'';' -f '$env:OLLAMA_MAX_LOADED_MODELS', $MaxLoadedModels),
        ('Write-Host ''{0}'' -ForegroundColor Cyan;' -f $escapedStartupMessage),
        ('& ''{0}'' serve' -f $escapedOllamaExe)
    )

    $command = $commandSegments -join ' '

    Start-Process `
        -FilePath "powershell.exe" `
        -ArgumentList "-NoExit", "-Command", $command `
        -WindowStyle Normal | Out-Null
}

# Guard: catch double-dash flags that PowerShell silently binds as the first positional.
# e.g. .\start-ollama-dual-gpu.ps1 --Abliterated  ->  $BindAddress = "--Abliterated"
if ($BindAddress -like '-*') {
    throw (
        "Invalid -BindAddress value '$BindAddress'. " +
        "PowerShell uses single-dash for switch parameters. " +
        "Run:  .\scripts\start-ollama-dual-gpu.ps1 -Abliterated"
    )
}

$ollamaExe = Get-OllamaCommand
$nodes = Get-OllamaNodes

Write-Host "Configured $($nodes.Count) Ollama node(s)." -ForegroundColor Green
foreach ($node in $nodes) {
    Write-Host "Node $($node.Name) -> port $($node.Port), binding $($node.BindingDescription)" -ForegroundColor DarkCyan
}

if ($Abliterated) {
    Write-Warning "-Abliterated is not used in this launcher. The default preloaded model is qwen3:4b. To run the abliterated variant, update DefaultPreloadModel and re-run the script."
}

if (-not $SkipFirewall) {
    try {
        foreach ($node in $nodes) {
            Ensure-FirewallRule -Port $node.Port
        }
    }
    catch {
        Write-Warning "Firewall rule creation failed. Re-run this script in an elevated PowerShell window or create inbound allow rules for ports $($nodes.Port -join ', ') manually."
    }
}

if (-not $LeaveExistingProcesses) {
    Stop-ExistingOllamaProcesses
}

for ($index = 0; $index -lt $nodes.Count; $index++) {
    $node = $nodes[$index]
    Start-OllamaWindow `
        -OllamaExe $ollamaExe `
        -Port $node.Port `
        -Bind $BindAddress `
        -TitlePrefix $WindowTitlePrefix `
        -NodeName $node.Name `
        -Environment $node.Environment `
        -BindingDescription $node.BindingDescription

    if ($index -lt ($nodes.Count - 1)) {
        Start-Sleep -Milliseconds 500
    }
}

foreach ($node in $nodes) {
    Stop-OllamaModel -OllamaExe $ollamaExe -Model $BlockedWarmModel -Bind $BindAddress -Port $node.Port
}

# Phase 1: pull all model blobs to disk — no GPU memory touched yet.
foreach ($model in $PullModels) {
    foreach ($node in $nodes) {
        Pull-OllamaModel -OllamaExe $ollamaExe -Model $model -Bind $BindAddress -Port $node.Port
    }
}

# Phase 2: load only the default model once on every node so it is resident and ready.
# Abliterated requests cause Ollama to perform a single clean swap at request time.
foreach ($node in $nodes) {
    Preheat-OllamaModel -Model $DefaultPreloadModel -Bind $BindAddress -Port $node.Port
}

Write-Host "Started Ollama node endpoints." -ForegroundColor Green
foreach ($node in $nodes) {
    Write-Host "$($node.Name) -> http://$BindAddress`:$($node.Port) [$($node.BindingDescription)]" -ForegroundColor Yellow
}
Write-Host "Pulled models -> $($PullModels -join ', ')" -ForegroundColor Yellow
Write-Host "Preloaded model per node -> $DefaultPreloadModel" -ForegroundColor Yellow
Write-Host "Skipped running model -> $BlockedWarmModel" -ForegroundColor Yellow
Write-Host "Max loaded models per node -> $MaxLoadedModels" -ForegroundColor Yellow
Write-Host "Strict mode -> $Strict" -ForegroundColor Yellow
Write-Host "Use your LAN IP instead of 0.0.0.0 when configuring remote clients." -ForegroundColor DarkYellow