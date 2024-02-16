from enum import Enum


class ApiTestCaseRunStatus(str, Enum):
    NOTRUN = "NotRun"
    NOTCOMPLETED = "NotCompleted"
    FAILED = "Failed"
    PASSED = "Passed"
    BLOCKED = "Blocked"
    NOTAPPLICABLE = "NotApplicable"

    def __str__(self) -> str:
        return str(self.value)
