from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.aqua_client_type import AquaClientType
from ..models.permission import Permission
from ..models.permission_scope import PermissionScope
from ..models.permission_variant import PermissionVariant
from ..types import UNSET, Unset

T = TypeVar("T", bound="GenericPermissionInfo")


@attr.s(auto_attribs=True)
class GenericPermissionInfo:
    """
    Attributes:
        title (Union[Unset, None, str]):
        generic_permission_name (Union[Unset, None, str]):
        group (Union[Unset, None, str]):
        permission_all (Union[Unset, Permission]):
        permission_assigned (Union[Unset, None, Permission]):
        permission_owned (Union[Unset, None, Permission]):
        scope (Union[Unset, PermissionScope]):
        allowed_folder_level (Union[Unset, bool]):
        required_all (Union[Unset, None, List[str]]):
        required_any (Union[Unset, None, List[str]]):
        login_client_type (Union[Unset, None, AquaClientType]):
        license_only (Union[Unset, bool]):
        permision_variants (Union[Unset, None, List[PermissionVariant]]):
    """

    title: Union[Unset, None, str] = UNSET
    generic_permission_name: Union[Unset, None, str] = UNSET
    group: Union[Unset, None, str] = UNSET
    permission_all: Union[Unset, Permission] = UNSET
    permission_assigned: Union[Unset, None, Permission] = UNSET
    permission_owned: Union[Unset, None, Permission] = UNSET
    scope: Union[Unset, PermissionScope] = UNSET
    allowed_folder_level: Union[Unset, bool] = UNSET
    required_all: Union[Unset, None, List[str]] = UNSET
    required_any: Union[Unset, None, List[str]] = UNSET
    login_client_type: Union[Unset, None, AquaClientType] = UNSET
    license_only: Union[Unset, bool] = UNSET
    permision_variants: Union[Unset, None, List[PermissionVariant]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        generic_permission_name = self.generic_permission_name
        group = self.group
        permission_all: Union[Unset, int] = UNSET
        if not isinstance(self.permission_all, Unset):
            permission_all = self.permission_all.value

        permission_assigned: Union[Unset, None, int] = UNSET
        if not isinstance(self.permission_assigned, Unset):
            permission_assigned = self.permission_assigned.value if self.permission_assigned else None

        permission_owned: Union[Unset, None, int] = UNSET
        if not isinstance(self.permission_owned, Unset):
            permission_owned = self.permission_owned.value if self.permission_owned else None

        scope: Union[Unset, int] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        allowed_folder_level = self.allowed_folder_level
        required_all: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.required_all, Unset):
            if self.required_all is None:
                required_all = None
            else:
                required_all = self.required_all

        required_any: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.required_any, Unset):
            if self.required_any is None:
                required_any = None
            else:
                required_any = self.required_any

        login_client_type: Union[Unset, None, int] = UNSET
        if not isinstance(self.login_client_type, Unset):
            login_client_type = self.login_client_type.value if self.login_client_type else None

        license_only = self.license_only
        permision_variants: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.permision_variants, Unset):
            if self.permision_variants is None:
                permision_variants = None
            else:
                permision_variants = []
                for permision_variants_item_data in self.permision_variants:
                    permision_variants_item = permision_variants_item_data.value

                    permision_variants.append(permision_variants_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["Title"] = title
        if generic_permission_name is not UNSET:
            field_dict["GenericPermissionName"] = generic_permission_name
        if group is not UNSET:
            field_dict["Group"] = group
        if permission_all is not UNSET:
            field_dict["PermissionAll"] = permission_all
        if permission_assigned is not UNSET:
            field_dict["PermissionAssigned"] = permission_assigned
        if permission_owned is not UNSET:
            field_dict["PermissionOwned"] = permission_owned
        if scope is not UNSET:
            field_dict["Scope"] = scope
        if allowed_folder_level is not UNSET:
            field_dict["AllowedFolderLevel"] = allowed_folder_level
        if required_all is not UNSET:
            field_dict["RequiredAll"] = required_all
        if required_any is not UNSET:
            field_dict["RequiredAny"] = required_any
        if login_client_type is not UNSET:
            field_dict["LoginClientType"] = login_client_type
        if license_only is not UNSET:
            field_dict["LicenseOnly"] = license_only
        if permision_variants is not UNSET:
            field_dict["PermisionVariants"] = permision_variants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("Title", UNSET)

        generic_permission_name = d.pop("GenericPermissionName", UNSET)

        group = d.pop("Group", UNSET)

        _permission_all = d.pop("PermissionAll", UNSET)
        permission_all: Union[Unset, Permission]
        if isinstance(_permission_all, Unset):
            permission_all = UNSET
        else:
            permission_all = Permission(_permission_all)

        _permission_assigned = d.pop("PermissionAssigned", UNSET)
        permission_assigned: Union[Unset, None, Permission]
        if _permission_assigned is None:
            permission_assigned = None
        elif isinstance(_permission_assigned, Unset):
            permission_assigned = UNSET
        else:
            permission_assigned = Permission(_permission_assigned)

        _permission_owned = d.pop("PermissionOwned", UNSET)
        permission_owned: Union[Unset, None, Permission]
        if _permission_owned is None:
            permission_owned = None
        elif isinstance(_permission_owned, Unset):
            permission_owned = UNSET
        else:
            permission_owned = Permission(_permission_owned)

        _scope = d.pop("Scope", UNSET)
        scope: Union[Unset, PermissionScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = PermissionScope(_scope)

        allowed_folder_level = d.pop("AllowedFolderLevel", UNSET)

        required_all = cast(List[str], d.pop("RequiredAll", UNSET))

        required_any = cast(List[str], d.pop("RequiredAny", UNSET))

        _login_client_type = d.pop("LoginClientType", UNSET)
        login_client_type: Union[Unset, None, AquaClientType]
        if _login_client_type is None:
            login_client_type = None
        elif isinstance(_login_client_type, Unset):
            login_client_type = UNSET
        else:
            login_client_type = AquaClientType(_login_client_type)

        license_only = d.pop("LicenseOnly", UNSET)

        permision_variants = []
        _permision_variants = d.pop("PermisionVariants", UNSET)
        for permision_variants_item_data in _permision_variants or []:
            permision_variants_item = PermissionVariant(permision_variants_item_data)

            permision_variants.append(permision_variants_item)

        generic_permission_info = cls(
            title=title,
            generic_permission_name=generic_permission_name,
            group=group,
            permission_all=permission_all,
            permission_assigned=permission_assigned,
            permission_owned=permission_owned,
            scope=scope,
            allowed_folder_level=allowed_folder_level,
            required_all=required_all,
            required_any=required_any,
            login_client_type=login_client_type,
            license_only=license_only,
            permision_variants=permision_variants,
        )

        return generic_permission_info
