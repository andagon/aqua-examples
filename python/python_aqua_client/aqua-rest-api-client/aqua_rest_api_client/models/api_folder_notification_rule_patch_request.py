from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_folder_notification_rule_patch_types import ApiFolderNotificationRulePatchTypes
from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_folder_notification_rule_replacement import ApiFolderNotificationRuleReplacement


T = TypeVar("T", bound="ApiFolderNotificationRulePatchRequest")


@attr.s(auto_attribs=True)
class ApiFolderNotificationRulePatchRequest:
    """Represents the folder notification rule request.

    Attributes:
        item_type (Union[Unset, ApiItemType]): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        folder_id (Union[Unset, int]): The id of the folder.
        recursive (Union[Unset, bool]): Use this rule for all subfolders, this means all subfolder rules will be
            deleted.
        operation (Union[Unset, ApiFolderNotificationRulePatchTypes]): Represents the folder notification rules patch
            types.
            This enum has the following values:
              - `UseInheritedNotificationRule` Use the inherited notification rule,
            if the recusrive flag is set all user rules will be deleted.
              - `UseThisNotificationRule` Use this notification rule.
        rule (Union[Unset, None, ApiFolderNotificationRuleReplacement]): Contains the necessary information to create a
            new folder notification rule.
    """

    item_type: Union[Unset, ApiItemType] = UNSET
    folder_id: Union[Unset, int] = UNSET
    recursive: Union[Unset, bool] = UNSET
    operation: Union[Unset, ApiFolderNotificationRulePatchTypes] = UNSET
    rule: Union[Unset, None, "ApiFolderNotificationRuleReplacement"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        folder_id = self.folder_id
        recursive = self.recursive
        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        rule: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict() if self.rule else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if recursive is not UNSET:
            field_dict["Recursive"] = recursive
        if operation is not UNSET:
            field_dict["Operation"] = operation
        if rule is not UNSET:
            field_dict["Rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_folder_notification_rule_replacement import ApiFolderNotificationRuleReplacement

        d = src_dict.copy()
        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        folder_id = d.pop("FolderId", UNSET)

        recursive = d.pop("Recursive", UNSET)

        _operation = d.pop("Operation", UNSET)
        operation: Union[Unset, ApiFolderNotificationRulePatchTypes]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = ApiFolderNotificationRulePatchTypes(_operation)

        _rule = d.pop("Rule", UNSET)
        rule: Union[Unset, None, ApiFolderNotificationRuleReplacement]
        if _rule is None:
            rule = None
        elif isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = ApiFolderNotificationRuleReplacement.from_dict(_rule)

        api_folder_notification_rule_patch_request = cls(
            item_type=item_type,
            folder_id=folder_id,
            recursive=recursive,
            operation=operation,
            rule=rule,
        )

        return api_folder_notification_rule_patch_request
