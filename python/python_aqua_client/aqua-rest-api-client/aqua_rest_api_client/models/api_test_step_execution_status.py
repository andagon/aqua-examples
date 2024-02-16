from enum import Enum


class ApiTestStepExecutionStatus(str, Enum):
    NOTRUN = "NotRun"
    FAILED = "Failed"
    PASS = "Pass"
    QUEUED = "Queued"
    INPROGRESS = "InProgress"
    ABORTED = "Aborted"
    BLOCKED = "Blocked"
    NOTAPPLICABLE = "NotApplicable"

    def __str__(self) -> str:
        return str(self.value)
