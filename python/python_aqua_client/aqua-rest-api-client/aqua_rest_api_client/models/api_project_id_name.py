from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectIdName")


@attr.s(auto_attribs=True)
class ApiProjectIdName:
    """Holds the id and the name of a project.

    Attributes:
        id (Union[Unset, int]): The id of the project.
        name (Union[Unset, None, str]): The name of the project.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        api_project_id_name = cls(
            id=id,
            name=name,
        )

        return api_project_id_name
