from enum import Enum


class ApiLicenseType(str, Enum):
    FLOATED = "Floated"
    NAMED = "Named"

    def __str__(self) -> str:
        return str(self.value)
