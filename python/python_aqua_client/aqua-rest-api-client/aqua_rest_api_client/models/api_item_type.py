from enum import Enum


class ApiItemType(str, Enum):
    DEFECT = "Defect"
    REQUIREMENT = "Requirement"
    TESTCASE = "TestCase"
    TESTSCENARIO = "TestScenario"
    TESTEXECUTION = "TestExecution"
    SCRIPT = "Script"
    EXTERNALJIRA = "ExternalJira"
    EXTERNALOTRS = "ExternalOtrs"

    def __str__(self) -> str:
        return str(self.value)
