from enum import Enum


class ApiImportPhase(str, Enum):
    INITIALIZING = "Initializing"
    READINGFILE = "ReadingFile"
    IMPORTINGREQUIREMENTS = "ImportingRequirements"
    IMPORTINGDEFECTS = "ImportingDefects"
    IMPORTINGTESTCASES = "ImportingTestCases"
    IMPORTINGTESTSCENARIOS = "ImportingTestScenarios"
    CREATINGDEPENDENCIES = "CreatingDependencies"
    CREATINGTESTJOBS = "CreatingTestJobs"
    CREATINGHIERARCHY = "CreatingHierarchy"
    FINISHING = "Finishing"
    DONE = "Done"
    ERROR = "Error"

    def __str__(self) -> str:
        return str(self.value)
