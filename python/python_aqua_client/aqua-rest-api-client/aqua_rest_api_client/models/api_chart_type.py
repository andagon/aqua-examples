from enum import Enum


class ApiChartType(str, Enum):
    PIE = "Pie"
    BAR = "Bar"
    BARSIDEBYSIDE = "BarSideBySide"
    BARSTACKED = "BarStacked"
    TABLE = "Table"

    def __str__(self) -> str:
        return str(self.value)
