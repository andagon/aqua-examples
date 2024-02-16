from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportParameterValue")


@attr.s(auto_attribs=True)
class ApiReportParameterValue:
    """Represents a value of report parameter.

    Attributes:
        name (Union[Unset, None, str]): Internal name of the parameter (key)
        value (Union[Unset, Any]): Value of this parameter (depends on Type).
            When loading report options this value represents default value.
    """

    name: Union[Unset, None, str] = UNSET
    value: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        value = d.pop("Value", UNSET)

        api_report_parameter_value = cls(
            name=name,
            value=value,
        )

        return api_report_parameter_value
