from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_template_dictionary_entry import ApiProjectTemplateDictionaryEntry
    from ..models.api_project_template_dictionary_usage import ApiProjectTemplateDictionaryUsage


T = TypeVar("T", bound="ApiProjectTemplateDictionaryWithUsage")


@attr.s(auto_attribs=True)
class ApiProjectTemplateDictionaryWithUsage:
    """
    Attributes:
        entries (Union[Unset, None, List['ApiProjectTemplateDictionaryEntry']]): Entries of this dictionary. The order
            matters.
        id (Union[Unset, int]): Internal Id of the dictionary.
        name (Union[Unset, None, str]): Name of the dictionary.
        consistency_key (Union[Unset, None, str]): Consistency key. Needs to be provided when saving.
            Prevents from concurrent modifications.
        usage (Union[Unset, None, List['ApiProjectTemplateDictionaryUsage']]): Contains list of places (custom fields)
            where the dictionary is referenced in current project template.
    """

    entries: Union[Unset, None, List["ApiProjectTemplateDictionaryEntry"]] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    consistency_key: Union[Unset, None, str] = UNSET
    usage: Union[Unset, None, List["ApiProjectTemplateDictionaryUsage"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        usage: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.usage, Unset):
            if self.usage is None:
                usage = None
            else:
                usage = []
                for usage_item_data in self.usage:
                    usage_item = usage_item_data.to_dict()

                    usage.append(usage_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["Entries"] = entries
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if consistency_key is not UNSET:
            field_dict["ConsistencyKey"] = consistency_key
        if usage is not UNSET:
            field_dict["Usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_template_dictionary_entry import ApiProjectTemplateDictionaryEntry
        from ..models.api_project_template_dictionary_usage import ApiProjectTemplateDictionaryUsage

        d = src_dict.copy()
        entries = []
        _entries = d.pop("Entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ApiProjectTemplateDictionaryEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        consistency_key = d.pop("ConsistencyKey", UNSET)

        usage = []
        _usage = d.pop("Usage", UNSET)
        for usage_item_data in _usage or []:
            usage_item = ApiProjectTemplateDictionaryUsage.from_dict(usage_item_data)

            usage.append(usage_item)

        api_project_template_dictionary_with_usage = cls(
            entries=entries,
            id=id,
            name=name,
            consistency_key=consistency_key,
            usage=usage,
        )

        api_project_template_dictionary_with_usage.additional_properties = d
        return api_project_template_dictionary_with_usage

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
