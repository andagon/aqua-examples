from enum import Enum


class ApiHistoryCreationMode(str, Enum):
    EMPTYITEM = "EmptyItem"
    COPYOFITEM = "CopyOfItem"
    NEWVERSIONOFITEM = "NewVersionOfItem"

    def __str__(self) -> str:
        return str(self.value)
