from enum import Enum


class ApiReportXlsPrintoutEncryptionType(str, Enum):
    STRONG = "Strong"
    COMPATIBLE = "Compatible"

    def __str__(self) -> str:
        return str(self.value)
