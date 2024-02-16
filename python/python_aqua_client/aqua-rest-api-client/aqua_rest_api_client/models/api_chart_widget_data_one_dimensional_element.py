from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value import ApiFieldValue


T = TypeVar("T", bound="ApiChartWidgetDataOneDimensionalElement")


@attr.s(auto_attribs=True)
class ApiChartWidgetDataOneDimensionalElement:
    """A data point for a one-dimensional chart

    Attributes:
        grouped_value (Union[Unset, None, ApiFieldValue]):
        number_of_elements (Union[Unset, int]): The number of elements which have this value
    """

    grouped_value: Union[Unset, None, "ApiFieldValue"] = UNSET
    number_of_elements: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        grouped_value: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.grouped_value, Unset):
            grouped_value = self.grouped_value.to_dict() if self.grouped_value else None

        number_of_elements = self.number_of_elements

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if grouped_value is not UNSET:
            field_dict["GroupedValue"] = grouped_value
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

        number_of_elements = d.pop("NumberOfElements", UNSET)

        api_chart_widget_data_one_dimensional_element = cls(
            grouped_value=grouped_value,
            number_of_elements=number_of_elements,
        )

        return api_chart_widget_data_one_dimensional_element
