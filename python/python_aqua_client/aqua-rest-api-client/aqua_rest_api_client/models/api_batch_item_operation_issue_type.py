from enum import Enum


class ApiBatchItemOperationIssueType(str, Enum):
    ITEMERROR = "ItemError"
    ITEMWARNING = "ItemWarning"
    ITEMINFORMATION = "ItemInformation"
    FIELDERROR = "FieldError"
    FIELDWARNING = "FieldWarning"
    FIELDINFORMATION = "FieldInformation"

    def __str__(self) -> str:
        return str(self.value)
