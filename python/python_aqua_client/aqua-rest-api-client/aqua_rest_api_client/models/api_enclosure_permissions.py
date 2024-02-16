from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEnclosurePermissions")


@attr.s(auto_attribs=True)
class ApiEnclosurePermissions:
    """Represents permissions of a Enclosure.

    Attributes:
        can_delete (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_edit (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
    """

    can_delete: Union[Unset, ApiPermissionResult] = UNSET
    can_edit: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_delete: Union[Unset, str] = UNSET
        if not isinstance(self.can_delete, Unset):
            can_delete = self.can_delete.value

        can_edit: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit, Unset):
            can_edit = self.can_edit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_delete is not UNSET:
            field_dict["CanDelete"] = can_delete
        if can_edit is not UNSET:
            field_dict["CanEdit"] = can_edit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _can_delete = d.pop("CanDelete", UNSET)
        can_delete: Union[Unset, ApiPermissionResult]
        if isinstance(_can_delete, Unset):
            can_delete = UNSET
        else:
            can_delete = ApiPermissionResult(_can_delete)

        _can_edit = d.pop("CanEdit", UNSET)
        can_edit: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit, Unset):
            can_edit = UNSET
        else:
            can_edit = ApiPermissionResult(_can_edit)

        api_enclosure_permissions = cls(
            can_delete=can_delete,
            can_edit=can_edit,
        )

        return api_enclosure_permissions
