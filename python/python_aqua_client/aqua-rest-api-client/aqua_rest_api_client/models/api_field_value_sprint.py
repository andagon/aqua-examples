from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldValueSprint")


@attr.s(auto_attribs=True)
class ApiFieldValueSprint:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
        id (Union[Unset, int]): The Id of the Sprint
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldValueType": field_value_type,
            }
        )
        if text is not UNSET:
            field_dict["Text"] = text
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_value_type = d.pop("FieldValueType")

        text = d.pop("Text", UNSET)

        id = d.pop("Id", UNSET)

        api_field_value_sprint = cls(
            field_value_type=field_value_type,
            text=text,
            id=id,
        )

        api_field_value_sprint.additional_properties = d
        return api_field_value_sprint

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
