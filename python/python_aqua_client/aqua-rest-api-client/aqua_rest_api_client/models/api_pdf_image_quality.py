from enum import Enum


class ApiPdfImageQuality(str, Enum):
    LOWEST = "Lowest"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    HIGHEST = "Highest"

    def __str__(self) -> str:
        return str(self.value)
