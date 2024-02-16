from enum import Enum


class ApiPdfPrintingPermissions(str, Enum):
    NONE = "None"
    LOWRESOLUTION = "LowResolution"
    HIGHRESOLUTION = "HighResolution"

    def __str__(self) -> str:
        return str(self.value)
