from enum import Enum


class ApiEnclosureType(str, Enum):
    DESCRIPTION = "Description"
    NOTE = "Note"
    REPLICATIONPROCEDURE = "ReplicationProcedure"
    RESOLUTION = "Resolution"

    def __str__(self) -> str:
        return str(self.value)
