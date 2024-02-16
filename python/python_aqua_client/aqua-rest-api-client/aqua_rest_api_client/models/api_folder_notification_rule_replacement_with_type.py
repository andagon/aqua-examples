from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..models.api_notification_rule_filter_type import ApiNotificationRuleFilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_notification_rule_filter_options import ApiNotificationRuleFilterOptions


T = TypeVar("T", bound="ApiFolderNotificationRuleReplacementWithType")


@attr.s(auto_attribs=True)
class ApiFolderNotificationRuleReplacementWithType:
    """
    Attributes:
        filter_type (Union[Unset, ApiNotificationRuleFilterType]): The type of notification rule filter.
            This enum has the following values:
              - `AnyChange` Any change notification.
              - `Custom` Custom notification filter.
              - `None` No notification filter.
        custom_filter_options (Union[Unset, None, ApiNotificationRuleFilterOptions]): The type options of notification
            rule.
        ignore_if_owner_action (Union[Unset, bool]): Ignore if owner action.
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
    """

    filter_type: Union[Unset, ApiNotificationRuleFilterType] = UNSET
    custom_filter_options: Union[Unset, None, "ApiNotificationRuleFilterOptions"] = UNSET
    ignore_if_owner_action: Union[Unset, bool] = UNSET
    item_type: Union[Unset, ApiItemType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        custom_filter_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_filter_options, Unset):
            custom_filter_options = self.custom_filter_options.to_dict() if self.custom_filter_options else None

        ignore_if_owner_action = self.ignore_if_owner_action
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_type is not UNSET:
            field_dict["FilterType"] = filter_type
        if custom_filter_options is not UNSET:
            field_dict["CustomFilterOptions"] = custom_filter_options
        if ignore_if_owner_action is not UNSET:
            field_dict["IgnoreIfOwnerAction"] = ignore_if_owner_action
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_notification_rule_filter_options import ApiNotificationRuleFilterOptions

        d = src_dict.copy()
        _filter_type = d.pop("FilterType", UNSET)
        filter_type: Union[Unset, ApiNotificationRuleFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = ApiNotificationRuleFilterType(_filter_type)

        _custom_filter_options = d.pop("CustomFilterOptions", UNSET)
        custom_filter_options: Union[Unset, None, ApiNotificationRuleFilterOptions]
        if _custom_filter_options is None:
            custom_filter_options = None
        elif isinstance(_custom_filter_options, Unset):
            custom_filter_options = UNSET
        else:
            custom_filter_options = ApiNotificationRuleFilterOptions.from_dict(_custom_filter_options)

        ignore_if_owner_action = d.pop("IgnoreIfOwnerAction", UNSET)

        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        api_folder_notification_rule_replacement_with_type = cls(
            filter_type=filter_type,
            custom_filter_options=custom_filter_options,
            ignore_if_owner_action=ignore_if_owner_action,
            item_type=item_type,
        )

        api_folder_notification_rule_replacement_with_type.additional_properties = d
        return api_folder_notification_rule_replacement_with_type

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
