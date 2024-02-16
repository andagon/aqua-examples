from enum import Enum


class ApiDashboardNGSize(str, Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

    def __str__(self) -> str:
        return str(self.value)
