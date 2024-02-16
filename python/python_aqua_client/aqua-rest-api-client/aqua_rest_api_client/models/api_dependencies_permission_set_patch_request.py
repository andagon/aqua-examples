from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission import ApiPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDependenciesPermissionSetPatchRequest")


@attr.s(auto_attribs=True)
class ApiDependenciesPermissionSetPatchRequest:
    """
    Attributes:
        operation_type (str):
        all_permissions (Union[Unset, None, List[ApiPermission]]): List of permissions to validate.
    """

    operation_type: str
    all_permissions: Union[Unset, None, List[ApiPermission]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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

        api_dependencies_permission_set_patch_request = cls(
            operation_type=operation_type,
            all_permissions=all_permissions,
        )

        api_dependencies_permission_set_patch_request.additional_properties = d
        return api_dependencies_permission_set_patch_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
