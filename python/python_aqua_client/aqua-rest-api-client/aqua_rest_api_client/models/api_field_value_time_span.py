from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.time_unit import TimeUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldValueTimeSpan")


@attr.s(auto_attribs=True)
class ApiFieldValueTimeSpan:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
        value (Union[Unset, float]): The value of the given time span. The base unit is
            given separately.
        unit (Union[Unset, TimeUnit]):
            This enum has the following values:
              - `Day`
              - `Hour`
              - `Minute`
              - `Month`
              - `Second`
              - `Week`
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET
    value: Union[Unset, float] = UNSET
    unit: Union[Unset, TimeUnit] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text
        value = self.value
        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldValueType": field_value_type,
            }
        )
        if text is not UNSET:
            field_dict["Text"] = text
        if value is not UNSET:
            field_dict["Value"] = value
        if unit is not UNSET:
            field_dict["Unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_value_type = d.pop("FieldValueType")

        text = d.pop("Text", UNSET)

        value = d.pop("Value", UNSET)

        _unit = d.pop("Unit", UNSET)
        unit: Union[Unset, TimeUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = TimeUnit(_unit)

        api_field_value_time_span = cls(
            field_value_type=field_value_type,
            text=text,
            value=value,
            unit=unit,
        )

        api_field_value_time_span.additional_properties = d
        return api_field_value_time_span

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
