from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectIdNameHasSubfolders")


@attr.s(auto_attribs=True)
class ApiProjectIdNameHasSubfolders:
    """
    Attributes:
        id (Union[Unset, int]): The id of the project.
        name (Union[Unset, None, str]): The name of the project.
        has_subfolders (Union[Unset, bool]): Indicates whether this project has any subfolders.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    has_subfolders: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        has_subfolders = self.has_subfolders

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if has_subfolders is not UNSET:
            field_dict["HasSubfolders"] = has_subfolders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        has_subfolders = d.pop("HasSubfolders", UNSET)

        api_project_id_name_has_subfolders = cls(
            id=id,
            name=name,
            has_subfolders=has_subfolders,
        )

        api_project_id_name_has_subfolders.additional_properties = d
        return api_project_id_name_has_subfolders

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
