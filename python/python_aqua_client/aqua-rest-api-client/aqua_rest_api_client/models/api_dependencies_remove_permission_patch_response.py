from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission import ApiPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDependenciesRemovePermissionPatchResponse")


@attr.s(auto_attribs=True)
class ApiDependenciesRemovePermissionPatchResponse:
    """
    Attributes:
        operation_type (str):
        permissions_to_remove (Union[Unset, None, List[ApiPermission]]): List of permission where depdencie is not
            resolved, after the remove operation.
    """

    operation_type: str
    permissions_to_remove: Union[Unset, None, List[ApiPermission]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        permissions_to_remove: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.permissions_to_remove, Unset):
            if self.permissions_to_remove is None:
                permissions_to_remove = None
            else:
                permissions_to_remove = []
                for permissions_to_remove_item_data in self.permissions_to_remove:
                    permissions_to_remove_item = permissions_to_remove_item_data.value

                    permissions_to_remove.append(permissions_to_remove_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if permissions_to_remove is not UNSET:
            field_dict["PermissionsToRemove"] = permissions_to_remove

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        permissions_to_remove = []
        _permissions_to_remove = d.pop("PermissionsToRemove", UNSET)
        for permissions_to_remove_item_data in _permissions_to_remove or []:
            permissions_to_remove_item = ApiPermission(permissions_to_remove_item_data)

            permissions_to_remove.append(permissions_to_remove_item)

        api_dependencies_remove_permission_patch_response = cls(
            operation_type=operation_type,
            permissions_to_remove=permissions_to_remove,
        )

        api_dependencies_remove_permission_patch_response.additional_properties = d
        return api_dependencies_remove_permission_patch_response

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
