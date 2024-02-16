from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRoleNewResponse")


@attr.s(auto_attribs=True)
class ApiRoleNewResponse:
    """Contains information about created role.

    Attributes:
        role_id (Union[Unset, int]): The id of the role.
    """

    role_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        role_id = self.role_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if role_id is not UNSET:
            field_dict["RoleId"] = role_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_id = d.pop("RoleId", UNSET)

        api_role_new_response = cls(
            role_id=role_id,
        )

        return api_role_new_response
