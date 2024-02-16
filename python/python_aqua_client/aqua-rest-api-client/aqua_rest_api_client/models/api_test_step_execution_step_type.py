from enum import Enum


class ApiTestStepExecutionStepType(str, Enum):
    CONDITION = "Condition"
    STEP = "Step"

    def __str__(self) -> str:
        return str(self.value)
