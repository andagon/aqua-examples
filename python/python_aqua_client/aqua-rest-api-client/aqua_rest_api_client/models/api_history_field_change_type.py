from enum import Enum


class ApiHistoryFieldChangeType(str, Enum):
    ADDED = "Added"
    CHANGED = "Changed"
    REMOVED = "Removed"
    CHANGEDNODIFF = "ChangedNoDiff"

    def __str__(self) -> str:
        return str(self.value)
