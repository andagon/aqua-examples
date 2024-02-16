from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportPermissions")


@attr.s(auto_attribs=True)
class ApiReportPermissions:
    """Represents permissions for a report.

    Attributes:
        can_generate (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_edit_properties (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_edit_layout (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_delete (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_export (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
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

    can_generate: Union[Unset, ApiPermissionResult] = UNSET
    can_edit_properties: Union[Unset, ApiPermissionResult] = UNSET
    can_edit_layout: Union[Unset, ApiPermissionResult] = UNSET
    can_delete: Union[Unset, ApiPermissionResult] = UNSET
    can_export: Union[Unset, ApiPermissionResult] = UNSET
    can_publish: Union[Unset, ApiPermissionResult] = UNSET
    can_make_private: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_generate: Union[Unset, str] = UNSET
        if not isinstance(self.can_generate, Unset):
            can_generate = self.can_generate.value

        can_edit_properties: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit_properties, Unset):
            can_edit_properties = self.can_edit_properties.value

        can_edit_layout: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit_layout, Unset):
            can_edit_layout = self.can_edit_layout.value

        can_delete: Union[Unset, str] = UNSET
        if not isinstance(self.can_delete, Unset):
            can_delete = self.can_delete.value

        can_export: Union[Unset, str] = UNSET
        if not isinstance(self.can_export, Unset):
            can_export = self.can_export.value

        can_publish: Union[Unset, str] = UNSET
        if not isinstance(self.can_publish, Unset):
            can_publish = self.can_publish.value

        can_make_private: Union[Unset, str] = UNSET
        if not isinstance(self.can_make_private, Unset):
            can_make_private = self.can_make_private.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_generate is not UNSET:
            field_dict["CanGenerate"] = can_generate
        if can_edit_properties is not UNSET:
            field_dict["CanEditProperties"] = can_edit_properties
        if can_edit_layout is not UNSET:
            field_dict["CanEditLayout"] = can_edit_layout
        if can_delete is not UNSET:
            field_dict["CanDelete"] = can_delete
        if can_export is not UNSET:
            field_dict["CanExport"] = can_export
        if can_publish is not UNSET:
            field_dict["CanPublish"] = can_publish
        if can_make_private is not UNSET:
            field_dict["CanMakePrivate"] = can_make_private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _can_generate = d.pop("CanGenerate", UNSET)
        can_generate: Union[Unset, ApiPermissionResult]
        if isinstance(_can_generate, Unset):
            can_generate = UNSET
        else:
            can_generate = ApiPermissionResult(_can_generate)

        _can_edit_properties = d.pop("CanEditProperties", UNSET)
        can_edit_properties: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit_properties, Unset):
            can_edit_properties = UNSET
        else:
            can_edit_properties = ApiPermissionResult(_can_edit_properties)

        _can_edit_layout = d.pop("CanEditLayout", UNSET)
        can_edit_layout: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit_layout, Unset):
            can_edit_layout = UNSET
        else:
            can_edit_layout = ApiPermissionResult(_can_edit_layout)

        _can_delete = d.pop("CanDelete", UNSET)
        can_delete: Union[Unset, ApiPermissionResult]
        if isinstance(_can_delete, Unset):
            can_delete = UNSET
        else:
            can_delete = ApiPermissionResult(_can_delete)

        _can_export = d.pop("CanExport", UNSET)
        can_export: Union[Unset, ApiPermissionResult]
        if isinstance(_can_export, Unset):
            can_export = UNSET
        else:
            can_export = ApiPermissionResult(_can_export)

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

        api_report_permissions = cls(
            can_generate=can_generate,
            can_edit_properties=can_edit_properties,
            can_edit_layout=can_edit_layout,
            can_delete=can_delete,
            can_export=can_export,
            can_publish=can_publish,
            can_make_private=can_make_private,
        )

        return api_report_permissions
