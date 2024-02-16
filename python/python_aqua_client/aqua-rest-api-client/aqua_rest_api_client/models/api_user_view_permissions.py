from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserViewPermissions")


@attr.s(auto_attribs=True)
class ApiUserViewPermissions:
    """Represents permissions for a report.

    Attributes:
        can_edit (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_delete (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_publish (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_make_private (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
    """

    can_edit: Union[Unset, ApiPermissionResult] = UNSET
    can_delete: Union[Unset, ApiPermissionResult] = UNSET
    can_publish: Union[Unset, ApiPermissionResult] = UNSET
    can_make_private: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_edit: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit, Unset):
            can_edit = self.can_edit.value

        can_delete: Union[Unset, str] = UNSET
        if not isinstance(self.can_delete, Unset):
            can_delete = self.can_delete.value

        can_publish: Union[Unset, str] = UNSET
        if not isinstance(self.can_publish, Unset):
            can_publish = self.can_publish.value

        can_make_private: Union[Unset, str] = UNSET
        if not isinstance(self.can_make_private, Unset):
            can_make_private = self.can_make_private.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_edit is not UNSET:
            field_dict["CanEdit"] = can_edit
        if can_delete is not UNSET:
            field_dict["CanDelete"] = can_delete
        if can_publish is not UNSET:
            field_dict["CanPublish"] = can_publish
        if can_make_private is not UNSET:
            field_dict["CanMakePrivate"] = can_make_private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _can_edit = d.pop("CanEdit", UNSET)
        can_edit: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit, Unset):
            can_edit = UNSET
        else:
            can_edit = ApiPermissionResult(_can_edit)

        _can_delete = d.pop("CanDelete", UNSET)
        can_delete: Union[Unset, ApiPermissionResult]
        if isinstance(_can_delete, Unset):
            can_delete = UNSET
        else:
            can_delete = ApiPermissionResult(_can_delete)

        _can_publish = d.pop("CanPublish", UNSET)
        can_publish: Union[Unset, ApiPermissionResult]
        if isinstance(_can_publish, Unset):
            can_publish = UNSET
        else:
            can_publish = ApiPermissionResult(_can_publish)

        _can_make_private = d.pop("CanMakePrivate", UNSET)
        can_make_private: Union[Unset, ApiPermissionResult]
        if isinstance(_can_make_private, Unset):
            can_make_private = UNSET
        else:
            can_make_private = ApiPermissionResult(_can_make_private)

        api_user_view_permissions = cls(
            can_edit=can_edit,
            can_delete=can_delete,
            can_publish=can_publish,
            can_make_private=can_make_private,
        )

        return api_user_view_permissions
