from enum import Enum


class ApiReportPrintoutDefaultBoolean(str, Enum):
    TRUE = "True"
    FALSE = "False"
    DEFAULT = "Default"

    def __str__(self) -> str:
        return str(self.value)
