from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_user_status import ApiUserStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserMinimalInfo")


@attr.s(auto_attribs=True)
class ApiUserMinimalInfo:
    """Represents the necessary minimal information about a user.

    Attributes:
        id (Union[Unset, int]): The id of the user.
        user_name (Union[Unset, None, str]): The username of the user.
        first_name (Union[Unset, None, str]): The first name of the user.
        surname (Union[Unset, None, str]): The surname / last name of the user.
        status (Union[Unset, ApiUserStatus]): Identifies the user status.
            This enum has the following values:
              - `Activated` The user is activated.
              - `Deactivated` The user is deactivated.
              - `LicenseDeactivated` The license is deactivated.
        any_active_license (Union[Unset, bool]): If set, indicates the the user has at least one active license
            assigned.
    """

    id: Union[Unset, int] = UNSET
    user_name: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    surname: Union[Unset, None, str] = UNSET
    status: Union[Unset, ApiUserStatus] = UNSET
    any_active_license: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_name = self.user_name
        first_name = self.first_name
        surname = self.surname
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        any_active_license = self.any_active_license

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if surname is not UNSET:
            field_dict["Surname"] = surname
        if status is not UNSET:
            field_dict["Status"] = status
        if any_active_license is not UNSET:
            field_dict["AnyActiveLicense"] = any_active_license

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        user_name = d.pop("UserName", UNSET)

        first_name = d.pop("FirstName", UNSET)

        surname = d.pop("Surname", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiUserStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiUserStatus(_status)

        any_active_license = d.pop("AnyActiveLicense", UNSET)

        api_user_minimal_info = cls(
            id=id,
            user_name=user_name,
            first_name=first_name,
            surname=surname,
            status=status,
            any_active_license=any_active_license,
        )

        return api_user_minimal_info
