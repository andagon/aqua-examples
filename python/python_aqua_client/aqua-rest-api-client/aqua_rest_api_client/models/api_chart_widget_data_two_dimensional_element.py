from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value import ApiFieldValue


T = TypeVar("T", bound="ApiChartWidgetDataTwoDimensionalElement")


@attr.s(auto_attribs=True)
class ApiChartWidgetDataTwoDimensionalElement:
    """A data point for a two-dimensional chart

    Attributes:
        grouped_value (Union[Unset, None, ApiFieldValue]):
        x_axis_value (Union[Unset, None, ApiFieldValue]):
        number_of_elements (Union[Unset, int]): The number of elements which have these values
    """

    grouped_value: Union[Unset, None, "ApiFieldValue"] = UNSET
    x_axis_value: Union[Unset, None, "ApiFieldValue"] = UNSET
    number_of_elements: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        grouped_value: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.grouped_value, Unset):
            grouped_value = self.grouped_value.to_dict() if self.grouped_value else None

        x_axis_value: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.x_axis_value, Unset):
            x_axis_value = self.x_axis_value.to_dict() if self.x_axis_value else None

        number_of_elements = self.number_of_elements

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if grouped_value is not UNSET:
            field_dict["GroupedValue"] = grouped_value
        if x_axis_value is not UNSET:
            field_dict["XAxisValue"] = x_axis_value
        if number_of_elements is not UNSET:
            field_dict["NumberOfElements"] = number_of_elements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value import ApiFieldValue

        d = src_dict.copy()
        _grouped_value = d.pop("GroupedValue", UNSET)
        grouped_value: Union[Unset, None, ApiFieldValue]
        if _grouped_value is None:
            grouped_value = None
        elif isinstance(_grouped_value, Unset):
            grouped_value = UNSET
        else:
            grouped_value = ApiFieldValue.from_dict(_grouped_value)

        _x_axis_value = d.pop("XAxisValue", UNSET)
        x_axis_value: Union[Unset, None, ApiFieldValue]
        if _x_axis_value is None:
            x_axis_value = None
        elif isinstance(_x_axis_value, Unset):
            x_axis_value = UNSET
        else:
            x_axis_value = ApiFieldValue.from_dict(_x_axis_value)

        number_of_elements = d.pop("NumberOfElements", UNSET)

        api_chart_widget_data_two_dimensional_element = cls(
            grouped_value=grouped_value,
            x_axis_value=x_axis_value,
            number_of_elements=number_of_elements,
        )

        return api_chart_widget_data_two_dimensional_element
