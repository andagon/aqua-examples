from enum import Enum


class ApiHistoryPostChangeType(str, Enum):
    ADDED = "Added"
    MODIFIED = "Modified"
    REMOVED = "Removed"

    def __str__(self) -> str:
        return str(self.value)
