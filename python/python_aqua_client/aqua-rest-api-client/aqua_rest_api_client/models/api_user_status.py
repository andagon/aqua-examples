from enum import Enum


class ApiUserStatus(str, Enum):
    ACTIVATED = "Activated"
    DEACTIVATED = "Deactivated"
    LICENSEDEACTIVATED = "LicenseDeactivated"

    def __str__(self) -> str:
        return str(self.value)
