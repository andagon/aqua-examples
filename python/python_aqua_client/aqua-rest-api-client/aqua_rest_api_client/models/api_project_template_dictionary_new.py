from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_template_dictionary_entry_new import ApiProjectTemplateDictionaryEntryNew


T = TypeVar("T", bound="ApiProjectTemplateDictionaryNew")


@attr.s(auto_attribs=True)
class ApiProjectTemplateDictionaryNew:
    """Represents a new dictionary to be created.

    Attributes:
        entries (Union[Unset, None, List['ApiProjectTemplateDictionaryEntryNew']]): Entries of this dictionary. The
            order matters.
            All items must be new.
        name (Union[Unset, None, str]): Name of the dictionary.
    """

    entries: Union[Unset, None, List["ApiProjectTemplateDictionaryEntryNew"]] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        entries: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            if self.entries is None:
                entries = None
            else:
                entries = []
                for entries_item_data in self.entries:
                    entries_item = entries_item_data.to_dict()

                    entries.append(entries_item)

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if entries is not UNSET:
            field_dict["Entries"] = entries
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_template_dictionary_entry_new import ApiProjectTemplateDictionaryEntryNew

        d = src_dict.copy()
        entries = []
        _entries = d.pop("Entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ApiProjectTemplateDictionaryEntryNew.from_dict(entries_item_data)

            entries.append(entries_item)

        name = d.pop("Name", UNSET)

        api_project_template_dictionary_new = cls(
            entries=entries,
            name=name,
        )

        return api_project_template_dictionary_new
