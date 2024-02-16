from enum import Enum


class ApiReportPrintoutExportImageType(str, Enum):
    JPEG = "jpeg"
    PNG = "png"
    GIF = "gif"

    def __str__(self) -> str:
        return str(self.value)
