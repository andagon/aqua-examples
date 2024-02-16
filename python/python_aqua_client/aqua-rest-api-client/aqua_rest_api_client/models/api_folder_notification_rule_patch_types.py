from enum import Enum


class ApiFolderNotificationRulePatchTypes(str, Enum):
    USEINHERITEDNOTIFICATIONRULE = "UseInheritedNotificationRule"
    USETHISNOTIFICATIONRULE = "UseThisNotificationRule"

    def __str__(self) -> str:
        return str(self.value)
