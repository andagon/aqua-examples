from enum import Enum


class ApiTestExecutionType(str, Enum):
    MANUAL = "Manual"
    AUTOMATED = "Automated"

    def __str__(self) -> str:
        return str(self.value)
