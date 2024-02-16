from enum import Enum


class ApiProjectNotificationType(str, Enum):
    BASEOBJECTCHANGEDPROPERTIES = "BaseObjectChangedProperties"
    BASEOBJECTCHANGEDSTATUS = "BaseObjectChangedStatus"
    BASEOBJECTCREATED = "BaseObjectCreated"
    BASEOBJECTMOVED = "BaseObjectMoved"
    BASEOBJECTDELETED = "BaseObjectDeleted"

    def __str__(self) -> str:
        return str(self.value)
