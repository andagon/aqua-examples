from enum import Enum


class PdfEncryptionLevel(str, Enum):
    AES128 = "AES128"
    AES256 = "AES256"
    ARC4 = "ARC4"

    def __str__(self) -> str:
        return str(self.value)
