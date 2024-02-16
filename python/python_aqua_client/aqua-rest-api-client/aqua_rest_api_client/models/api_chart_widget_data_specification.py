from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_chart_widget_date_time_scale import ApiChartWidgetDateTimeScale
from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiChartWidgetDataSpecification")


@attr.s(auto_attribs=True)
class ApiChartWidgetDataSpecification:
    """Data specification for the chart widget

    Attributes:
        dimensions (Union[Unset, int]): Number of dimensions. Allowed values are 1 or 2
        item_type (Union[Unset, ApiItemType]): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        x_axis_property_title (Union[Unset, None, str]): Title of the field used to aggregate on X-axis (used only if
            the number of dimensions is 2).
        x_axis_date_time_scale (Union[Unset, ApiChartWidgetDateTimeScale]):
            This enum has the following values:
              - `CalendarWeek` Aggregate by calendar week
              - `Day` Aggregate by day (default)
              - `Month` Aggregate by month
        x_axis_separate_multi_list (Union[Unset, bool]): If true and field used for aggregation on X-axis is a multi-
            select field (dictionary or user)
            then data is aggregated for each single element of the multi-select list, not for subsets.
            (used only if number od dimensions is 2)
        group_by_property_title (Union[Unset, None, str]): Title of the field used to group by.
        group_by_date_time_scale (Union[Unset, ApiChartWidgetDateTimeScale]):
            This enum has the following values:
              - `CalendarWeek` Aggregate by calendar week
              - `Day` Aggregate by day (default)
              - `Month` Aggregate by month
        group_by_separate_multi_list (Union[Unset, bool]): If true and field used for aggregation on Group-By is a
            multi-select field (dictionary or user)
            then data is aggregated for each single element of the multi-select list, not for subsets.
        filter_expression (Union[Unset, Any]): Filter expression to be used for filtering data for this chart
        reverse_sort_x_axis (Union[Unset, bool]): If true then sorting on X-axis should be reversed  (used only if
            number od dimensions is 2)
        reverse_sort_group_by (Union[Unset, bool]): If true then sorting on group-by should be reversed
    """

    dimensions: Union[Unset, int] = UNSET
    item_type: Union[Unset, ApiItemType] = UNSET
    x_axis_property_title: Union[Unset, None, str] = UNSET
    x_axis_date_time_scale: Union[Unset, ApiChartWidgetDateTimeScale] = UNSET
    x_axis_separate_multi_list: Union[Unset, bool] = UNSET
    group_by_property_title: Union[Unset, None, str] = UNSET
    group_by_date_time_scale: Union[Unset, ApiChartWidgetDateTimeScale] = UNSET
    group_by_separate_multi_list: Union[Unset, bool] = UNSET
    filter_expression: Union[Unset, Any] = UNSET
    reverse_sort_x_axis: Union[Unset, bool] = UNSET
    reverse_sort_group_by: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        dimensions = self.dimensions
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        x_axis_property_title = self.x_axis_property_title
        x_axis_date_time_scale: Union[Unset, str] = UNSET
        if not isinstance(self.x_axis_date_time_scale, Unset):
            x_axis_date_time_scale = self.x_axis_date_time_scale.value

        x_axis_separate_multi_list = self.x_axis_separate_multi_list
        group_by_property_title = self.group_by_property_title
        group_by_date_time_scale: Union[Unset, str] = UNSET
        if not isinstance(self.group_by_date_time_scale, Unset):
            group_by_date_time_scale = self.group_by_date_time_scale.value

        group_by_separate_multi_list = self.group_by_separate_multi_list
        filter_expression = self.filter_expression
        reverse_sort_x_axis = self.reverse_sort_x_axis
        reverse_sort_group_by = self.reverse_sort_group_by

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if dimensions is not UNSET:
            field_dict["Dimensions"] = dimensions
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if x_axis_property_title is not UNSET:
            field_dict["XAxisPropertyTitle"] = x_axis_property_title
        if x_axis_date_time_scale is not UNSET:
            field_dict["XAxisDateTimeScale"] = x_axis_date_time_scale
        if x_axis_separate_multi_list is not UNSET:
            field_dict["XAxisSeparateMultiList"] = x_axis_separate_multi_list
        if group_by_property_title is not UNSET:
            field_dict["GroupByPropertyTitle"] = group_by_property_title
        if group_by_date_time_scale is not UNSET:
            field_dict["GroupByDateTimeScale"] = group_by_date_time_scale
        if group_by_separate_multi_list is not UNSET:
            field_dict["GroupBySeparateMultiList"] = group_by_separate_multi_list
        if filter_expression is not UNSET:
            field_dict["FilterExpression"] = filter_expression
        if reverse_sort_x_axis is not UNSET:
            field_dict["ReverseSortXAxis"] = reverse_sort_x_axis
        if reverse_sort_group_by is not UNSET:
            field_dict["ReverseSortGroupBy"] = reverse_sort_group_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dimensions = d.pop("Dimensions", UNSET)

        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        x_axis_property_title = d.pop("XAxisPropertyTitle", UNSET)

        _x_axis_date_time_scale = d.pop("XAxisDateTimeScale", UNSET)
        x_axis_date_time_scale: Union[Unset, ApiChartWidgetDateTimeScale]
        if isinstance(_x_axis_date_time_scale, Unset):
            x_axis_date_time_scale = UNSET
        else:
            x_axis_date_time_scale = ApiChartWidgetDateTimeScale(_x_axis_date_time_scale)

        x_axis_separate_multi_list = d.pop("XAxisSeparateMultiList", UNSET)

        group_by_property_title = d.pop("GroupByPropertyTitle", UNSET)

        _group_by_date_time_scale = d.pop("GroupByDateTimeScale", UNSET)
        group_by_date_time_scale: Union[Unset, ApiChartWidgetDateTimeScale]
        if isinstance(_group_by_date_time_scale, Unset):
            group_by_date_time_scale = UNSET
        else:
            group_by_date_time_scale = ApiChartWidgetDateTimeScale(_group_by_date_time_scale)

        group_by_separate_multi_list = d.pop("GroupBySeparateMultiList", UNSET)

        filter_expression = d.pop("FilterExpression", UNSET)

        reverse_sort_x_axis = d.pop("ReverseSortXAxis", UNSET)

        reverse_sort_group_by = d.pop("ReverseSortGroupBy", UNSET)

        api_chart_widget_data_specification = cls(
            dimensions=dimensions,
            item_type=item_type,
            x_axis_property_title=x_axis_property_title,
            x_axis_date_time_scale=x_axis_date_time_scale,
            x_axis_separate_multi_list=x_axis_separate_multi_list,
            group_by_property_title=group_by_property_title,
            group_by_date_time_scale=group_by_date_time_scale,
            group_by_separate_multi_list=group_by_separate_multi_list,
            filter_expression=filter_expression,
            reverse_sort_x_axis=reverse_sort_x_axis,
            reverse_sort_group_by=reverse_sort_group_by,
        )

        return api_chart_widget_data_specification
