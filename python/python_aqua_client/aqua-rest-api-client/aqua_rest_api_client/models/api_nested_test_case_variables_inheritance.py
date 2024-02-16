from enum import Enum


class ApiNestedTestCaseVariablesInheritance(str, Enum):
    PREFEROUTER = "PreferOuter"
    PREFERNESTED = "PreferNested"

    def __str__(self) -> str:
        return str(self.value)
