from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_list_widget_data_specification import ApiItemListWidgetDataSpecification


T = TypeVar("T", bound="ApiItemListWidgetModel")


@attr.s(auto_attribs=True)
class ApiItemListWidgetModel:
    """
    Attributes:
        widget_type (str):
        columns (Union[Unset, None, List[str]]): Columns to be presented in the grid.
        filter_display (Union[Unset, None, str]): Textual representation of the filter string which is included in
            ItemListWidgetDataSpecification.
        item_list_widget_data_specification (Union[Unset, None, ApiItemListWidgetDataSpecification]): The data
            specification for an item list widget
    """

    widget_type: str
    columns: Union[Unset, None, List[str]] = UNSET
    filter_display: Union[Unset, None, str] = UNSET
    item_list_widget_data_specification: Union[Unset, None, "ApiItemListWidgetDataSpecification"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        widget_type = self.widget_type
        columns: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            if self.columns is None:
                columns = None
            else:
                columns = self.columns

        filter_display = self.filter_display
        item_list_widget_data_specification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.item_list_widget_data_specification, Unset):
            item_list_widget_data_specification = (
                self.item_list_widget_data_specification.to_dict() if self.item_list_widget_data_specification else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "WidgetType": widget_type,
            }
        )
        if columns is not UNSET:
            field_dict["Columns"] = columns
        if filter_display is not UNSET:
            field_dict["FilterDisplay"] = filter_display
        if item_list_widget_data_specification is not UNSET:
            field_dict["ItemListWidgetDataSpecification"] = item_list_widget_data_specification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_list_widget_data_specification import ApiItemListWidgetDataSpecification

        d = src_dict.copy()
        widget_type = d.pop("WidgetType")

        columns = cast(List[str], d.pop("Columns", UNSET))

        filter_display = d.pop("FilterDisplay", UNSET)

        _item_list_widget_data_specification = d.pop("ItemListWidgetDataSpecification", UNSET)
        item_list_widget_data_specification: Union[Unset, None, ApiItemListWidgetDataSpecification]
        if _item_list_widget_data_specification is None:
            item_list_widget_data_specification = None
        elif isinstance(_item_list_widget_data_specification, Unset):
            item_list_widget_data_specification = UNSET
        else:
            item_list_widget_data_specification = ApiItemListWidgetDataSpecification.from_dict(
                _item_list_widget_data_specification
            )

        api_item_list_widget_model = cls(
            widget_type=widget_type,
            columns=columns,
            filter_display=filter_display,
            item_list_widget_data_specification=item_list_widget_data_specification,
        )

        api_item_list_widget_model.additional_properties = d
        return api_item_list_widget_model

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
