from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_folder_notification_rule import ApiFolderNotificationRule


T = TypeVar("T", bound="ApiFolderNotificationRuleResponse")


@attr.s(auto_attribs=True)
class ApiFolderNotificationRuleResponse:
    """Contains the folder notification active and Inheritable rule.

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
        active_folder_rule (Union[Unset, None, ApiFolderNotificationRule]): Contains the folder notification rule.
        next_inheritable_rule (Union[Unset, None, ApiFolderNotificationRule]): Contains the folder notification rule.
    """

    item_type: Union[Unset, ApiItemType] = UNSET
    active_folder_rule: Union[Unset, None, "ApiFolderNotificationRule"] = UNSET
    next_inheritable_rule: Union[Unset, None, "ApiFolderNotificationRule"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        active_folder_rule: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.active_folder_rule, Unset):
            active_folder_rule = self.active_folder_rule.to_dict() if self.active_folder_rule else None

        next_inheritable_rule: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.next_inheritable_rule, Unset):
            next_inheritable_rule = self.next_inheritable_rule.to_dict() if self.next_inheritable_rule else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if active_folder_rule is not UNSET:
            field_dict["ActiveFolderRule"] = active_folder_rule
        if next_inheritable_rule is not UNSET:
            field_dict["NextInheritableRule"] = next_inheritable_rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_folder_notification_rule import ApiFolderNotificationRule

        d = src_dict.copy()
        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        _active_folder_rule = d.pop("ActiveFolderRule", UNSET)
        active_folder_rule: Union[Unset, None, ApiFolderNotificationRule]
        if _active_folder_rule is None:
            active_folder_rule = None
        elif isinstance(_active_folder_rule, Unset):
            active_folder_rule = UNSET
        else:
            active_folder_rule = ApiFolderNotificationRule.from_dict(_active_folder_rule)

        _next_inheritable_rule = d.pop("NextInheritableRule", UNSET)
        next_inheritable_rule: Union[Unset, None, ApiFolderNotificationRule]
        if _next_inheritable_rule is None:
            next_inheritable_rule = None
        elif isinstance(_next_inheritable_rule, Unset):
            next_inheritable_rule = UNSET
        else:
            next_inheritable_rule = ApiFolderNotificationRule.from_dict(_next_inheritable_rule)

        api_folder_notification_rule_response = cls(
            item_type=item_type,
            active_folder_rule=active_folder_rule,
            next_inheritable_rule=next_inheritable_rule,
        )

        return api_folder_notification_rule_response
