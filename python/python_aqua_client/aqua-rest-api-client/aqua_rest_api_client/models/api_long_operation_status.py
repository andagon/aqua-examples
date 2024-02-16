from enum import Enum


class ApiLongOperationStatus(str, Enum):
    QUEUED = "Queued"
    INPROGRESS = "InProgress"
    FINISHED = "Finished"
    FINISHEDWITHWARNING = "FinishedWithWarning"
    FAILED = "Failed"
    ABORTED = "Aborted"
    BLOCKEDBYANOTHERTASK = "BlockedByAnotherTask"

    def __str__(self) -> str:
        return str(self.value)
