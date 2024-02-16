from enum import Enum


class ApiTestDataFileFormat(str, Enum):
    XLS = "XLS"
    XLSX = "XLSX"
    XML = "XML"
    CSV = "CSV"

    def __str__(self) -> str:
        return str(self.value)
