from enum import Enum


class ApiAquaClientType(str, Enum):
    UNKNOWN = "Unknown"
    RICH = "Rich"
    OFFLINE = "Offline"
    WEB = "Web"
    API = "API"

    def __str__(self) -> str:
        return str(self.value)
