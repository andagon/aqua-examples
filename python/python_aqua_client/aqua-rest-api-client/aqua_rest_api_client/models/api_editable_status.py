from enum import Enum


class ApiEditableStatus(str, Enum):
    EDITABLE = "Editable"
    LOCKED = "Locked"
    NOPERMISSIONTOEDIT = "NoPermissionToEdit"
    NOPERMISSIONTOVIEW = "NoPermissionToView"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
