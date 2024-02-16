from enum import Enum


class ApiNotificationRuleFilterType(str, Enum):
    NONE = "None"
    CUSTOM = "Custom"
    ANYCHANGE = "AnyChange"

    def __str__(self) -> str:
        return str(self.value)
