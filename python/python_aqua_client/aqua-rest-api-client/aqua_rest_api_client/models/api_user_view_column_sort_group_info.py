from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_column_sort_order import ApiColumnSortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserViewColumnSortGroupInfo")


@attr.s(auto_attribs=True)
class ApiUserViewColumnSortGroupInfo:
    """Contains the user view column sorting and grouping information.

    Attributes:
        field_id (Union[Unset, None, str]): The name of the column.
        title (Union[Unset, None, str]): The label of the column.
        sort_order (Union[Unset, ApiColumnSortOrder]): Represents the sort orders.
            This enum has the following values:
              - `Ascending` Sorts the columns in descending order.
              - `Descending` Sorts the columns in descending order.
        is_grouped (Union[Unset, bool]): Indicates if the column is grouped.
    """

    field_id: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    sort_order: Union[Unset, ApiColumnSortOrder] = UNSET
    is_grouped: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        title = self.title
        sort_order: Union[Unset, str] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        is_grouped = self.is_grouped

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if title is not UNSET:
            field_dict["Title"] = title
        if sort_order is not UNSET:
            field_dict["SortOrder"] = sort_order
        if is_grouped is not UNSET:
            field_dict["IsGrouped"] = is_grouped

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId", UNSET)

        title = d.pop("Title", UNSET)

        _sort_order = d.pop("SortOrder", UNSET)
        sort_order: Union[Unset, ApiColumnSortOrder]
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = ApiColumnSortOrder(_sort_order)

        is_grouped = d.pop("IsGrouped", UNSET)

        api_user_view_column_sort_group_info = cls(
            field_id=field_id,
            title=title,
            sort_order=sort_order,
            is_grouped=is_grouped,
        )

        return api_user_view_column_sort_group_info
