from enum import Enum


class ApiHistorySyncEventType(str, Enum):
    ERROR = "Error"
    ERRORRESOLVED = "ErrorResolved"

    def __str__(self) -> str:
        return str(self.value)
