from enum import Enum


class ApiTestStepType(str, Enum):
    STEP = "Step"
    CONDITION = "Condition"
    NESTEDTESTCASE = "NestedTestCase"

    def __str__(self) -> str:
        return str(self.value)
