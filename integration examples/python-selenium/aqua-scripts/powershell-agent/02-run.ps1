using namespace aqua.ProcessEngine.WebServiceProxy

param($aquaCallback)

$aquaCallback.SendMessage(
    "Start test execution.",
    [ExecutionLogMessageType]::InformationalInfo,
    "PowerShell")

Push-Location "../aqua-examples/integration examples/python-selenium"

# Create a new folder for screenshot uploads
New-Item -Type Directory -Name screenshots

# poetry has to be in path for this to work
poetry run python main.py

# capture the return state
$result = $?

# Upload screenshots
Get-ChildItem -Path screenshots | ForEach-Object {
    $aquaCallback.AddExecutionAttachment($_.FullName)
}

# Check exit code and fail the execution if it's not 0
if ($false -ne $result) {
    return "Fail"
}

return "Ready"