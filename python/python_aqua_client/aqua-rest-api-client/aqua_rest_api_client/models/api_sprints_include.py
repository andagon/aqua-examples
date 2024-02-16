from enum import Enum


class ApiSprintsInclude(str, Enum):
    ALL = "All"
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def __str__(self) -> str:
        return str(self.value)
