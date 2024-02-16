from enum import Enum


class ApiBatchItemUpdateIssueDetailsType(str, Enum):
    NOTFOUND = "NotFound"
    LOCKED = "Locked"
    DENIED = "Denied"
    VALUENOTALLOWED = "ValueNotAllowed"
    FAILURE = "Failure"
    FIELDINCOMPATIBLE = "FieldIncompatible"

    def __str__(self) -> str:
        return str(self.value)
