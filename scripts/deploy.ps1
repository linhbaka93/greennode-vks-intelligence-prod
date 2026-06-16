# deploy.ps1 -- Build, push, update AgentBase runtime
# Usage: .\scripts\deploy.ps1 [-SkipTests] [-SkipBuild] [-DryRun]

param(
    [string]$RuntimeId = "runtime-dab75afc-7889-405b-b216-b0746e721743",
    [string]$EnvFile   = ".env",
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
$EndpointUrl   = "https://endpoint-b314a16e-88d5-419f-a76c-e549c4ba6e50.agentbase-runtime.aiplatform.vngcloud.vn"
$IamTokenUrl   = "https://iam.api.vngcloud.vn/accounts-api/v2/auth/token"
$RuntimeApiUrl = "https://agentbase.api.vngcloud.vn/runtime/agent-runtimes/$RuntimeId"

function Write-Step([string]$msg) { Write-Host "`n>>> $msg" -ForegroundColor Cyan }
function Write-Ok([string]$msg)   { Write-Host "    OK: $msg" -ForegroundColor Green }
function Write-Fail([string]$msg) { Write-Host "    FAIL: $msg" -ForegroundColor Red; exit 1 }

Push-Location $ProjectDir

# -- 0. Credentials --
Write-Step "0. Load credentials"
$gnJson  = Join-Path $ProjectDir ".greennode.json"
$regJson = Join-Path $ProjectDir "registry-credentials.json"
if (-not (Test-Path $gnJson))  { Write-Fail ".greennode.json not found" }
if (-not (Test-Path $regJson)) { Write-Fail "registry-credentials.json not found" }
$gnCreds  = Get-Content $gnJson  -Raw | ConvertFrom-Json
$regCreds = Get-Content $regJson -Raw | ConvertFrom-Json
Write-Ok "Credentials loaded"

# -- 1. IAM token --
Write-Step "1. Get IAM token"
$authBytes = [System.Text.Encoding]::UTF8.GetBytes("$($gnCreds.client_id):$($gnCreds.client_secret)")
$authB64   = [Convert]::ToBase64String($authBytes)
$tokenResp = Invoke-RestMethod -Uri $IamTokenUrl -Method POST `
    -Headers @{ Authorization = "Basic $authB64" } `
    -Body "grant_type=client_credentials" `
    -ContentType "application/x-www-form-urlencoded"
$TOKEN = $tokenResp.access_token
Write-Ok "Token OK (len=$($TOKEN.Length))"

# -- 2. Tests --
if (-not $SkipTests) {
    Write-Step "2. Run local tests"
    $result = & uv run pytest tests/ -q 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host ($result | Out-String) -ForegroundColor Red
        Write-Fail "Tests failed -- stopping deploy"
    }
    Write-Ok "Tests passed"
} else {
    Write-Host "`n>>> 2. Tests: skipped (-SkipTests)" -ForegroundColor Yellow
}

# -- 3. Docker build --
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
    Write-Host "    Image: $ImageFull"
    Pop-Location; exit 0
}

# -- 4. Docker login + push --
Write-Step "4. Docker login vCR"
# Logout trước để xóa cached credentials cũ (tránh unauthorized với password stale)
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
    Write-Ok "Push done"
} else {
    Write-Host "`n>>> 5. Push: skipped (-SkipBuild)" -ForegroundColor Yellow
    $ImageFull = Read-Host "    Enter imageUrl to deploy"
    if (-not $ImageFull) { Write-Fail "No imageUrl provided" }
}

# -- 5. Build env vars: runtime current vars (base) + .env (override) --
Write-Step "6. Merge env vars (runtime base + $EnvFile override)"
$skipKeys = @("GREENNODE_CLIENT_ID","GREENNODE_CLIENT_SECRET","GREENNODE_AGENT_IDENTITY","GREENNODE_ENDPOINT_URL")

# 5a. Fetch current runtime version env vars as base (preserves manually-set secrets like TELEGRAM_*)
$envVars = @{}
try {
    $verResp = Invoke-RestMethod -Uri "$RuntimeApiUrl/versions?page=1&size=1" `
        -Method GET -Headers @{ Authorization = "Bearer $TOKEN" }
    $currentEnv = $verResp.listData[0].environmentVariables
    if ($currentEnv) {
        $currentEnv.PSObject.Properties | ForEach-Object {
            if ($_.Name -notin $skipKeys) { $envVars[$_.Name] = $_.Value }
        }
        Write-Host "    Base: $($envVars.Count) vars from current runtime version"
    }
} catch {
    Write-Host "    Could not fetch current runtime env vars: $($_.Exception.Message)" -ForegroundColor Yellow
}

# 5b. Overlay with .env (values in .env take precedence; empty values skipped)
$envFilePath = Join-Path $ProjectDir $EnvFile
$dotEnvCount = 0
if (Test-Path $envFilePath) {
    Get-Content $envFilePath | ForEach-Object {
        $line = $_.Trim()
        if ($line -and -not $line.StartsWith("#") -and $line -match "^([^=]+)=(.+)$") {
            $key = $Matches[1].Trim(); $val = $Matches[2].Trim()
            if ($key -notin $skipKeys) { $envVars[$key] = $val; $dotEnvCount++ }
        }
    }
    Write-Ok "Merged $dotEnvCount vars from $EnvFile (total: $($envVars.Count))"
} else {
    Write-Host "    $EnvFile not found -- using runtime vars only" -ForegroundColor Yellow
}

# Show Telegram vars state for debug
$tgToken = if ($envVars["TELEGRAM_BOT_TOKEN"]) { "SET (len=$($envVars['TELEGRAM_BOT_TOKEN'].Length))" } else { "MISSING" }
$tgChat  = if ($envVars["TELEGRAM_CHAT_ID"])   { "SET ($($envVars['TELEGRAM_CHAT_ID']))" }             else { "MISSING" }
Write-Host "    TELEGRAM_BOT_TOKEN: $tgToken"
Write-Host "    TELEGRAM_CHAT_ID  : $tgChat"

# -- 6. PATCH runtime --
Write-Step "7. Update AgentBase runtime"
Write-Host "    imageUrl: $ImageFull"

$patchBody = @{
    description          = "deploy $Tag"
    imageUrl             = $ImageFull
    imageAuth            = @{ enabled = $true; username = $regCreds.username; password = $regCreds.password }
    command              = @()
    args                 = @()
    environmentVariables = $envVars
    flavorId             = "runtime-s2-general-2x4"
    # GIỮ minReplicas=maxReplicas=1: scheduler nội bộ (scheduler.py) không an toàn khi >1 replica
    autoscaling          = @{ minReplicas = 1; maxReplicas = 1; cpuUtilization = 70; memoryUtilization = 70 }
} | ConvertTo-Json -Depth 5

$patchResult = Invoke-RestMethod -Uri $RuntimeApiUrl -Method PATCH `
    -Headers @{ Authorization = "Bearer $TOKEN"; "Content-Type" = "application/json" } `
    -Body $patchBody
Write-Ok "PATCH OK -- status: $($patchResult.status)"

# -- 7. Poll ACTIVE --
Write-Step "8. Wait for runtime ACTIVE (max 3 min)"
$maxWait = 180; $interval = 10; $elapsed = 0
while ($elapsed -lt $maxWait) {
    Start-Sleep -Seconds $interval
    $elapsed += $interval
    $rt = Invoke-RestMethod -Uri $RuntimeApiUrl -Method GET -Headers @{ Authorization = "Bearer $TOKEN" }
    Write-Host "    [+${elapsed}s] status: $($rt.status)"
    if ($rt.status -eq "ACTIVE") { Write-Ok "Runtime ACTIVE"; break }
    if ($rt.status -eq "ERROR")  { Write-Fail "Runtime ERROR -- check logs on console" }
}
if ($elapsed -ge $maxWait) { Write-Fail "Timeout -- runtime not ACTIVE after ${maxWait}s" }

# -- 8. Health check --
Write-Step "9. Health check"
Start-Sleep -Seconds 5
try {
    $health = Invoke-RestMethod -Uri "$EndpointUrl/health" -Method GET -TimeoutSec 30
    Write-Ok "/health: $($health | ConvertTo-Json -Compress)"
} catch {
    Write-Host "    /health not ready yet: $($_.Exception.Message)" -ForegroundColor Yellow
    Write-Host "    Container still starting -- retry manually in 30s"
}

Pop-Location

Write-Host "`n========================================" -ForegroundColor Green
Write-Host " DEPLOY DONE" -ForegroundColor Green
Write-Host " Runtime : $RuntimeId" -ForegroundColor Green
Write-Host " Image   : $ImageFull" -ForegroundColor Green
Write-Host " Endpoint: $EndpointUrl" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
