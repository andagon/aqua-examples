#Requires -Version 7.2
<#
    .SYNOPSIS
        Fixes known issues in the swagger file.
    
    .DESCRIPTION
        This function will resolve two issues.
        1. Fix aqua swagger.json issue - add "scopes" to "securitySchema"
        2. Fix aqua swagger.json issue - change content from "*/*" to "application/octet-stream"
#>
[CmdletBinding()]
param (
    [string] $swaggerFile = "./swagger.json"
)

$ErrorActionPreference = "Stop"

$swagger = Get-Content $swaggerFile | ConvertFrom-Json -Depth 100

# Fix aqua swagger.json issue - add "scopes" to "securitySchema"
Add-Member -MemberType NoteProperty -Name scopes -Value @{} -InputObject $swagger.components.securitySchemes.oauth2.flows.password

# Fix aqua swagger.json issue - change content from "*/*" to "application/octet-stream"
if( $swagger.paths -is [PSCustomObject] ) {
    $paths = ($swagger.paths.PSObject.Properties | Select-Object -Property Name)

    foreach($path in $paths) {
        $pathName = $path.name
        if ($swagger.paths.$pathName -isnot [PSCustomObject] ) {
            continue
        }
        
        $endpointMethods = $paths = ($swagger.paths.$pathName.PSObject.Properties | Select-Object -Property Name)
        foreach($endpoint in $endpointMethods) {
            $methodName = $endpoint.name
            if ($swagger.paths.$pathName.$methodName -isnot [PSCustomObject] ) {
                continue
            }

            if($swagger.paths.$pathName.$methodName.responses."200".content.PSobject.Properties.name -match "\*/\*") {
                Write-Host "Changed content type for methode $methodName of the endpoint $pathName"
                $content_value = $swagger.paths.$pathName.$methodName.responses."200".content."*/*"
                $swagger.paths.$pathName.$methodName.responses."200".content | Add-Member -NotePropertyName "application/octet-stream" -NotePropertyValue $content_value
                $swagger.paths.$pathName.$methodName.responses."200".content.PSObject.Properties.Remove("*/*")
            }
        }
    }
}

Set-Content $swaggerFile  -Value ($swagger | ConvertTo-Json -Depth 100)
