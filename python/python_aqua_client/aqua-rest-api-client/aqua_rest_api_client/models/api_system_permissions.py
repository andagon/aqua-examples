from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSystemPermissions")


@attr.s(auto_attribs=True)
class ApiSystemPermissions:
    """Represents permissions in a system.

    Attributes:
        can_create_project (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_manage_roles (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_manage_any_users (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_view_system_log (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_manage_any_integrations (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_view_any_agile_board (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
    """

    can_create_project: Union[Unset, ApiPermissionResult] = UNSET
    can_manage_roles: Union[Unset, ApiPermissionResult] = UNSET
    can_manage_any_users: Union[Unset, ApiPermissionResult] = UNSET
    can_view_system_log: Union[Unset, ApiPermissionResult] = UNSET
    can_manage_any_integrations: Union[Unset, ApiPermissionResult] = UNSET
    can_view_any_agile_board: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_create_project: Union[Unset, str] = UNSET
        if not isinstance(self.can_create_project, Unset):
            can_create_project = self.can_create_project.value

        can_manage_roles: Union[Unset, str] = UNSET
        if not isinstance(self.can_manage_roles, Unset):
            can_manage_roles = self.can_manage_roles.value

        can_manage_any_users: Union[Unset, str] = UNSET
        if not isinstance(self.can_manage_any_users, Unset):
            can_manage_any_users = self.can_manage_any_users.value

        can_view_system_log: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_system_log, Unset):
            can_view_system_log = self.can_view_system_log.value

        can_manage_any_integrations: Union[Unset, str] = UNSET
        if not isinstance(self.can_manage_any_integrations, Unset):
            can_manage_any_integrations = self.can_manage_any_integrations.value

        can_view_any_agile_board: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_any_agile_board, Unset):
            can_view_any_agile_board = self.can_view_any_agile_board.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_create_project is not UNSET:
            field_dict["CanCreateProject"] = can_create_project
        if can_manage_roles is not UNSET:
            field_dict["CanManageRoles"] = can_manage_roles
        if can_manage_any_users is not UNSET:
            field_dict["CanManageAnyUsers"] = can_manage_any_users
        if can_view_system_log is not UNSET:
            field_dict["CanViewSystemLog"] = can_view_system_log
        if can_manage_any_integrations is not UNSET:
            field_dict["CanManageAnyIntegrations"] = can_manage_any_integrations
        if can_view_any_agile_board is not UNSET:
            field_dict["CanViewAnyAgileBoard"] = can_view_any_agile_board

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _can_create_project = d.pop("CanCreateProject", UNSET)
        can_create_project: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create_project, Unset):
            can_create_project = UNSET
        else:
            can_create_project = ApiPermissionResult(_can_create_project)

        _can_manage_roles = d.pop("CanManageRoles", UNSET)
        can_manage_roles: Union[Unset, ApiPermissionResult]
        if isinstance(_can_manage_roles, Unset):
            can_manage_roles = UNSET
        else:
            can_manage_roles = ApiPermissionResult(_can_manage_roles)

        _can_manage_any_users = d.pop("CanManageAnyUsers", UNSET)
        can_manage_any_users: Union[Unset, ApiPermissionResult]
        if isinstance(_can_manage_any_users, Unset):
            can_manage_any_users = UNSET
        else:
            can_manage_any_users = ApiPermissionResult(_can_manage_any_users)

        _can_view_system_log = d.pop("CanViewSystemLog", UNSET)
        can_view_system_log: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_system_log, Unset):
            can_view_system_log = UNSET
        else:
            can_view_system_log = ApiPermissionResult(_can_view_system_log)

        _can_manage_any_integrations = d.pop("CanManageAnyIntegrations", UNSET)
        can_manage_any_integrations: Union[Unset, ApiPermissionResult]
        if isinstance(_can_manage_any_integrations, Unset):
            can_manage_any_integrations = UNSET
        else:
            can_manage_any_integrations = ApiPermissionResult(_can_manage_any_integrations)

        _can_view_any_agile_board = d.pop("CanViewAnyAgileBoard", UNSET)
        can_view_any_agile_board: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_any_agile_board, Unset):
            can_view_any_agile_board = UNSET
        else:
            can_view_any_agile_board = ApiPermissionResult(_can_view_any_agile_board)

        api_system_permissions = cls(
            can_create_project=can_create_project,
            can_manage_roles=can_manage_roles,
            can_manage_any_users=can_manage_any_users,
            can_view_system_log=can_view_system_log,
            can_manage_any_integrations=can_manage_any_integrations,
            can_view_any_agile_board=can_view_any_agile_board,
        )

        return api_system_permissions
