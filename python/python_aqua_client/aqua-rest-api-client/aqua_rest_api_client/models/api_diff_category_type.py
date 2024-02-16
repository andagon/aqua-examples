from enum import Enum


class ApiDiffCategoryType(str, Enum):
    TEMPLATE = "Template"
    WORKFLOW = "Workflow"
    SUBTEMPLATE = "Subtemplate"
    NOTIFICATION = "Notification"
    FIELDRULES = "FieldRules"

    def __str__(self) -> str:
        return str(self.value)
