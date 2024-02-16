from enum import Enum


class ApiReportPrintoutTextExportMode(str, Enum):
    TEXT = "Text"
    VALUE = "Value"

    def __str__(self) -> str:
        return str(self.value)
