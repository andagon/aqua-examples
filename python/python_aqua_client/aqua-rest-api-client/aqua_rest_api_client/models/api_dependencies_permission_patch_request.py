from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission import ApiPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDependenciesPermissionPatchRequest")


@attr.s(auto_attribs=True)
class ApiDependenciesPermissionPatchRequest:
    """Represent a request to validate permission dependencies.
    Actual subclasses are used, depending on OperationType.

        Attributes:
            operation_type (str):
            all_permissions (Union[Unset, None, List[ApiPermission]]): List of permissions to validate.
    """

    operation_type: str
    all_permissions: Union[Unset, None, List[ApiPermission]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        all_permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.all_permissions, Unset):
            if self.all_permissions is None:
                all_permissions = None
            else:
                all_permissions = []
                for all_permissions_item_data in self.all_permissions:
                    all_permissions_item = all_permissions_item_data.value

                    all_permissions.append(all_permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if all_permissions is not UNSET:
            field_dict["AllPermissions"] = all_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        all_permissions = []
        _all_permissions = d.pop("AllPermissions", UNSET)
        for all_permissions_item_data in _all_permissions or []:
            all_permissions_item = ApiPermission(all_permissions_item_data)

            all_permissions.append(all_permissions_item)

        api_dependencies_permission_patch_request = cls(
            operation_type=operation_type,
            all_permissions=all_permissions,
        )

        return api_dependencies_permission_patch_request
