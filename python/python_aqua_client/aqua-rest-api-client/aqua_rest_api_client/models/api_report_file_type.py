from enum import Enum


class ApiReportFileType(str, Enum):
    PDF = "Pdf"
    HTML = "Html"
    MHT = "Mht"
    RTF = "Rtf"
    XLS = "Xls"
    XLSX = "Xlsx"
    CSV = "Csv"
    TEXT = "Text"
    IMAGE = "Image"
    DOCX = "Docx"

    def __str__(self) -> str:
        return str(self.value)
