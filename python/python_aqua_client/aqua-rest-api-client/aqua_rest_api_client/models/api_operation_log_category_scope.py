from enum import Enum


class ApiOperationLogCategoryScope(str, Enum):
    GLOBAL = "Global"
    PROJECT = "Project"

    def __str__(self) -> str:
        return str(self.value)
