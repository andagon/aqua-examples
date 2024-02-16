from enum import Enum


class ApiAgentSimpleStatus(str, Enum):
    BLOCKEDORNOAGENTS = "BlockedOrNoAgents"
    AVAILABLE = "Available"
    PARTIALLYAVAILABLE = "PartiallyAvailable"
    UNAVAILABLE = "Unavailable"
    NORESPONSEYET = "NoResponseYet"

    def __str__(self) -> str:
        return str(self.value)
