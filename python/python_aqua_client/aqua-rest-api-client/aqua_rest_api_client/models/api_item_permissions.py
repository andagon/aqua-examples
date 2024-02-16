from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_permissions_can_create_dependent_item import ApiItemPermissionsCanCreateDependentItem


T = TypeVar("T", bound="ApiItemPermissions")


@attr.s(auto_attribs=True)
class ApiItemPermissions:
    """Represents permissions of an item. Intended to be subclassed
    by classes with more fine-grained permission set for given context.

        Attributes:
            can_create_dependency (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_delete_dependency (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_create_dependent_item (Union[Unset, None, ApiItemPermissionsCanCreateDependentItem]): Indicates whether the
                user is able to create a new dependent item of
                a certain type in the same folder as the current item is located in.
            can_edit_fields (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_edit_status (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_delete (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_view_attachments (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_add_attachments (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_delete_attachments (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_create_edit_mind_map (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_manage_project_custom_defaults (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
                check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
    """

    can_create_dependency: Union[Unset, ApiPermissionResult] = UNSET
    can_delete_dependency: Union[Unset, ApiPermissionResult] = UNSET
    can_create_dependent_item: Union[Unset, None, "ApiItemPermissionsCanCreateDependentItem"] = UNSET
    can_edit_fields: Union[Unset, ApiPermissionResult] = UNSET
    can_edit_status: Union[Unset, ApiPermissionResult] = UNSET
    can_delete: Union[Unset, ApiPermissionResult] = UNSET
    can_view_attachments: Union[Unset, ApiPermissionResult] = UNSET
    can_add_attachments: Union[Unset, ApiPermissionResult] = UNSET
    can_delete_attachments: Union[Unset, ApiPermissionResult] = UNSET
    can_create_edit_mind_map: Union[Unset, ApiPermissionResult] = UNSET
    can_manage_project_custom_defaults: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_create_dependency: Union[Unset, str] = UNSET
        if not isinstance(self.can_create_dependency, Unset):
            can_create_dependency = self.can_create_dependency.value

        can_delete_dependency: Union[Unset, str] = UNSET
        if not isinstance(self.can_delete_dependency, Unset):
            can_delete_dependency = self.can_delete_dependency.value

        can_create_dependent_item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.can_create_dependent_item, Unset):
            can_create_dependent_item = (
                self.can_create_dependent_item.to_dict() if self.can_create_dependent_item else None
            )

        can_edit_fields: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit_fields, Unset):
            can_edit_fields = self.can_edit_fields.value

        can_edit_status: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit_status, Unset):
            can_edit_status = self.can_edit_status.value

        can_delete: Union[Unset, str] = UNSET
        if not isinstance(self.can_delete, Unset):
            can_delete = self.can_delete.value

        can_view_attachments: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_attachments, Unset):
            can_view_attachments = self.can_view_attachments.value

        can_add_attachments: Union[Unset, str] = UNSET
        if not isinstance(self.can_add_attachments, Unset):
            can_add_attachments = self.can_add_attachments.value

        can_delete_attachments: Union[Unset, str] = UNSET
        if not isinstance(self.can_delete_attachments, Unset):
            can_delete_attachments = self.can_delete_attachments.value

        can_create_edit_mind_map: Union[Unset, str] = UNSET
        if not isinstance(self.can_create_edit_mind_map, Unset):
            can_create_edit_mind_map = self.can_create_edit_mind_map.value

        can_manage_project_custom_defaults: Union[Unset, str] = UNSET
        if not isinstance(self.can_manage_project_custom_defaults, Unset):
            can_manage_project_custom_defaults = self.can_manage_project_custom_defaults.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_create_dependency is not UNSET:
            field_dict["CanCreateDependency"] = can_create_dependency
        if can_delete_dependency is not UNSET:
            field_dict["CanDeleteDependency"] = can_delete_dependency
        if can_create_dependent_item is not UNSET:
            field_dict["CanCreateDependentItem"] = can_create_dependent_item
        if can_edit_fields is not UNSET:
            field_dict["CanEditFields"] = can_edit_fields
        if can_edit_status is not UNSET:
            field_dict["CanEditStatus"] = can_edit_status
        if can_delete is not UNSET:
            field_dict["CanDelete"] = can_delete
        if can_view_attachments is not UNSET:
            field_dict["CanViewAttachments"] = can_view_attachments
        if can_add_attachments is not UNSET:
            field_dict["CanAddAttachments"] = can_add_attachments
        if can_delete_attachments is not UNSET:
            field_dict["CanDeleteAttachments"] = can_delete_attachments
        if can_create_edit_mind_map is not UNSET:
            field_dict["CanCreateEditMindMap"] = can_create_edit_mind_map
        if can_manage_project_custom_defaults is not UNSET:
            field_dict["CanManageProjectCustomDefaults"] = can_manage_project_custom_defaults

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_permissions_can_create_dependent_item import ApiItemPermissionsCanCreateDependentItem

        d = src_dict.copy()
        _can_create_dependency = d.pop("CanCreateDependency", UNSET)
        can_create_dependency: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create_dependency, Unset):
            can_create_dependency = UNSET
        else:
            can_create_dependency = ApiPermissionResult(_can_create_dependency)

        _can_delete_dependency = d.pop("CanDeleteDependency", UNSET)
        can_delete_dependency: Union[Unset, ApiPermissionResult]
        if isinstance(_can_delete_dependency, Unset):
            can_delete_dependency = UNSET
        else:
            can_delete_dependency = ApiPermissionResult(_can_delete_dependency)

        _can_create_dependent_item = d.pop("CanCreateDependentItem", UNSET)
        can_create_dependent_item: Union[Unset, None, ApiItemPermissionsCanCreateDependentItem]
        if _can_create_dependent_item is None:
            can_create_dependent_item = None
        elif isinstance(_can_create_dependent_item, Unset):
            can_create_dependent_item = UNSET
        else:
            can_create_dependent_item = ApiItemPermissionsCanCreateDependentItem.from_dict(_can_create_dependent_item)

        _can_edit_fields = d.pop("CanEditFields", UNSET)
        can_edit_fields: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit_fields, Unset):
            can_edit_fields = UNSET
        else:
            can_edit_fields = ApiPermissionResult(_can_edit_fields)

        _can_edit_status = d.pop("CanEditStatus", UNSET)
        can_edit_status: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit_status, Unset):
            can_edit_status = UNSET
        else:
            can_edit_status = ApiPermissionResult(_can_edit_status)

        _can_delete = d.pop("CanDelete", UNSET)
        can_delete: Union[Unset, ApiPermissionResult]
        if isinstance(_can_delete, Unset):
            can_delete = UNSET
        else:
            can_delete = ApiPermissionResult(_can_delete)

        _can_view_attachments = d.pop("CanViewAttachments", UNSET)
        can_view_attachments: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_attachments, Unset):
            can_view_attachments = UNSET
        else:
            can_view_attachments = ApiPermissionResult(_can_view_attachments)

        _can_add_attachments = d.pop("CanAddAttachments", UNSET)
        can_add_attachments: Union[Unset, ApiPermissionResult]
        if isinstance(_can_add_attachments, Unset):
            can_add_attachments = UNSET
        else:
            can_add_attachments = ApiPermissionResult(_can_add_attachments)

        _can_delete_attachments = d.pop("CanDeleteAttachments", UNSET)
        can_delete_attachments: Union[Unset, ApiPermissionResult]
        if isinstance(_can_delete_attachments, Unset):
            can_delete_attachments = UNSET
        else:
            can_delete_attachments = ApiPermissionResult(_can_delete_attachments)

        _can_create_edit_mind_map = d.pop("CanCreateEditMindMap", UNSET)
        can_create_edit_mind_map: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create_edit_mind_map, Unset):
            can_create_edit_mind_map = UNSET
        else:
            can_create_edit_mind_map = ApiPermissionResult(_can_create_edit_mind_map)

        _can_manage_project_custom_defaults = d.pop("CanManageProjectCustomDefaults", UNSET)
        can_manage_project_custom_defaults: Union[Unset, ApiPermissionResult]
        if isinstance(_can_manage_project_custom_defaults, Unset):
            can_manage_project_custom_defaults = UNSET
        else:
            can_manage_project_custom_defaults = ApiPermissionResult(_can_manage_project_custom_defaults)

        api_item_permissions = cls(
            can_create_dependency=can_create_dependency,
            can_delete_dependency=can_delete_dependency,
            can_create_dependent_item=can_create_dependent_item,
            can_edit_fields=can_edit_fields,
            can_edit_status=can_edit_status,
            can_delete=can_delete,
            can_view_attachments=can_view_attachments,
            can_add_attachments=can_add_attachments,
            can_delete_attachments=can_delete_attachments,
            can_create_edit_mind_map=can_create_edit_mind_map,
            can_manage_project_custom_defaults=can_manage_project_custom_defaults,
        )

        return api_item_permissions
