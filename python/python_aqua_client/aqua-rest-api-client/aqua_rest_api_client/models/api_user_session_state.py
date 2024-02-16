from enum import Enum


class ApiUserSessionState(str, Enum):
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def __str__(self) -> str:
        return str(self.value)
