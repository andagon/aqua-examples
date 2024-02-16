from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldValue")


@attr.s(auto_attribs=True)
class ApiFieldValue:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "FieldValueType": field_value_type,
            }
        )
        if text is not UNSET:
            field_dict["Text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_value_type = d.pop("FieldValueType")

        text = d.pop("Text", UNSET)

        api_field_value = cls(
            field_value_type=field_value_type,
            text=text,
        )

        return api_field_value
