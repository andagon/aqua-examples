from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_template_dictionary_entry import ApiProjectTemplateDictionaryEntry


T = TypeVar("T", bound="ApiProjectTemplateDictionary")


@attr.s(auto_attribs=True)
class ApiProjectTemplateDictionary:
    """Represents a single dictionary (i.e. entity that has a name and holds list of values) defined in the project
    template.
    Please note that dictionary fields reference either their own ("local") dictionaries, or use dictionaries
    referenced by many fields at the same time ("shared").

        Attributes:
            entries (Union[Unset, None, List['ApiProjectTemplateDictionaryEntry']]): Entries of this dictionary. The order
                matters.
            id (Union[Unset, int]): Internal Id of the dictionary.
            name (Union[Unset, None, str]): Name of the dictionary.
            consistency_key (Union[Unset, None, str]): Consistency key. Needs to be provided when saving.
                Prevents from concurrent modifications.
    """

    entries: Union[Unset, None, List["ApiProjectTemplateDictionaryEntry"]] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    consistency_key: Union[Unset, None, str] = UNSET

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

        id = self.id
        name = self.name
        consistency_key = self.consistency_key

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if entries is not UNSET:
            field_dict["Entries"] = entries
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if consistency_key is not UNSET:
            field_dict["ConsistencyKey"] = consistency_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_template_dictionary_entry import ApiProjectTemplateDictionaryEntry

        d = src_dict.copy()
        entries = []
        _entries = d.pop("Entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ApiProjectTemplateDictionaryEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        consistency_key = d.pop("ConsistencyKey", UNSET)

        api_project_template_dictionary = cls(
            entries=entries,
            id=id,
            name=name,
            consistency_key=consistency_key,
        )

        return api_project_template_dictionary
