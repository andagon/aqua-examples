from enum import Enum


class ApiPermissionResult(str, Enum):
    DENIED = "Denied"
    NOTLICENSED = "NotLicensed"
    GRANTED = "Granted"

    def __str__(self) -> str:
        return str(self.value)
