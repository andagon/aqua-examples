from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_chart_type import ApiChartType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_chart_widget_data_specification import ApiChartWidgetDataSpecification
    from ..models.api_chart_widget_kpi_entry import ApiChartWidgetKPIEntry


T = TypeVar("T", bound="ApiChartWidgetModel")


@attr.s(auto_attribs=True)
class ApiChartWidgetModel:
    """
    Attributes:
        widget_type (str):
        chart_type (Union[Unset, ApiChartType]):
            This enum has the following values:
              - `Bar`
              - `BarSideBySide`
              - `BarStacked`
              - `Pie`
              - `Table`
        filter_display (Union[Unset, None, str]): Textual representation of the filter string (included in
            ChartWidgetDataSpecification)
        show_legend (Union[Unset, bool]): If true the chart should show a legend.
        show_totals (Union[Unset, bool]): If true the chart should show totals.
        show_percentages (Union[Unset, bool]): If true the chart should show percentages.
        kpi (Union[Unset, None, List['ApiChartWidgetKPIEntry']]): KPI specifications (optional)
        chart_widget_data_specification (Union[Unset, None, ApiChartWidgetDataSpecification]): Data specification for
            the chart widget
    """

    widget_type: str
    chart_type: Union[Unset, ApiChartType] = UNSET
    filter_display: Union[Unset, None, str] = UNSET
    show_legend: Union[Unset, bool] = UNSET
    show_totals: Union[Unset, bool] = UNSET
    show_percentages: Union[Unset, bool] = UNSET
    kpi: Union[Unset, None, List["ApiChartWidgetKPIEntry"]] = UNSET
    chart_widget_data_specification: Union[Unset, None, "ApiChartWidgetDataSpecification"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        widget_type = self.widget_type
        chart_type: Union[Unset, str] = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value

        filter_display = self.filter_display
        show_legend = self.show_legend
        show_totals = self.show_totals
        show_percentages = self.show_percentages
        kpi: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.kpi, Unset):
            if self.kpi is None:
                kpi = None
            else:
                kpi = []
                for kpi_item_data in self.kpi:
                    kpi_item = kpi_item_data.to_dict()

                    kpi.append(kpi_item)

        chart_widget_data_specification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.chart_widget_data_specification, Unset):
            chart_widget_data_specification = (
                self.chart_widget_data_specification.to_dict() if self.chart_widget_data_specification else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "WidgetType": widget_type,
            }
        )
        if chart_type is not UNSET:
            field_dict["ChartType"] = chart_type
        if filter_display is not UNSET:
            field_dict["FilterDisplay"] = filter_display
        if show_legend is not UNSET:
            field_dict["ShowLegend"] = show_legend
        if show_totals is not UNSET:
            field_dict["ShowTotals"] = show_totals
        if show_percentages is not UNSET:
            field_dict["ShowPercentages"] = show_percentages
        if kpi is not UNSET:
            field_dict["KPI"] = kpi
        if chart_widget_data_specification is not UNSET:
            field_dict["ChartWidgetDataSpecification"] = chart_widget_data_specification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_chart_widget_data_specification import ApiChartWidgetDataSpecification
        from ..models.api_chart_widget_kpi_entry import ApiChartWidgetKPIEntry

        d = src_dict.copy()
        widget_type = d.pop("WidgetType")

        _chart_type = d.pop("ChartType", UNSET)
        chart_type: Union[Unset, ApiChartType]
        if isinstance(_chart_type, Unset):
            chart_type = UNSET
        else:
            chart_type = ApiChartType(_chart_type)

        filter_display = d.pop("FilterDisplay", UNSET)

        show_legend = d.pop("ShowLegend", UNSET)

        show_totals = d.pop("ShowTotals", UNSET)

        show_percentages = d.pop("ShowPercentages", UNSET)

        kpi = []
        _kpi = d.pop("KPI", UNSET)
        for kpi_item_data in _kpi or []:
            kpi_item = ApiChartWidgetKPIEntry.from_dict(kpi_item_data)

            kpi.append(kpi_item)

        _chart_widget_data_specification = d.pop("ChartWidgetDataSpecification", UNSET)
        chart_widget_data_specification: Union[Unset, None, ApiChartWidgetDataSpecification]
        if _chart_widget_data_specification is None:
            chart_widget_data_specification = None
        elif isinstance(_chart_widget_data_specification, Unset):
            chart_widget_data_specification = UNSET
        else:
            chart_widget_data_specification = ApiChartWidgetDataSpecification.from_dict(
                _chart_widget_data_specification
            )

        api_chart_widget_model = cls(
            widget_type=widget_type,
            chart_type=chart_type,
            filter_display=filter_display,
            show_legend=show_legend,
            show_totals=show_totals,
            show_percentages=show_percentages,
            kpi=kpi,
            chart_widget_data_specification=chart_widget_data_specification,
        )

        api_chart_widget_model.additional_properties = d
        return api_chart_widget_model

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
