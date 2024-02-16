from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_editable_status import ApiEditableStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value_date_time import ApiFieldValueDateTime
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiEditableInfo")


@attr.s(auto_attribs=True)
class ApiEditableInfo:
    """Contains information about editable status of an item.

    Attributes:
        status (Union[Unset, ApiEditableStatus]):
            This enum has the following values:
              - `Editable` The item can be edited.
              - `Locked` The item is already locked (either by another user or
            by the same user in a different context)
              - `NoPermissionToEdit` The current user is not permitted to edit the item.
              - `NoPermissionToView` The current user is not permitted to view the item.
              - `Unknown` No information is provided whether the item is editable or not.
            The item should not be edited based on this editable status.
        locking_user (Union[Unset, None, ApiUserInfo]): The user information
        locking_date (Union[Unset, None, ApiFieldValueDateTime]):
    """

    status: Union[Unset, ApiEditableStatus] = UNSET
    locking_user: Union[Unset, None, "ApiUserInfo"] = UNSET
    locking_date: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        locking_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.locking_user, Unset):
            locking_user = self.locking_user.to_dict() if self.locking_user else None

        locking_date: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.locking_date, Unset):
            locking_date = self.locking_date.to_dict() if self.locking_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status is not UNSET:
            field_dict["Status"] = status
        if locking_user is not UNSET:
            field_dict["LockingUser"] = locking_user
        if locking_date is not UNSET:
            field_dict["LockingDate"] = locking_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_date_time import ApiFieldValueDateTime
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiEditableStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEditableStatus(_status)

        _locking_user = d.pop("LockingUser", UNSET)
        locking_user: Union[Unset, None, ApiUserInfo]
        if _locking_user is None:
            locking_user = None
        elif isinstance(_locking_user, Unset):
            locking_user = UNSET
        else:
            locking_user = ApiUserInfo.from_dict(_locking_user)

        _locking_date = d.pop("LockingDate", UNSET)
        locking_date: Union[Unset, None, ApiFieldValueDateTime]
        if _locking_date is None:
            locking_date = None
        elif isinstance(_locking_date, Unset):
            locking_date = UNSET
        else:
            locking_date = ApiFieldValueDateTime.from_dict(_locking_date)

        api_editable_info = cls(
            status=status,
            locking_user=locking_user,
            locking_date=locking_date,
        )

        return api_editable_info
