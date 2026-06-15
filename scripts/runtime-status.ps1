# runtime-status.ps1 — Debug nhanh AgentBase runtime
# Dùng: .\scripts\runtime-status.ps1

param(
    [string]$RuntimeId = "runtime-dab75afc-7889-405b-b216-b0746e721743"
)

$ProjectDir  = Split-Path -Parent $PSScriptRoot
$IamTokenUrl = "https://iam.api.vngcloud.vn/accounts-api/v2/auth/token"
$RuntimeBase = "https://agentbase.api.vngcloud.vn/runtime/agent-runtimes"
$EndpointUrl = "https://endpoint-b314a16e-88d5-419f-a76c-e549c4ba6e50.agentbase-runtime.aiplatform.vngcloud.vn"

# Token
$gnCreds  = Get-Content (Join-Path $ProjectDir ".greennode.json") -Raw | ConvertFrom-Json
$authB64  = [Convert]::ToBase64String(
    [System.Text.Encoding]::UTF8.GetBytes("$($gnCreds.client_id):$($gnCreds.client_secret)")
)
$TOKEN = (Invoke-RestMethod -Uri $IamTokenUrl -Method POST `
    -Headers @{ Authorization = "Basic $authB64" } `
    -Body "grant_type=client_credentials" `
    -ContentType "application/x-www-form-urlencoded").access_token

# Runtime status
$rt = Invoke-RestMethod -Uri "$RuntimeBase/$RuntimeId" `
    -Method GET -Headers @{ Authorization = "Bearer $TOKEN" }
$statusColor = if ($rt.status -eq 'ACTIVE') {'Green'} elseif ($rt.status -eq 'ERROR') {'Red'} else {'Yellow'}
Write-Host "`n=== RUNTIME ===" -ForegroundColor Cyan
Write-Host "  ID       : $($rt.id)"
Write-Host "  Name     : $($rt.name)"
Write-Host "  Status   : $($rt.status)" -ForegroundColor $statusColor
Write-Host "  UpdatedAt: $($rt.updatedAt)"

# Latest version + imageUrl
$ver = (Invoke-RestMethod -Uri "$RuntimeBase/$RuntimeId/versions?page=1&size=1" `
    -Method GET -Headers @{ Authorization = "Bearer $TOKEN" }).listData[0]
Write-Host "`n=== VERSION $($ver.version) ===" -ForegroundColor Cyan
Write-Host "  imageUrl : $($ver.imageUrl)"
Write-Host "  flavorId : $($ver.flavorId)"
Write-Host "  created  : $($ver.createdAt)"

# Endpoints
$eps = Invoke-RestMethod -Uri "$RuntimeBase/$RuntimeId/endpoints" `
    -Method GET -Headers @{ Authorization = "Bearer $TOKEN" }
Write-Host "`n=== ENDPOINTS ===" -ForegroundColor Cyan
foreach ($ep in $eps.listData) {
    $epColor = if ($ep.status -eq 'ACTIVE') {'Green'} elseif ($ep.status -eq 'ERROR') {'Red'} else {'Yellow'}
    Write-Host "  $($ep.name) v$($ep.version) | $($ep.status) | replicas=$($ep.currentReplicaCount)" -ForegroundColor $epColor
    Write-Host "  url: $($ep.url)"
}

# Health check
Write-Host "`n=== HEALTH CHECK ===" -ForegroundColor Cyan
try {
    $health = Invoke-RestMethod -Uri "$EndpointUrl/health" -Method GET -TimeoutSec 10
    Write-Host "  /health: $($health | ConvertTo-Json -Compress)" -ForegroundColor Green
} catch {
    Write-Host "  /health: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
