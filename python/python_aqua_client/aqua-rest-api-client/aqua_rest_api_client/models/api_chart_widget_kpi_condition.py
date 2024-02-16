from enum import Enum


class ApiChartWidgetKPICondition(str, Enum):
    EQUAL = "Equal"
    NOTEQUAL = "NotEqual"
    LESS = "Less"
    LESSEQUAL = "LessEqual"
    GREATER = "Greater"
    GREATEREQUAL = "GreaterEqual"

    def __str__(self) -> str:
        return str(self.value)
