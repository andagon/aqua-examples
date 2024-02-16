from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_chart_widget_kpi_condition import ApiChartWidgetKPICondition
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiChartWidgetKPIEntry")


@attr.s(auto_attribs=True)
class ApiChartWidgetKPIEntry:
    """KPI for a chart widget

    Attributes:
        condition_type (Union[Unset, ApiChartWidgetKPICondition]): KPI condition type
            This enum has the following values:
              - `Equal`
              - `Greater`
              - `GreaterEqual`
              - `Less`
              - `LessEqual`
              - `NotEqual`
        selector (Union[Unset, None, str]): If not-null the value is used to select only some of the grouped values.
        threshold (Union[Unset, int]): Threshold (count) to be compared using the given ConditionType
        color (Union[Unset, None, str]): Color to be used (optional). HEX RGB string e.g. "ffaabc"
    """

    condition_type: Union[Unset, ApiChartWidgetKPICondition] = UNSET
    selector: Union[Unset, None, str] = UNSET
    threshold: Union[Unset, int] = UNSET
    color: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        condition_type: Union[Unset, str] = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type.value

        selector = self.selector
        threshold = self.threshold
        color = self.color

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if condition_type is not UNSET:
            field_dict["ConditionType"] = condition_type
        if selector is not UNSET:
            field_dict["Selector"] = selector
        if threshold is not UNSET:
            field_dict["Threshold"] = threshold
        if color is not UNSET:
            field_dict["Color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _condition_type = d.pop("ConditionType", UNSET)
        condition_type: Union[Unset, ApiChartWidgetKPICondition]
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = ApiChartWidgetKPICondition(_condition_type)

        selector = d.pop("Selector", UNSET)

        threshold = d.pop("Threshold", UNSET)

        color = d.pop("Color", UNSET)

        api_chart_widget_kpi_entry = cls(
            condition_type=condition_type,
            selector=selector,
            threshold=threshold,
            color=color,
        )

        return api_chart_widget_kpi_entry
