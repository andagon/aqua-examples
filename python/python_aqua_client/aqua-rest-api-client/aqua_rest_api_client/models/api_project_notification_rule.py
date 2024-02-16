from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..models.api_notification_rule_filter_type import ApiNotificationRuleFilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_notification_rule_filter_options import ApiNotificationRuleFilterOptions
    from ..models.api_project_id_name import ApiProjectIdName
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiProjectNotificationRule")


@attr.s(auto_attribs=True)
class ApiProjectNotificationRule:
    """Contains the project default notification rule.

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
        project_info (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
        created_by_user (Union[Unset, None, ApiUserInfo]): The user information
        id (Union[Unset, int]): The id of the rule.
        filter_type (Union[Unset, ApiNotificationRuleFilterType]): The type of notification rule filter.
            This enum has the following values:
              - `AnyChange` Any change notification.
              - `Custom` Custom notification filter.
              - `None` No notification filter.
        custom_filter_options (Union[Unset, None, ApiNotificationRuleFilterOptions]): The type options of notification
            rule.
        ignore_if_owner_action (Union[Unset, bool]): Ignore if owner action.
    """

    item_type: Union[Unset, ApiItemType] = UNSET
    project_info: Union[Unset, None, "ApiProjectIdName"] = UNSET
    created_by_user: Union[Unset, None, "ApiUserInfo"] = UNSET
    id: Union[Unset, int] = UNSET
    filter_type: Union[Unset, ApiNotificationRuleFilterType] = UNSET
    custom_filter_options: Union[Unset, None, "ApiNotificationRuleFilterOptions"] = UNSET
    ignore_if_owner_action: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        project_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project_info, Unset):
            project_info = self.project_info.to_dict() if self.project_info else None

        created_by_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = self.created_by_user.to_dict() if self.created_by_user else None

        id = self.id
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        custom_filter_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_filter_options, Unset):
            custom_filter_options = self.custom_filter_options.to_dict() if self.custom_filter_options else None

        ignore_if_owner_action = self.ignore_if_owner_action

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if project_info is not UNSET:
            field_dict["ProjectInfo"] = project_info
        if created_by_user is not UNSET:
            field_dict["CreatedByUser"] = created_by_user
        if id is not UNSET:
            field_dict["Id"] = id
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
        from ..models.api_project_id_name import ApiProjectIdName
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        _project_info = d.pop("ProjectInfo", UNSET)
        project_info: Union[Unset, None, ApiProjectIdName]
        if _project_info is None:
            project_info = None
        elif isinstance(_project_info, Unset):
            project_info = UNSET
        else:
            project_info = ApiProjectIdName.from_dict(_project_info)

        _created_by_user = d.pop("CreatedByUser", UNSET)
        created_by_user: Union[Unset, None, ApiUserInfo]
        if _created_by_user is None:
            created_by_user = None
        elif isinstance(_created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = ApiUserInfo.from_dict(_created_by_user)

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

        api_project_notification_rule = cls(
            item_type=item_type,
            project_info=project_info,
            created_by_user=created_by_user,
            id=id,
            filter_type=filter_type,
            custom_filter_options=custom_filter_options,
            ignore_if_owner_action=ignore_if_owner_action,
        )

        return api_project_notification_rule
