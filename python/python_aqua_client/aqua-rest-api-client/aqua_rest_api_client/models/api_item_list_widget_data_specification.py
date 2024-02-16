from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_list_widget_sorting import ApiItemListWidgetSorting


T = TypeVar("T", bound="ApiItemListWidgetDataSpecification")


@attr.s(auto_attribs=True)
class ApiItemListWidgetDataSpecification:
    """The data specification for an item list widget

    Attributes:
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
        filter_expression (Union[Unset, Any]): Filter expression to be used.
        first_results (Union[Unset, int]): Number of elements to skip (used for pagination)
        max_results (Union[Unset, int]): Number of elements to take (used for pagination)
        culture (Union[Unset, None, str]): Language ('en' or 'de'), required for generating values of some fields
            that depend on the current language (e.g. last execution status).
        sort_columns (Union[Unset, None, List['ApiItemListWidgetSorting']]): The sorting which should be applied to the
            item list
    """

    item_type: Union[Unset, ApiItemType] = UNSET
    filter_expression: Union[Unset, Any] = UNSET
    first_results: Union[Unset, int] = UNSET
    max_results: Union[Unset, int] = UNSET
    culture: Union[Unset, None, str] = UNSET
    sort_columns: Union[Unset, None, List["ApiItemListWidgetSorting"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        filter_expression = self.filter_expression
        first_results = self.first_results
        max_results = self.max_results
        culture = self.culture
        sort_columns: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sort_columns, Unset):
            if self.sort_columns is None:
                sort_columns = None
            else:
                sort_columns = []
                for sort_columns_item_data in self.sort_columns:
                    sort_columns_item = sort_columns_item_data.to_dict()

                    sort_columns.append(sort_columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if filter_expression is not UNSET:
            field_dict["FilterExpression"] = filter_expression
        if first_results is not UNSET:
            field_dict["FirstResults"] = first_results
        if max_results is not UNSET:
            field_dict["MaxResults"] = max_results
        if culture is not UNSET:
            field_dict["Culture"] = culture
        if sort_columns is not UNSET:
            field_dict["SortColumns"] = sort_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_list_widget_sorting import ApiItemListWidgetSorting

        d = src_dict.copy()
        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        filter_expression = d.pop("FilterExpression", UNSET)

        first_results = d.pop("FirstResults", UNSET)

        max_results = d.pop("MaxResults", UNSET)

        culture = d.pop("Culture", UNSET)

        sort_columns = []
        _sort_columns = d.pop("SortColumns", UNSET)
        for sort_columns_item_data in _sort_columns or []:
            sort_columns_item = ApiItemListWidgetSorting.from_dict(sort_columns_item_data)

            sort_columns.append(sort_columns_item)

        api_item_list_widget_data_specification = cls(
            item_type=item_type,
            filter_expression=filter_expression,
            first_results=first_results,
            max_results=max_results,
            culture=culture,
            sort_columns=sort_columns,
        )

        return api_item_list_widget_data_specification
