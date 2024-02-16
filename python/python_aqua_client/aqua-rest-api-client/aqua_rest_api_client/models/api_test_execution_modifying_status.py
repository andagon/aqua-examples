from enum import Enum


class ApiTestExecutionModifyingStatus(str, Enum):
    FINISHED = "Finished"
    EXECUTING = "Executing"

    def __str__(self) -> str:
        return str(self.value)
