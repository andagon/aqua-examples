from enum import Enum


class ApiHistoryDependencyChangeType(str, Enum):
    ADDED = "Added"
    TYPECHANGED = "TypeChanged"
    REMOVED = "Removed"

    def __str__(self) -> str:
        return str(self.value)
