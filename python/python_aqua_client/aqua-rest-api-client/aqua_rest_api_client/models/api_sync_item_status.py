from enum import Enum


class ApiSyncItemStatus(str, Enum):
    OK = "Ok"
    WARNING = "Warning"
    ERROR = "Error"
    UNSYNCED = "Unsynced"

    def __str__(self) -> str:
        return str(self.value)
