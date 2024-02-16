from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectTemplateDictionaryEntryNew")


@attr.s(auto_attribs=True)
class ApiProjectTemplateDictionaryEntryNew:
    """Contains the meta-information of a new dictionary entry.

    Attributes:
        name (Union[Unset, None, str]): Name of the dictionary entry. This is the value visible in the UI.
        is_default (Union[Unset, bool]): Indicates whether this entry should be considered as default for this
            dictionary.
    """

    name: Union[Unset, None, str] = UNSET
    is_default: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_default = self.is_default

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if is_default is not UNSET:
            field_dict["IsDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        is_default = d.pop("IsDefault", UNSET)

        api_project_template_dictionary_entry_new = cls(
            name=name,
            is_default=is_default,
        )

        return api_project_template_dictionary_entry_new
