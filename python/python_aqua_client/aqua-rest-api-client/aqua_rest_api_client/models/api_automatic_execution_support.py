from enum import Enum


class ApiAutomaticExecutionSupport(str, Enum):
    NONE = "None"
    PARTIALLY = "Partially"
    COMPLETE = "Complete"

    def __str__(self) -> str:
        return str(self.value)
