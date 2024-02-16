from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_chart_widget_data_status import ApiChartWidgetDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_chart_widget_data_one_dimensional_element import ApiChartWidgetDataOneDimensionalElement
    from ..models.api_chart_widget_data_two_dimensional_element import ApiChartWidgetDataTwoDimensionalElement
    from ..models.api_field_meta import ApiFieldMeta


T = TypeVar("T", bound="ApiChartWidgetData")


@attr.s(auto_attribs=True)
class ApiChartWidgetData:
    """
    Attributes:
        data_type (str):
        status (Union[Unset, ApiChartWidgetDataStatus]):
            This enum has the following values:
              - `InvalidFilter`
              - `InvalidSpecification`
              - `NoPermission`
              - `OK`
        one_dimensional_data (Union[Unset, None, List['ApiChartWidgetDataOneDimensionalElement']]): The data points for
            a one-dimensional chart
        two_dimensional_data (Union[Unset, None, List['ApiChartWidgetDataTwoDimensionalElement']]): The data points for
            a two-dimensional chart
        group_by_field_meta (Union[Unset, None, ApiFieldMeta]): Contains the meta-information of a specific field.
        x_axis_field_meta (Union[Unset, None, ApiFieldMeta]): Contains the meta-information of a specific field.
    """

    data_type: str
    status: Union[Unset, ApiChartWidgetDataStatus] = UNSET
    one_dimensional_data: Union[Unset, None, List["ApiChartWidgetDataOneDimensionalElement"]] = UNSET
    two_dimensional_data: Union[Unset, None, List["ApiChartWidgetDataTwoDimensionalElement"]] = UNSET
    group_by_field_meta: Union[Unset, None, "ApiFieldMeta"] = UNSET
    x_axis_field_meta: Union[Unset, None, "ApiFieldMeta"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_type = self.data_type
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        one_dimensional_data: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.one_dimensional_data, Unset):
            if self.one_dimensional_data is None:
                one_dimensional_data = None
            else:
                one_dimensional_data = []
                for one_dimensional_data_item_data in self.one_dimensional_data:
                    one_dimensional_data_item = one_dimensional_data_item_data.to_dict()

                    one_dimensional_data.append(one_dimensional_data_item)

        two_dimensional_data: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.two_dimensional_data, Unset):
            if self.two_dimensional_data is None:
                two_dimensional_data = None
            else:
                two_dimensional_data = []
                for two_dimensional_data_item_data in self.two_dimensional_data:
                    two_dimensional_data_item = two_dimensional_data_item_data.to_dict()

                    two_dimensional_data.append(two_dimensional_data_item)

        group_by_field_meta: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.group_by_field_meta, Unset):
            group_by_field_meta = self.group_by_field_meta.to_dict() if self.group_by_field_meta else None

        x_axis_field_meta: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.x_axis_field_meta, Unset):
            x_axis_field_meta = self.x_axis_field_meta.to_dict() if self.x_axis_field_meta else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DataType": data_type,
            }
        )
        if status is not UNSET:
            field_dict["Status"] = status
        if one_dimensional_data is not UNSET:
            field_dict["OneDimensionalData"] = one_dimensional_data
        if two_dimensional_data is not UNSET:
            field_dict["TwoDimensionalData"] = two_dimensional_data
        if group_by_field_meta is not UNSET:
            field_dict["GroupByFieldMeta"] = group_by_field_meta
        if x_axis_field_meta is not UNSET:
            field_dict["XAxisFieldMeta"] = x_axis_field_meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_chart_widget_data_one_dimensional_element import ApiChartWidgetDataOneDimensionalElement
        from ..models.api_chart_widget_data_two_dimensional_element import ApiChartWidgetDataTwoDimensionalElement
        from ..models.api_field_meta import ApiFieldMeta

        d = src_dict.copy()
        data_type = d.pop("DataType")

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiChartWidgetDataStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiChartWidgetDataStatus(_status)

        one_dimensional_data = []
        _one_dimensional_data = d.pop("OneDimensionalData", UNSET)
        for one_dimensional_data_item_data in _one_dimensional_data or []:
            one_dimensional_data_item = ApiChartWidgetDataOneDimensionalElement.from_dict(
                one_dimensional_data_item_data
            )

            one_dimensional_data.append(one_dimensional_data_item)

        two_dimensional_data = []
        _two_dimensional_data = d.pop("TwoDimensionalData", UNSET)
        for two_dimensional_data_item_data in _two_dimensional_data or []:
            two_dimensional_data_item = ApiChartWidgetDataTwoDimensionalElement.from_dict(
                two_dimensional_data_item_data
            )

            two_dimensional_data.append(two_dimensional_data_item)

        _group_by_field_meta = d.pop("GroupByFieldMeta", UNSET)
        group_by_field_meta: Union[Unset, None, ApiFieldMeta]
        if _group_by_field_meta is None:
            group_by_field_meta = None
        elif isinstance(_group_by_field_meta, Unset):
            group_by_field_meta = UNSET
        else:
            group_by_field_meta = ApiFieldMeta.from_dict(_group_by_field_meta)

        _x_axis_field_meta = d.pop("XAxisFieldMeta", UNSET)
        x_axis_field_meta: Union[Unset, None, ApiFieldMeta]
        if _x_axis_field_meta is None:
            x_axis_field_meta = None
        elif isinstance(_x_axis_field_meta, Unset):
            x_axis_field_meta = UNSET
        else:
            x_axis_field_meta = ApiFieldMeta.from_dict(_x_axis_field_meta)

        api_chart_widget_data = cls(
            data_type=data_type,
            status=status,
            one_dimensional_data=one_dimensional_data,
            two_dimensional_data=two_dimensional_data,
            group_by_field_meta=group_by_field_meta,
            x_axis_field_meta=x_axis_field_meta,
        )

        api_chart_widget_data.additional_properties = d
        return api_chart_widget_data

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
