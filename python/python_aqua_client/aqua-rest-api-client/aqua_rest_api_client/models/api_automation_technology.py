from enum import Enum


class ApiAutomationTechnology(str, Enum):
    NONE = "None"
    DATABASE = "Database"
    JENKINS = "Jenkins"
    JMETER = "JMeter"
    POWERSHELL = "PowerShell"
    QTP = "QTP"
    RANOREX = "Ranorex"
    SOAPUI = "SoapUI"
    UFT = "UFT"
    UNIXSHELL = "UnixShell"

    def __str__(self) -> str:
        return str(self.value)
