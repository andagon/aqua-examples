from enum import Enum


class ApiBaseItemAccessibility(str, Enum):
    ACCESSIBLE = "Accessible"
    DELETED = "Deleted"
    NOPERMISSIONS = "NoPermissions"
    ARCHIVED = "Archived"

    def __str__(self) -> str:
        return str(self.value)
