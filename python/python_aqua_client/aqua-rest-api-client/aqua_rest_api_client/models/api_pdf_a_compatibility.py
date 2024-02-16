from enum import Enum


class ApiPdfACompatibility(str, Enum):
    NONE = "None"
    PDFA1A = "PdfA1a"
    PDFA1B = "PdfA1b"
    PDFA2A = "PdfA2a"
    PDFA2B = "PdfA2b"
    PDFA3A = "PdfA3a"
    PDFA3B = "PdfA3b"

    def __str__(self) -> str:
        return str(self.value)
