from enum import Enum


class ApiTestScenarioRunStatus(str, Enum):
    NOTRUN = "NotRun"
    NOTCOMPLETED = "NotCompleted"
    FAILED = "Failed"
    PASSED = "Passed"
    BLOCKED = "Blocked"

    def __str__(self) -> str:
        return str(self.value)
