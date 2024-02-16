from enum import Enum


class ApiAgentExecutionStatus(str, Enum):
    IDLE = "Idle"
    EXECUTING = "Executing"
    OFFLINE = "Offline"

    def __str__(self) -> str:
        return str(self.value)
