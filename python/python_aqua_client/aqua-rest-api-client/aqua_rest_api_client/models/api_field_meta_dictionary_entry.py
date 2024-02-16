from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldMetaDictionaryEntry")


@attr.s(auto_attribs=True)
class ApiFieldMetaDictionaryEntry:
    """Contains the meta-information of a dictionary entry.

    Attributes:
        id (Union[Unset, int]): Id of the entry. This value is stored on actual item that references the dictionary
            entry.
            (entries can be safely renamed, as their ids do not change).
        name (Union[Unset, None, str]): Name of the dictionary entry. This is the value visible in the UI.
        is_default (Union[Unset, bool]): Indicates whether this entry should be cosnidered as default for this
            dictionary.
        is_deleted (Union[Unset, bool]): Indicates whether this entry was deleted.
            Deleted entries are not available for selection, but still can seen on old items (edited before teh entry has
            been deleted).
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    is_deleted: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        is_default = self.is_default
        is_deleted = self.is_deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if is_default is not UNSET:
            field_dict["IsDefault"] = is_default
        if is_deleted is not UNSET:
            field_dict["IsDeleted"] = is_deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        is_default = d.pop("IsDefault", UNSET)

        is_deleted = d.pop("IsDeleted", UNSET)

        api_field_meta_dictionary_entry = cls(
            id=id,
            name=name,
            is_default=is_default,
            is_deleted=is_deleted,
        )

        return api_field_meta_dictionary_entry
