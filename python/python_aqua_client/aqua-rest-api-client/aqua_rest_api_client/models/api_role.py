from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission import ApiPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRole")


@attr.s(auto_attribs=True)
class ApiRole:
    """
    Attributes:
        id (Union[Unset, int]): The id of the role.
        name (Union[Unset, None, str]): The name of the role.
        permissions (Union[Unset, None, List[ApiPermission]]): The list of permissions of the role.
        is_default (Union[Unset, bool]): True if role is a default role, which means it can't be changed.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    permissions: Union[Unset, None, List[ApiPermission]] = UNSET
    is_default: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = []
                for permissions_item_data in self.permissions:
                    permissions_item = permissions_item_data.value

                    permissions.append(permissions_item)

        is_default = self.is_default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions
        if is_default is not UNSET:
            field_dict["IsDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        permissions = []
        _permissions = d.pop("Permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = ApiPermission(permissions_item_data)

            permissions.append(permissions_item)

        is_default = d.pop("IsDefault", UNSET)

        api_role = cls(
            id=id,
            name=name,
            permissions=permissions,
            is_default=is_default,
        )

        api_role.additional_properties = d
        return api_role

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
