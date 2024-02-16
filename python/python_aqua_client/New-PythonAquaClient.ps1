#Requires -Version 7.2
<#
    .SYNOPSIS
        Update/Create an aqua python client

    .DESCRIPTION
        This function will download the swagger file from the given url.
        Fix the known issues, generate the client.
        The generated client will be build as universall wheel and replaced in the requirements file.
#>
[CmdletBinding()]
param (
    [string] $aquaUrl = "https://app.aqua-cloud.io/" # change to your aqua instance url
)

$ErrorActionPreference = "Stop"

# Setup Python virtual environment with dependencies
python -m venv .venv
. .\.venv\Scripts\activate
pip install -r requirements.txt

# Download swagger file
$swaggerFile = "./swagger.json"
Invoke-WebRequest -Uri "$aquaUrl/aquawebng/swagger/v1/swagger.json" -OutFile $swaggerFile

# Fix aqua swagger.json issue - changes content type "*/*" to "application/octet-stream"
.\Update-SwaggerFile.ps1 -swaggerFile $swaggerFile

# Remove old client
if (Test-Path $PSScriptRoot/aqua-rest-api-client) {
    Remove-Item $PSScriptRoot/aqua-rest-api-client -Recurse -Force
}

# generate client
openapi-python-client generate --path $swaggerFile

# build universal wheel
poetry build --directory=$PSScriptRoot/aqua-rest-api-client -f wheel

.\Update-RequirementsFile.ps1
