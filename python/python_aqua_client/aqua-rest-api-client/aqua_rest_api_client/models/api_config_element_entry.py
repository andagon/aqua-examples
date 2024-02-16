from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiConfigElementEntry")


@attr.s(auto_attribs=True)
class ApiConfigElementEntry:
    """
    Attributes:
        label (Union[Unset, None, str]): Label of the entry.
        content (Union[Unset, None, str]): Content of the entry.
        id (Union[Unset, int]): If of the entry. Can be used to e.g. delete the entry.
    """

    label: Union[Unset, None, str] = UNSET
    content: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        content = self.content
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["Label"] = label
        if content is not UNSET:
            field_dict["Content"] = content
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("Label", UNSET)

        content = d.pop("Content", UNSET)

        id = d.pop("Id", UNSET)

        api_config_element_entry = cls(
            label=label,
            content=content,
            id=id,
        )

        api_config_element_entry.additional_properties = d
        return api_config_element_entry

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
