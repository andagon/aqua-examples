from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiConfigElementEntrySave")


@attr.s(auto_attribs=True)
class ApiConfigElementEntrySave:
    """Represents single entry of a config element.

    Attributes:
        label (Union[Unset, None, str]): Label of the entry.
        content (Union[Unset, None, str]): Content of the entry.
    """

    label: Union[Unset, None, str] = UNSET
    content: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if label is not UNSET:
            field_dict["Label"] = label
        if content is not UNSET:
            field_dict["Content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("Label", UNSET)

        content = d.pop("Content", UNSET)

        api_config_element_entry_save = cls(
            label=label,
            content=content,
        )

        return api_config_element_entry_save
