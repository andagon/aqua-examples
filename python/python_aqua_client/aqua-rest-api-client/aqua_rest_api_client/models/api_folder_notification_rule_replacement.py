from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_notification_rule_filter_type import ApiNotificationRuleFilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_notification_rule_filter_options import ApiNotificationRuleFilterOptions


T = TypeVar("T", bound="ApiFolderNotificationRuleReplacement")


@attr.s(auto_attribs=True)
class ApiFolderNotificationRuleReplacement:
    """Contains the necessary information to create a new folder notification rule.

    Attributes:
        filter_type (Union[Unset, ApiNotificationRuleFilterType]): The type of notification rule filter.
            This enum has the following values:
              - `AnyChange` Any change notification.
              - `Custom` Custom notification filter.
              - `None` No notification filter.
        custom_filter_options (Union[Unset, None, ApiNotificationRuleFilterOptions]): The type options of notification
            rule.
        ignore_if_owner_action (Union[Unset, bool]): Ignore if owner action.
    """

    filter_type: Union[Unset, ApiNotificationRuleFilterType] = UNSET
    custom_filter_options: Union[Unset, None, "ApiNotificationRuleFilterOptions"] = UNSET
    ignore_if_owner_action: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        custom_filter_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_filter_options, Unset):
            custom_filter_options = self.custom_filter_options.to_dict() if self.custom_filter_options else None

        ignore_if_owner_action = self.ignore_if_owner_action

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if filter_type is not UNSET:
            field_dict["FilterType"] = filter_type
        if custom_filter_options is not UNSET:
            field_dict["CustomFilterOptions"] = custom_filter_options
        if ignore_if_owner_action is not UNSET:
            field_dict["IgnoreIfOwnerAction"] = ignore_if_owner_action

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

        api_folder_notification_rule_replacement = cls(
            filter_type=filter_type,
            custom_filter_options=custom_filter_options,
            ignore_if_owner_action=ignore_if_owner_action,
        )

        return api_folder_notification_rule_replacement
