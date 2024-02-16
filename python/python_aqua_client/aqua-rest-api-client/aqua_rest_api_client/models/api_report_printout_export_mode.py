from enum import Enum


class ApiReportPrintoutExportMode(str, Enum):
    SINGLEFILE = "SingleFile"
    SINGLEFILEPAGEBYPAGE = "SingleFilePageByPage"

    def __str__(self) -> str:
        return str(self.value)
