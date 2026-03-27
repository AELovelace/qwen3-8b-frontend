<#
.SYNOPSIS
    One-shot environment setup script for qwen3-8b-frontend on a fresh Windows PC.

.DESCRIPTION
    Performs the following steps, in order:
      1. Verifies prerequisites (Python 3.10+, Node.js / npm)
      2. Creates a Python virtual environment at .venv\ (if absent)
      3. Installs Python dependencies from requirements.txt
      4. Installs Node.js dev dependencies (package.json)
      5. Builds the CodeMirror file-editor bundle
      6. Creates .env with prompted values (if absent)
      7. Confirms config.json exists (creates minimal default if absent)
      8. Runs a quick py_compile sanity check on server.py

    Re-running this script is safe -- each step is idempotent.

.PARAMETER SkipEnvPrompt
    If set, skip the interactive .env creation prompt and leave any existing .env
    unchanged (or skip creation if absent).

.PARAMETER OllamaBaseUrl
    Override the default OLLAMA_BASE_URL written into .env.
    Defaults to http://100.66.64.45:11434

.EXAMPLE
    .\setup.ps1

.EXAMPLE
    .\setup.ps1 -OllamaBaseUrl "http://localhost:11434"
#>
[CmdletBinding()]
param(
    [switch]$SkipEnvPrompt,

    [string]$OllamaBaseUrl = "http://100.66.64.45:11434"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
function Write-Step { param([string]$Msg) Write-Host "`n==> $Msg" -ForegroundColor Cyan }
function Write-OK   { param([string]$Msg) Write-Host "    [OK] $Msg" -ForegroundColor Green }
function Write-Skip { param([string]$Msg) Write-Host "    [--] $Msg" -ForegroundColor DarkGray }
function Write-Warn { param([string]$Msg) Write-Host "    [!!] $Msg" -ForegroundColor Yellow }
function Write-Fail { param([string]$Msg) Write-Host "    [XX] $Msg" -ForegroundColor Red }

function Prompt-WithDefault {
    param([string]$Label, [string]$Default)
    $raw = Read-Host "$Label [default: $Default]"
    if ($raw.Trim() -eq "") { return $Default }
    return $raw.Trim()
}

# Change to the directory that contains this script so all relative paths work.
$ScriptDir = $PSScriptRoot
if (-not $ScriptDir) { $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition }
Set-Location $ScriptDir

Write-Host ""
Write-Host "================================================" -ForegroundColor Magenta
Write-Host "  qwen3-8b-frontend -- environment setup"       -ForegroundColor Magenta
Write-Host "  Working directory: $ScriptDir"                -ForegroundColor Magenta
Write-Host "================================================" -ForegroundColor Magenta

# ---------------------------------------------------------------------------
# Step 1 -- Verify Python 3.10+
# ---------------------------------------------------------------------------
Write-Step "Checking Python version"

$pythonCmd = $null
foreach ($candidate in @("python", "python3")) {
    try {
        $verStr = & $candidate --version 2>&1
        if ($verStr -match "Python (\d+)\.(\d+)") {
            $major = [int]$Matches[1]
            $minor = [int]$Matches[2]
            if ($major -gt 3 -or ($major -eq 3 -and $minor -ge 10)) {
                $pythonCmd = $candidate
                Write-OK "$candidate -- $verStr"
                break
            }
        }
    }
    catch { <# not found, try next #> }
}

if (-not $pythonCmd) {
    Write-Fail "Python 3.10 or newer not found in PATH."
    Write-Host "  Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "  Make sure to tick 'Add Python to PATH' during install." -ForegroundColor Yellow
    exit 1
}

# ---------------------------------------------------------------------------
# Step 2 -- Verify Node.js / npm
# ---------------------------------------------------------------------------
Write-Step "Checking Node.js / npm"

$npmOk = $false
try {
    $nodeVer = & node --version 2>&1
    $npmVer  = & npm  --version 2>&1
    Write-OK "node $nodeVer  |  npm $npmVer"
    $npmOk = $true
}
catch {
    Write-Warn "Node.js / npm not found in PATH."
    Write-Host "  Download from: https://nodejs.org/" -ForegroundColor Yellow
    Write-Host "  The file-editor bundle will NOT be built. Server will still start," -ForegroundColor Yellow
    Write-Host "  but the popup file editor will fall back to plain textarea mode." -ForegroundColor Yellow
}

# ---------------------------------------------------------------------------
# Step 3 -- Python virtual environment
# ---------------------------------------------------------------------------
Write-Step "Python virtual environment (.venv)"

$venvDir    = Join-Path $ScriptDir ".venv"
$venvPython = Join-Path $venvDir "Scripts\python.exe"

if (Test-Path $venvPython) {
    Write-Skip "Virtual environment already exists -- skipping creation"
}
else {
    Write-Host "    Creating venv..." -ForegroundColor Gray
    & $pythonCmd -m venv $venvDir
    Write-OK "Virtual environment created at .venv\"
}

# ---------------------------------------------------------------------------
# Step 4 -- Install / upgrade Python dependencies
# ---------------------------------------------------------------------------
Write-Step "Installing Python dependencies (requirements.txt)"

# Always run in case requirements.txt changed since last install.
& $venvPython -m pip install --upgrade pip --quiet
& $venvPython -m pip install -r requirements.txt

Write-OK "Python packages installed"

# ---------------------------------------------------------------------------
# Step 5 -- Node.js packages + bundle build
# ---------------------------------------------------------------------------
if ($npmOk) {
    Write-Step "Installing Node.js dev dependencies (package.json)"

    $nodeModules = Join-Path $ScriptDir "node_modules"
    if (Test-Path $nodeModules) {
        Write-Skip "node_modules already present -- running npm install to sync any changes"
    }

    & npm install
    Write-OK "npm packages installed"

    Write-Step "Building CodeMirror file-editor bundle"

    $bundlePath = Join-Path $ScriptDir "resources\file-editor-popup.bundle.js"
    & npm run build:file-editor

    if (Test-Path $bundlePath) {
        $sizeKB = [math]::Round((Get-Item $bundlePath).Length / 1KB, 0)
        Write-OK "Bundle built: resources\file-editor-popup.bundle.js  ($sizeKB KB)"
    }
    else {
        Write-Fail "Bundle file not found after build -- check esbuild output above."
        exit 1
    }
}
else {
    Write-Warn "Skipping npm install and bundle build (Node.js not found)"
}

# ---------------------------------------------------------------------------
# Step 6 -- Create .env file
# ---------------------------------------------------------------------------
Write-Step "Environment file (.env)"

$envPath = Join-Path $ScriptDir ".env"

if (Test-Path $envPath) {
    Write-Skip ".env already exists -- not overwriting"
    Write-Host "    Edit $envPath to change secrets / settings." -ForegroundColor DarkGray
}
elseif ($SkipEnvPrompt) {
    Write-Warn "-SkipEnvPrompt set and no .env found; skipping .env creation."
    Write-Warn "The server auto-generates a JWT secret into config.json on first run."
    Write-Warn "Set ADMIN_USERNAME + ADMIN_PASSWORD in .env before starting the server."
}
else {
    Write-Host ""
    Write-Host "  Creating .env -- enter values below." -ForegroundColor Cyan
    Write-Host "  Press Enter to accept defaults shown in brackets." -ForegroundColor DarkGray
    Write-Host ""

    # Admin credentials (required for first-run account bootstrap)
    do {
        $adminUser = (Read-Host "  ADMIN_USERNAME (alphanumeric, 3-32 chars)").Trim()
    } while ($adminUser.Length -lt 3)

    do {
        $adminPass = (Read-Host "  ADMIN_PASSWORD (min 8 chars, include a digit + special char)").Trim()
    } while ($adminPass.Length -lt 8)

    # JWT secret -- auto-generate a strong random value as the default.
    $jwtBytes = [byte[]]::new(40)
    [System.Security.Cryptography.RandomNumberGenerator]::Fill($jwtBytes)
    $jwtDefault = [Convert]::ToBase64String($jwtBytes) -replace '=','' -replace '\+','-' -replace '/','_'

    $jwtSecret = Prompt-WithDefault "  JWT_SECRET" $jwtDefault

    # Brave API key -- optional
    $braveKey = (Read-Host "  BRAVE_API_KEY (optional -- leave blank to disable web search)").Trim()

    # Ollama endpoint
    $ollamaUrl = Prompt-WithDefault "  OLLAMA_BASE_URL" $OllamaBaseUrl

    # Build .env content
    $envLines = @(
        "ADMIN_USERNAME=$adminUser",
        "ADMIN_PASSWORD=$adminPass",
        "JWT_SECRET=$jwtSecret",
        "OLLAMA_BASE_URL=$ollamaUrl"
    )
    if ($braveKey -ne "") {
        $envLines += "BRAVE_API_KEY=$braveKey"
    }

    [System.IO.File]::WriteAllLines($envPath, $envLines, [System.Text.UTF8Encoding]::new($false))
    Write-OK ".env written to $envPath"
    Write-Warn "Keep .env private -- it contains secrets. It should be excluded from git."
}

# ---------------------------------------------------------------------------
# Step 7 -- Ensure config.json has the required structure
# ---------------------------------------------------------------------------
Write-Step "config.json"

$configPath = Join-Path $ScriptDir "config.json"
if (Test-Path $configPath) {
    Write-Skip "config.json already exists -- not overwriting"
}
else {
    $defaultConfig = @'
{
  "global_tool_toggles": {
    "use_gml_docs": true,
    "use_ps_docs": true,
    "use_file_tools": true,
    "use_code_interpreter": true,
    "use_powershell": "native",
    "use_mcp_tools": true,
    "use_raw_api": true
  }
}
'@
    [System.IO.File]::WriteAllText($configPath, $defaultConfig, [System.Text.UTF8Encoding]::new($false))
    Write-OK "config.json created with default tool toggles"
}

# ---------------------------------------------------------------------------
# Step 8 -- Sanity check: py_compile server.py
# ---------------------------------------------------------------------------
Write-Step "Syntax check (py_compile server.py)"

try {
    & $venvPython -m py_compile server.py
    Write-OK "server.py compiles cleanly"
}
catch {
    Write-Fail "server.py has a syntax error. See output above."
    exit 1
}

# ---------------------------------------------------------------------------
# Done
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "  Setup complete!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "  To start the server:" -ForegroundColor Cyan
Write-Host "      .\.venv\Scripts\python.exe server.py" -ForegroundColor White
Write-Host ""
Write-Host "  Then open: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host ""
Write-Host "  To rebuild the file-editor bundle after editing resources-src\:" -ForegroundColor DarkGray
Write-Host "      npm run build:file-editor" -ForegroundColor White
Write-Host ""
