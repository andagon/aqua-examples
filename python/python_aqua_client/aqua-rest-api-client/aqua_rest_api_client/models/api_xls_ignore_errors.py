from enum import Enum


class ApiXlsIgnoreErrors(str, Enum):
    NONE = "None"
    NUMBERSTOREDASTEXT = "NumberStoredAsText"

    def __str__(self) -> str:
        return str(self.value)
