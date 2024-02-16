from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_report_parameter_type import ApiReportParameterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportParameter")


@attr.s(auto_attribs=True)
class ApiReportParameter:
    """
    Attributes:
        name (Union[Unset, None, str]): Internal name of the parameter (key)
        value (Union[Unset, Any]): Value of this parameter (depends on Type).
            When loading report options this value represents default value.
        description (Union[Unset, None, str]): Parameter description
        type (Union[Unset, ApiReportParameterType]): Report parameter types
            This enum has the following values:
              - `Boolean` Boolean
              - `Date` Date
              - `Guid` Guid
              - `Number16` Short number (16 bit)
              - `Number32` Number (32 bit)
              - `Number64` Long number (64 bit)
              - `NumberDecimal` Decimal number
              - `NumberDouble` Double floating number
              - `NumberFloat` Floating number
              - `String` String
        visible (Union[Unset, bool]): Indicates whether parameter should is visible for end users
        multi_value (Union[Unset, bool]): Indicates whether parameter is multi-value i.e. the value is an array of
            values instead of single one
    """

    name: Union[Unset, None, str] = UNSET
    value: Union[Unset, Any] = UNSET
    description: Union[Unset, None, str] = UNSET
    type: Union[Unset, ApiReportParameterType] = UNSET
    visible: Union[Unset, bool] = UNSET
    multi_value: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        value = self.value
        description = self.description
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        visible = self.visible
        multi_value = self.multi_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if value is not UNSET:
            field_dict["Value"] = value
        if description is not UNSET:
            field_dict["Description"] = description
        if type is not UNSET:
            field_dict["Type"] = type
        if visible is not UNSET:
            field_dict["Visible"] = visible
        if multi_value is not UNSET:
            field_dict["MultiValue"] = multi_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        value = d.pop("Value", UNSET)

        description = d.pop("Description", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiReportParameterType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiReportParameterType(_type)

        visible = d.pop("Visible", UNSET)

        multi_value = d.pop("MultiValue", UNSET)

        api_report_parameter = cls(
            name=name,
            value=value,
            description=description,
            type=type,
            visible=visible,
            multi_value=multi_value,
        )

        api_report_parameter.additional_properties = d
        return api_report_parameter

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
