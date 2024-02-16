from enum import Enum


class ApiTestStepExecutionUpdateStatus(str, Enum):
    NOTRUN = "NotRun"
    PASS = "Pass"
    FAILED = "Failed"
    BLOCKED = "Blocked"
    NOTAPPLICABLE = "NotApplicable"

    def __str__(self) -> str:
        return str(self.value)
