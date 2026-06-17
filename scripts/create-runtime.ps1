# create-runtime.ps1 -- Create NEW AgentBase runtime, build+push image, update deploy.ps1
# Usage: .\scripts\create-runtime.ps1 [-Name <name>] [-SkipTests] [-SkipBuild] [-DryRun]

param(
    [string]$Name        = "vks-intelligence",
    [string]$FlavorId    = "runtime-s2-general-2x4",
    [string]$EnvFile     = ".env",
    [switch]$DryRun,
    [switch]$SkipTests,
    [switch]$SkipBuild
)

Set-StrictMode -Off
$ErrorActionPreference = "Stop"

$ProjectDir    = Split-Path -Parent $PSScriptRoot
$Registry      = "vcr.vngcloud.vn"
$RepoPath      = "98510-greennode-vks-intelligence/vks-intelligence"
$ImageBase     = "$Registry/$RepoPath"
$Tag           = "v$(Get-Date -Format 'yyyyMMddHHmmss')"
$ImageFull     = "${ImageBase}:${Tag}"
$IamTokenUrl   = "https://iam.api.vngcloud.vn/accounts-api/v2/auth/token"
$RuntimeApiUrl = "https://agentbase.api.vngcloud.vn/runtime/agent-runtimes"

function Write-Step([string]$msg) { Write-Host "`n>>> $msg" -ForegroundColor Cyan }
function Write-Ok([string]$msg)   { Write-Host "    OK: $msg" -ForegroundColor Green }
function Write-Fail([string]$msg) { Write-Host "    FAIL: $msg" -ForegroundColor Red; exit 1 }

Push-Location $ProjectDir

# ── 0. Load credentials ──────────────────────────────────────────────────────
Write-Step "0. Load credentials"
$gnJson  = Join-Path $ProjectDir ".greennode.json"
$regJson = Join-Path $ProjectDir "registry-credentials.json"
if (-not (Test-Path $gnJson))  { Write-Fail ".greennode.json not found" }
if (-not (Test-Path $regJson)) { Write-Fail "registry-credentials.json not found" }
$gnCreds  = Get-Content $gnJson  -Raw | ConvertFrom-Json
$regCreds = Get-Content $regJson -Raw | ConvertFrom-Json
Write-Ok "Credentials loaded (client_id=$($gnCreds.client_id.Substring(0,8))...)"

# ── 1. IAM token ─────────────────────────────────────────────────────────────
Write-Step "1. Get IAM token"
$authBytes = [System.Text.Encoding]::UTF8.GetBytes("$($gnCreds.client_id):$($gnCreds.client_secret)")
$authB64   = [Convert]::ToBase64String($authBytes)
$tokenResp = Invoke-RestMethod -Uri $IamTokenUrl -Method POST `
    -Headers @{ Authorization = "Basic $authB64" } `
    -Body "grant_type=client_credentials" `
    -ContentType "application/x-www-form-urlencoded"
$TOKEN = $tokenResp.access_token
if (-not $TOKEN) { Write-Fail "No access_token in IAM response" }
Write-Ok "Token OK (len=$($TOKEN.Length))"

# ── 2. Tests ──────────────────────────────────────────────────────────────────
if (-not $SkipTests) {
    Write-Step "2. Run local tests"
    $pytestExe = Join-Path $PSScriptRoot "..\\.venv\\Scripts\\python.exe"
    if (-not (Test-Path $pytestExe)) { $pytestExe = "python" }
    $result = & $pytestExe -m pytest tests/ -q 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host ($result | Out-String) -ForegroundColor Red
        Write-Fail "Tests failed -- stopping"
    }
    Write-Ok "Tests passed"
} else {
    Write-Host "`n>>> 2. Tests: skipped (-SkipTests)" -ForegroundColor Yellow
}

# ── 3. Docker build ───────────────────────────────────────────────────────────
if (-not $SkipBuild) {
    Write-Step "3. Docker build (linux/amd64)"
    Write-Host "    Image: $ImageFull"
    $ErrorActionPreference = "Continue"
    & docker build --platform linux/amd64 `
        --build-arg APP_BUILD_TAG=$Tag `
        --build-arg APP_BUILD_TIME=$(Get-Date -Format 'yyyy-MM-ddTHH:mm:ssZ') `
        -t $ImageFull .
    $buildExit = $LASTEXITCODE
    $ErrorActionPreference = "Stop"
    if ($buildExit -ne 0) { Write-Fail "docker build failed" }
    Write-Ok "Build done: $ImageFull"
} else {
    Write-Host "`n>>> 3. Build: skipped (-SkipBuild)" -ForegroundColor Yellow
}

if ($DryRun) {
    Write-Host "`n=== DRY RUN -- stop before push ===" -ForegroundColor Yellow
    Pop-Location; exit 0
}

# ── 4. Docker login + push ────────────────────────────────────────────────────
Write-Step "4. Docker login vCR"
docker logout $Registry 2>&1 | Out-Null
$ErrorActionPreference = "Continue"
& docker login $Registry -u $regCreds.username -p $regCreds.password
$loginExit = $LASTEXITCODE
$ErrorActionPreference = "Stop"
if ($loginExit -ne 0) { Write-Fail "docker login failed" }
Write-Ok "Login OK"

if (-not $SkipBuild) {
    Write-Step "5. Docker push"
    $ErrorActionPreference = "Continue"
    & docker push $ImageFull
    $pushExit = $LASTEXITCODE
    $ErrorActionPreference = "Stop"
    if ($pushExit -ne 0) { Write-Fail "docker push failed" }
    Write-Ok "Push done: $ImageFull"
} else {
    $ImageFull = Read-Host "    Enter imageUrl to deploy"
    if (-not $ImageFull) { Write-Fail "No imageUrl provided" }
}

# ── 5. Read env vars from .env ────────────────────────────────────────────────
Write-Step "6. Read env vars from $EnvFile"
$skipKeys = @("GREENNODE_CLIENT_ID","GREENNODE_CLIENT_SECRET","GREENNODE_AGENT_IDENTITY","GREENNODE_ENDPOINT_URL")
$envVars  = @{}
$envFilePath = Join-Path $ProjectDir $EnvFile
if (Test-Path $envFilePath) {
    Get-Content $envFilePath | ForEach-Object {
        $line = $_.Trim()
        if ($line -and -not $line.StartsWith("#") -and $line -match "^([^=]+)=(.+)$") {
            $key = $Matches[1].Trim(); $val = $Matches[2].Trim()
            if ($key -notin $skipKeys) { $envVars[$key] = $val }
        }
    }
    Write-Ok "Read $($envVars.Count) vars from $EnvFile"
} else {
    Write-Host "    $EnvFile not found -- env will be empty" -ForegroundColor Yellow
}
$tgToken = if ($envVars["TELEGRAM_BOT_TOKEN"]) { "SET (len=$($envVars['TELEGRAM_BOT_TOKEN'].Length))" } else { "MISSING" }
$tgChat  = if ($envVars["TELEGRAM_CHAT_ID"])   { "SET ($($envVars['TELEGRAM_CHAT_ID']))" }             else { "MISSING" }
$aiKey   = if ($envVars["AI_PLATFORM_API_KEY"]) { "SET (len=$($envVars['AI_PLATFORM_API_KEY'].Length))" } else { "MISSING" }
Write-Host "    TELEGRAM_BOT_TOKEN  : $tgToken"
Write-Host "    TELEGRAM_CHAT_ID    : $tgChat"
Write-Host "    AI_PLATFORM_API_KEY : $aiKey"

# ── 6. Create runtime (POST) ──────────────────────────────────────────────────
Write-Step "7. Create AgentBase runtime: $Name"
$createBody = @{
    name                 = $Name
    description          = "deploy $Tag"
    imageUrl             = $ImageFull
    imageAuth            = @{ enabled = $true; username = $regCreds.username; password = $regCreds.password }
    command              = @()
    args                 = @()
    environmentVariables = $envVars
    flavorId             = $FlavorId
    autoscaling          = @{ minReplicas = 1; maxReplicas = 1; cpuUtilization = 70; memoryUtilization = 70 }
} | ConvertTo-Json -Depth 5

$createResult = Invoke-RestMethod -Uri $RuntimeApiUrl -Method POST `
    -Headers @{ Authorization = "Bearer $TOKEN"; "Content-Type" = "application/json" } `
    -Body $createBody

$NewRuntimeId = $createResult.id
if (-not $NewRuntimeId) {
    Write-Host "    Response: $($createResult | ConvertTo-Json -Compress)" -ForegroundColor Red
    Write-Fail "Create runtime failed -- no ID in response"
}
Write-Ok "Runtime created: $NewRuntimeId"

# ── 7. Poll ACTIVE ────────────────────────────────────────────────────────────
Write-Step "8. Wait for runtime ACTIVE (max 4 min)"
$RuntimeUrl = "$RuntimeApiUrl/$NewRuntimeId"
$maxWait = 240; $interval = 10; $elapsed = 0
while ($elapsed -lt $maxWait) {
    Start-Sleep -Seconds $interval
    $elapsed += $interval
    $rt = Invoke-RestMethod -Uri $RuntimeUrl -Method GET -Headers @{ Authorization = "Bearer $TOKEN" }
    Write-Host "    [+${elapsed}s] status: $($rt.status)"
    if ($rt.status -eq "ACTIVE") { Write-Ok "Runtime ACTIVE"; break }
    if ($rt.status -eq "ERROR")  {
        Write-Host "    Reason: $($rt.statusReason)" -ForegroundColor Red
        Write-Fail "Runtime ERROR -- check console"
    }
}
if ($elapsed -ge $maxWait) { Write-Fail "Timeout -- runtime not ACTIVE after ${maxWait}s" }

# ── 8. Get endpoint URL ───────────────────────────────────────────────────────
Write-Step "9. Get endpoint URL"
Start-Sleep -Seconds 3
$epResp = Invoke-RestMethod -Uri "$RuntimeUrl/endpoints?page=1&size=10" `
    -Method GET -Headers @{ Authorization = "Bearer $TOKEN" }
$defaultEp = $epResp.listData | Select-Object -First 1
$NewEndpointUrl = $defaultEp.url
if (-not $NewEndpointUrl) {
    Write-Host "    Endpoints response: $($epResp | ConvertTo-Json -Compress)" -ForegroundColor Yellow
    Write-Host "    WARNING: Could not detect endpoint URL -- update deploy.ps1 manually" -ForegroundColor Yellow
    $NewEndpointUrl = "UNKNOWN"
} else {
    Write-Ok "Endpoint URL: $NewEndpointUrl"
}

# ── 9. Patch deploy.ps1 ───────────────────────────────────────────────────────
Write-Step "10. Update deploy.ps1"
$deployScript = Join-Path $PSScriptRoot "deploy.ps1"
$content = Get-Content $deployScript -Raw

# Replace [string]$RuntimeId default value
$content = [regex]::Replace(
    $content,
    '(\[string\]\$RuntimeId\s*=\s*)"[^"]+"',
    '$1"' + $NewRuntimeId + '"'
)
# Replace $EndpointUrl assignment
$content = [regex]::Replace(
    $content,
    '(\$EndpointUrl\s+=\s+)"[^"]+"',
    '$1"' + $NewEndpointUrl + '"'
)

Set-Content $deployScript -Value $content -Encoding UTF8 -NoNewline
Write-Ok "deploy.ps1 updated (RuntimeId + EndpointUrl)"

# ── 10. Health check ──────────────────────────────────────────────────────────
Write-Step "11. Health check"
Start-Sleep -Seconds 5
try {
    $health = Invoke-RestMethod -Uri "$NewEndpointUrl/health" -Method GET -TimeoutSec 30
    Write-Ok "/health: $($health | ConvertTo-Json -Compress)"
} catch {
    Write-Host "    /health not ready yet: $($_.Exception.Message)" -ForegroundColor Yellow
    Write-Host "    Retry: curl $NewEndpointUrl/health" -ForegroundColor Yellow
}

Pop-Location

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host " CREATE + DEPLOY DONE" -ForegroundColor Green
Write-Host " Runtime ID : $NewRuntimeId" -ForegroundColor Green
Write-Host " Image      : $ImageFull" -ForegroundColor Green
Write-Host " Endpoint   : $NewEndpointUrl" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host " deploy.ps1 da duoc cap nhat -- lan sau dung:" -ForegroundColor White
Write-Host " .\scripts\deploy.ps1" -ForegroundColor White
