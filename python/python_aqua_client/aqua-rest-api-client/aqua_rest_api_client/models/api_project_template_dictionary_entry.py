from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectTemplateDictionaryEntry")


@attr.s(auto_attribs=True)
class ApiProjectTemplateDictionaryEntry:
    """
    Attributes:
        name (Union[Unset, None, str]): Name of the dictionary entry. This is the value visible in the UI.
        is_default (Union[Unset, bool]): Indicates whether this entry should be considered as default for this
            dictionary.
        id (Union[Unset, int]): Id of the entry. This value is stored on actual item that references the dictionary
            entry.
            (Entries can be safely renamed, as their ids do not change).
    """

    name: Union[Unset, None, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_default = self.is_default
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if is_default is not UNSET:
            field_dict["IsDefault"] = is_default
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        is_default = d.pop("IsDefault", UNSET)

        id = d.pop("Id", UNSET)

        api_project_template_dictionary_entry = cls(
            name=name,
            is_default=is_default,
            id=id,
        )

        api_project_template_dictionary_entry.additional_properties = d
        return api_project_template_dictionary_entry

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
