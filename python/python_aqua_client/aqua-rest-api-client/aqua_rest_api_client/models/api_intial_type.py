from enum import Enum


class ApiIntialType(str, Enum):
    ALL = "All"
    SINGLE = "Single"

    def __str__(self) -> str:
        return str(self.value)
