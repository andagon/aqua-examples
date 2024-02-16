from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_notification_rule_filter_type import ApiNotificationRuleFilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_location import ApiItemLocation
    from ..models.api_notification_rule_filter_options import ApiNotificationRuleFilterOptions
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiFolderNotificationRule")


@attr.s(auto_attribs=True)
class ApiFolderNotificationRule:
    """Contains the folder notification rule.

    Attributes:
        notification_location (Union[Unset, None, ApiItemLocation]): Specifies the location (project and folder) of an
            item
        created_by_user (Union[Unset, None, ApiUserInfo]): The user information
        owner (Union[Unset, None, ApiUserInfo]): The user information
        id (Union[Unset, int]): The id of the rule.
        filter_type (Union[Unset, ApiNotificationRuleFilterType]): The type of notification rule filter.
            This enum has the following values:
              - `AnyChange` Any change notification.
              - `Custom` Custom notification filter.
              - `None` No notification filter.
        custom_filter_options (Union[Unset, None, ApiNotificationRuleFilterOptions]): The type options of notification
            rule.
        ignore_if_owner_action (Union[Unset, bool]): Ignore if owner action.
        recursive (Union[Unset, bool]): Use this rule for all subfolders.
        inherited (Union[Unset, bool]): Indicates if this rule is inherited.
        inherited_from_project_default (Union[Unset, bool]): Indicates if this rule is inherited from project default.
    """

    notification_location: Union[Unset, None, "ApiItemLocation"] = UNSET
    created_by_user: Union[Unset, None, "ApiUserInfo"] = UNSET
    owner: Union[Unset, None, "ApiUserInfo"] = UNSET
    id: Union[Unset, int] = UNSET
    filter_type: Union[Unset, ApiNotificationRuleFilterType] = UNSET
    custom_filter_options: Union[Unset, None, "ApiNotificationRuleFilterOptions"] = UNSET
    ignore_if_owner_action: Union[Unset, bool] = UNSET
    recursive: Union[Unset, bool] = UNSET
    inherited: Union[Unset, bool] = UNSET
    inherited_from_project_default: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        notification_location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.notification_location, Unset):
            notification_location = self.notification_location.to_dict() if self.notification_location else None

        created_by_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = self.created_by_user.to_dict() if self.created_by_user else None

        owner: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict() if self.owner else None

        id = self.id
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        custom_filter_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_filter_options, Unset):
            custom_filter_options = self.custom_filter_options.to_dict() if self.custom_filter_options else None

        ignore_if_owner_action = self.ignore_if_owner_action
        recursive = self.recursive
        inherited = self.inherited
        inherited_from_project_default = self.inherited_from_project_default

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if notification_location is not UNSET:
            field_dict["NotificationLocation"] = notification_location
        if created_by_user is not UNSET:
            field_dict["CreatedByUser"] = created_by_user
        if owner is not UNSET:
            field_dict["Owner"] = owner
        if id is not UNSET:
            field_dict["Id"] = id
        if filter_type is not UNSET:
            field_dict["FilterType"] = filter_type
        if custom_filter_options is not UNSET:
            field_dict["CustomFilterOptions"] = custom_filter_options
        if ignore_if_owner_action is not UNSET:
            field_dict["IgnoreIfOwnerAction"] = ignore_if_owner_action
        if recursive is not UNSET:
            field_dict["Recursive"] = recursive
        if inherited is not UNSET:
            field_dict["Inherited"] = inherited
        if inherited_from_project_default is not UNSET:
            field_dict["InheritedFromProjectDefault"] = inherited_from_project_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_location import ApiItemLocation
        from ..models.api_notification_rule_filter_options import ApiNotificationRuleFilterOptions
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        _notification_location = d.pop("NotificationLocation", UNSET)
        notification_location: Union[Unset, None, ApiItemLocation]
        if _notification_location is None:
            notification_location = None
        elif isinstance(_notification_location, Unset):
            notification_location = UNSET
        else:
            notification_location = ApiItemLocation.from_dict(_notification_location)

        _created_by_user = d.pop("CreatedByUser", UNSET)
        created_by_user: Union[Unset, None, ApiUserInfo]
        if _created_by_user is None:
            created_by_user = None
        elif isinstance(_created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = ApiUserInfo.from_dict(_created_by_user)

        _owner = d.pop("Owner", UNSET)
        owner: Union[Unset, None, ApiUserInfo]
        if _owner is None:
            owner = None
        elif isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = ApiUserInfo.from_dict(_owner)

        id = d.pop("Id", UNSET)

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

        recursive = d.pop("Recursive", UNSET)

        inherited = d.pop("Inherited", UNSET)

        inherited_from_project_default = d.pop("InheritedFromProjectDefault", UNSET)

        api_folder_notification_rule = cls(
            notification_location=notification_location,
            created_by_user=created_by_user,
            owner=owner,
            id=id,
            filter_type=filter_type,
            custom_filter_options=custom_filter_options,
            ignore_if_owner_action=ignore_if_owner_action,
            recursive=recursive,
            inherited=inherited,
            inherited_from_project_default=inherited_from_project_default,
        )

        return api_folder_notification_rule
