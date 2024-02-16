from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission import ApiPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRoleNew")


@attr.s(auto_attribs=True)
class ApiRoleNew:
    """
    Attributes:
        name (Union[Unset, None, str]): The name of the role.
        permissions (Union[Unset, None, List[ApiPermission]]): The list of permission of this role.
    """

    name: Union[Unset, None, str] = UNSET
    permissions: Union[Unset, None, List[ApiPermission]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        permissions = []
        _permissions = d.pop("Permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = ApiPermission(permissions_item_data)

            permissions.append(permissions_item)

        api_role_new = cls(
            name=name,
            permissions=permissions,
        )

        return api_role_new
