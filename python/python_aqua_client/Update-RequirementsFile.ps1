#Requires -Version 7.2
<#
    .SYNOPSIS
        Update given requirements file
    
    .DESCRIPTION
        This function will search for the project toml.
        Extract the aqua client version from there and replace it in the requirements file.
#>
[CmdletBinding()]
param (
    [string] $requirementsFile = "../python_project/requirements.txt"
)

$ErrorActionPreference = "Stop"

$projectFile = "$PSScriptRoot/aqua-rest-api-client/pyproject.toml"

Get-Content $projectFile | Select-String -Pattern '^version = ' -outvariable clientVersion

# cleanup the string
$clientVersion = $clientVersion -replace "version = ",""
$clientVersion = $clientVersion -replace '"', ''

$wheelStartString = "../python_aqua_client/aqua-rest-api-client/dist"
$newWheelPath = "$wheelStartString/aqua_rest_api_client-$clientVersion-py3-none-any.whl"

# remove old wheel
(Get-Content $requirementsFile) | Select-String -Pattern "^$wheelStartString" -NotMatch | Set-Content $requirementsFile
# add the new wheel
Add-Content $requirementsFile $newWheelPath 