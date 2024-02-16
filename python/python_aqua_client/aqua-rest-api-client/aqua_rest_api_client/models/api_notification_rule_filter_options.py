from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNotificationRuleFilterOptions")


@attr.s(auto_attribs=True)
class ApiNotificationRuleFilterOptions:
    """The type options of notification rule.

    Attributes:
        base_object_changed_properties (Union[Unset, bool]): Any change of base object property.
        base_object_changed_status (Union[Unset, bool]): Base object's status field has changed.
        base_object_accepted_statuses (Union[Unset, None, str]): List of accepted statuses as comma separated list.
        base_object_created (Union[Unset, bool]): Base object has been created.
        base_object_moved (Union[Unset, bool]): Base object has been moved between folders.
        base_object_deleted (Union[Unset, bool]): Base object has been deleted.
        base_object_change_under_assignment (Union[Unset, bool]): Base object has been changed (including changed
            properties, create, delete, move)
            assigned user notification.
        base_object_change_under_ownership (Union[Unset, bool]): Base object has been changed (including changed
            properties, create, delete, move)
            owner notification.
        base_object_assigned (Union[Unset, bool]): Base object has been assigned.
    """

    base_object_changed_properties: Union[Unset, bool] = UNSET
    base_object_changed_status: Union[Unset, bool] = UNSET
    base_object_accepted_statuses: Union[Unset, None, str] = UNSET
    base_object_created: Union[Unset, bool] = UNSET
    base_object_moved: Union[Unset, bool] = UNSET
    base_object_deleted: Union[Unset, bool] = UNSET
    base_object_change_under_assignment: Union[Unset, bool] = UNSET
    base_object_change_under_ownership: Union[Unset, bool] = UNSET
    base_object_assigned: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        base_object_changed_properties = self.base_object_changed_properties
        base_object_changed_status = self.base_object_changed_status
        base_object_accepted_statuses = self.base_object_accepted_statuses
        base_object_created = self.base_object_created
        base_object_moved = self.base_object_moved
        base_object_deleted = self.base_object_deleted
        base_object_change_under_assignment = self.base_object_change_under_assignment
        base_object_change_under_ownership = self.base_object_change_under_ownership
        base_object_assigned = self.base_object_assigned

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if base_object_changed_properties is not UNSET:
            field_dict["BaseObjectChangedProperties"] = base_object_changed_properties
        if base_object_changed_status is not UNSET:
            field_dict["BaseObjectChangedStatus"] = base_object_changed_status
        if base_object_accepted_statuses is not UNSET:
            field_dict["BaseObjectAcceptedStatuses"] = base_object_accepted_statuses
        if base_object_created is not UNSET:
            field_dict["BaseObjectCreated"] = base_object_created
        if base_object_moved is not UNSET:
            field_dict["BaseObjectMoved"] = base_object_moved
        if base_object_deleted is not UNSET:
            field_dict["BaseObjectDeleted"] = base_object_deleted
        if base_object_change_under_assignment is not UNSET:
            field_dict["BaseObjectChangeUnderAssignment"] = base_object_change_under_assignment
        if base_object_change_under_ownership is not UNSET:
            field_dict["BaseObjectChangeUnderOwnership"] = base_object_change_under_ownership
        if base_object_assigned is not UNSET:
            field_dict["BaseObjectAssigned"] = base_object_assigned

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base_object_changed_properties = d.pop("BaseObjectChangedProperties", UNSET)

        base_object_changed_status = d.pop("BaseObjectChangedStatus", UNSET)

        base_object_accepted_statuses = d.pop("BaseObjectAcceptedStatuses", UNSET)

        base_object_created = d.pop("BaseObjectCreated", UNSET)

        base_object_moved = d.pop("BaseObjectMoved", UNSET)

        base_object_deleted = d.pop("BaseObjectDeleted", UNSET)

        base_object_change_under_assignment = d.pop("BaseObjectChangeUnderAssignment", UNSET)

        base_object_change_under_ownership = d.pop("BaseObjectChangeUnderOwnership", UNSET)

        base_object_assigned = d.pop("BaseObjectAssigned", UNSET)

        api_notification_rule_filter_options = cls(
            base_object_changed_properties=base_object_changed_properties,
            base_object_changed_status=base_object_changed_status,
            base_object_accepted_statuses=base_object_accepted_statuses,
            base_object_created=base_object_created,
            base_object_moved=base_object_moved,
            base_object_deleted=base_object_deleted,
            base_object_change_under_assignment=base_object_change_under_assignment,
            base_object_change_under_ownership=base_object_change_under_ownership,
            base_object_assigned=base_object_assigned,
        )

        return api_notification_rule_filter_options
