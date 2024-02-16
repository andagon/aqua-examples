from enum import Enum


class ApiBatchOperationType(str, Enum):
    UNLOCK = "Unlock"

    def __str__(self) -> str:
        return str(self.value)
