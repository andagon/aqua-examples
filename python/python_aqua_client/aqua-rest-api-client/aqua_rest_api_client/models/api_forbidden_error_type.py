from enum import Enum


class ApiForbiddenErrorType(str, Enum):
    NOTLICENSED = "NotLicensed"
    NOTPERMITTED = "NotPermitted"

    def __str__(self) -> str:
        return str(self.value)
