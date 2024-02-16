from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldValueDictionaryMultiChoice")


@attr.s(auto_attribs=True)
class ApiFieldValueDictionaryMultiChoice:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
        ids (Union[Unset, None, List[int]]): The list of field value ids.
        values (Union[Unset, None, List[str]]): The list of field value names.
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET
    ids: Union[Unset, None, List[int]] = UNSET
    values: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text
        ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.ids, Unset):
            if self.ids is None:
                ids = None
            else:
                ids = self.ids

        values: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.values, Unset):
            if self.values is None:
                values = None
            else:
                values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldValueType": field_value_type,
            }
        )
        if text is not UNSET:
            field_dict["Text"] = text
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if values is not UNSET:
            field_dict["Values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_value_type = d.pop("FieldValueType")

        text = d.pop("Text", UNSET)

        ids = cast(List[int], d.pop("Ids", UNSET))

        values = cast(List[str], d.pop("Values", UNSET))

        api_field_value_dictionary_multi_choice = cls(
            field_value_type=field_value_type,
            text=text,
            ids=ids,
            values=values,
        )

        api_field_value_dictionary_multi_choice.additional_properties = d
        return api_field_value_dictionary_multi_choice

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
