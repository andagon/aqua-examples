from enum import Enum


class ApiExecutionLogMessageType(str, Enum):
    SUTERROR = "SUTError"
    SCRIPTEXECUTIONERROR = "ScriptExecutionError"
    PREPARATIONERROR = "PreparationError"
    EXECUTIONERROR = "ExecutionError"
    INFORMATIONALINFO = "InformationalInfo"
    INFORMATIONALDEBUG = "InformationalDebug"
    INFORMATIONALWARN = "InformationalWarn"
    INFORMATIONALSUCCESS = "InformationalSuccess"

    def __str__(self) -> str:
        return str(self.value)
