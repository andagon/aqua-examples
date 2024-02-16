from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission import ApiPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUpdateRole")


@attr.s(auto_attribs=True)
class ApiUpdateRole:
    """
    Attributes:
        new_name (Union[Unset, None, str]): The new name of the role.
        new_permissions (Union[Unset, None, List[ApiPermission]]): The list of new permission of this role.
    """

    new_name: Union[Unset, None, str] = UNSET
    new_permissions: Union[Unset, None, List[ApiPermission]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        new_name = self.new_name
        new_permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.new_permissions, Unset):
            if self.new_permissions is None:
                new_permissions = None
            else:
                new_permissions = []
                for new_permissions_item_data in self.new_permissions:
                    new_permissions_item = new_permissions_item_data.value

                    new_permissions.append(new_permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if new_name is not UNSET:
            field_dict["NewName"] = new_name
        if new_permissions is not UNSET:
            field_dict["NewPermissions"] = new_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_name = d.pop("NewName", UNSET)

        new_permissions = []
        _new_permissions = d.pop("NewPermissions", UNSET)
        for new_permissions_item_data in _new_permissions or []:
            new_permissions_item = ApiPermission(new_permissions_item_data)

            new_permissions.append(new_permissions_item)

        api_update_role = cls(
            new_name=new_name,
            new_permissions=new_permissions,
        )

        return api_update_role
