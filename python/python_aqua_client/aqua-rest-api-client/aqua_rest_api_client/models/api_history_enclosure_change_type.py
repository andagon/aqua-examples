from enum import Enum


class ApiHistoryEnclosureChangeType(str, Enum):
    ADDED = "Added"
    MODIFIED = "Modified"
    DELETED = "Deleted"

    def __str__(self) -> str:
        return str(self.value)
