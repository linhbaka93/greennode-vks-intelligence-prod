# refresh-vcr-credentials.ps1 -- Refresh vCR robot account secret key
# Dung khi docker login vcr.vngcloud.vn tra unauthorized
# Usage: .\scripts\refresh-vcr-credentials.ps1

$ProjectDir = Split-Path -Parent $PSScriptRoot
$RobotUuid  = "ra-1d54750b-9311-44c4-abba-67606ec2756b"
$Registry   = "vcr.vngcloud.vn"

# IAM token
$gnCreds = Get-Content "$ProjectDir\.greennode.json" -Raw | ConvertFrom-Json
$authB64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("$($gnCreds.client_id):$($gnCreds.client_secret)"))
$TOKEN = (Invoke-RestMethod -Uri "https://iam.api.vngcloud.vn/accounts-api/v2/auth/token" `
    -Method POST -Headers @{Authorization="Basic $authB64"} `
    -Body "grant_type=client_credentials" -ContentType "application/x-www-form-urlencoded").access_token

# Refresh secret key
Write-Host "Refreshing robot account secret key ($RobotUuid)..." -ForegroundColor Yellow
$newSecret = Invoke-RestMethod -Uri "https://vcr.api.vngcloud.vn/v1/user/$RobotUuid/refresh" `
    -Method GET -Headers @{Authorization="Bearer $TOKEN"}
Write-Host "New secret received (len=$($newSecret.Length))" -ForegroundColor Green

# Update registry-credentials.json
$regJson  = "$ProjectDir\registry-credentials.json"
$regCreds = Get-Content $regJson -Raw | ConvertFrom-Json
$regCreds.password = $newSecret
$regCreds | ConvertTo-Json | Set-Content $regJson -Encoding UTF8
Write-Host "registry-credentials.json updated" -ForegroundColor Green

# Verify Docker login
Write-Host "`nVerifying Docker login..." -ForegroundColor Cyan
docker logout $Registry 2>&1 | Out-Null
& docker login $Registry -u $regCreds.username -p $newSecret
if ($LASTEXITCODE -eq 0) {
    Write-Host "Docker login OK -- ready to push" -ForegroundColor Green
} else {
    Write-Host "Docker login still failing -- check robot account status on vCR console" -ForegroundColor Red
    exit 1
}
