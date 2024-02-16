from enum import Enum


class ApiTestExecutionStatus(str, Enum):
    NOTRUN = "NotRun"
    INCOMPLETE = "Incomplete"
    FAILED = "Failed"
    PASS = "Pass"
    QUEUED = "Queued"
    INPROGRESS = "InProgress"
    ABORTED = "Aborted"
    BLOCKED = "Blocked"
    WAITING = "Waiting"
    NOTAPPLICABLE = "NotApplicable"

    def __str__(self) -> str:
        return str(self.value)
