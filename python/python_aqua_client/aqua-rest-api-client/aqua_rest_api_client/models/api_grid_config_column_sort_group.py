from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_grid_config_column_sort_order import ApiGridConfigColumnSortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiGridConfigColumnSortGroup")


@attr.s(auto_attribs=True)
class ApiGridConfigColumnSortGroup:
    """Information regarding the sorting/grouping of a single column

    Attributes:
        field_id (Union[Unset, None, str]): The id of the field
        sort_order (Union[Unset, ApiGridConfigColumnSortOrder]): The direction in which the column is sorted
        is_grouped (Union[Unset, bool]): Indicates whether this column is grouped
    """

    field_id: Union[Unset, None, str] = UNSET
    sort_order: Union[Unset, ApiGridConfigColumnSortOrder] = UNSET
    is_grouped: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        sort_order: Union[Unset, int] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        is_grouped = self.is_grouped

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if sort_order is not UNSET:
            field_dict["SortOrder"] = sort_order
        if is_grouped is not UNSET:
            field_dict["IsGrouped"] = is_grouped

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId", UNSET)

        _sort_order = d.pop("SortOrder", UNSET)
        sort_order: Union[Unset, ApiGridConfigColumnSortOrder]
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = ApiGridConfigColumnSortOrder(_sort_order)

        is_grouped = d.pop("IsGrouped", UNSET)

        api_grid_config_column_sort_group = cls(
            field_id=field_id,
            sort_order=sort_order,
            is_grouped=is_grouped,
        )

        return api_grid_config_column_sort_group
