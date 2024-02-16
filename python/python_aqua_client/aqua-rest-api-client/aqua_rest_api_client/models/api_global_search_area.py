from enum import Enum


class ApiGlobalSearchArea(str, Enum):
    ALLITEMS = "AllItems"
    REQUIREMENTS = "Requirements"
    DEFECTS = "Defects"
    TESTCASES = "TestCases"
    TESTSCENARIOS = "TestScenarios"
    SCRIPTS = "Scripts"

    def __str__(self) -> str:
        return str(self.value)
