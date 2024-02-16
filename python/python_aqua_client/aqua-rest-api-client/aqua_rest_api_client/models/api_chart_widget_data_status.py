from enum import Enum


class ApiChartWidgetDataStatus(str, Enum):
    OK = "OK"
    NOPERMISSION = "NoPermission"
    INVALIDFILTER = "InvalidFilter"
    INVALIDSPECIFICATION = "InvalidSpecification"

    def __str__(self) -> str:
        return str(self.value)
