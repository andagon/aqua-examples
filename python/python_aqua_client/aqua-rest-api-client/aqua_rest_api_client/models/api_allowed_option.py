from enum import Enum


class ApiAllowedOption(str, Enum):
    ASKUSER = "AskUser"
    ALWAYSTRUE = "AlwaysTrue"
    ALWAYSFALSE = "AlwaysFalse"

    def __str__(self) -> str:
        return str(self.value)
