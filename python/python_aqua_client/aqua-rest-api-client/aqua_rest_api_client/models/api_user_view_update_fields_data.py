from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_filter_update import ApiFilterUpdate
    from ..models.api_user_view_column_sort_group_update import ApiUserViewColumnSortGroupUpdate
    from ..models.api_user_view_column_update import ApiUserViewColumnUpdate


T = TypeVar("T", bound="ApiUserViewUpdateFieldsData")


@attr.s(auto_attribs=True)
class ApiUserViewUpdateFieldsData:
    """Contains all changes of a user view which depend on the
    item type: filter, sorting/grouping and columns.

        Attributes:
            item_type (ApiItemType): Identifies the type of item.
                This enum has the following values:
                  - `Defect`
                  - `ExternalJira`
                  - `ExternalOtrs`
                  - `Requirement`
                  - `Script`
                  - `TestCase`
                  - `TestExecution`
                  - `TestScenario`
            filter_ (Union[Unset, None, ApiFilterUpdate]): Contains the new filter expression.
            columns (Union[Unset, None, List['ApiUserViewColumnUpdate']]): Contains the list of columns.
            sorting_grouping (Union[Unset, None, List['ApiUserViewColumnSortGroupUpdate']]): Contains the list of sorting
                and grouping information for columns.
    """

    item_type: ApiItemType
    filter_: Union[Unset, None, "ApiFilterUpdate"] = UNSET
    columns: Union[Unset, None, List["ApiUserViewColumnUpdate"]] = UNSET
    sorting_grouping: Union[Unset, None, List["ApiUserViewColumnSortGroupUpdate"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type = self.item_type.value

        filter_: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict() if self.filter_ else None

        columns: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            if self.columns is None:
                columns = None
            else:
                columns = []
                for columns_item_data in self.columns:
                    columns_item = columns_item_data.to_dict()

                    columns.append(columns_item)

        sorting_grouping: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorting_grouping, Unset):
            if self.sorting_grouping is None:
                sorting_grouping = None
            else:
                sorting_grouping = []
                for sorting_grouping_item_data in self.sorting_grouping:
                    sorting_grouping_item = sorting_grouping_item_data.to_dict()

                    sorting_grouping.append(sorting_grouping_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ItemType": item_type,
            }
        )
        if filter_ is not UNSET:
            field_dict["Filter"] = filter_
        if columns is not UNSET:
            field_dict["Columns"] = columns
        if sorting_grouping is not UNSET:
            field_dict["SortingGrouping"] = sorting_grouping

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_filter_update import ApiFilterUpdate
        from ..models.api_user_view_column_sort_group_update import ApiUserViewColumnSortGroupUpdate
        from ..models.api_user_view_column_update import ApiUserViewColumnUpdate

        d = src_dict.copy()
        item_type = ApiItemType(d.pop("ItemType"))

        _filter_ = d.pop("Filter", UNSET)
        filter_: Union[Unset, None, ApiFilterUpdate]
        if _filter_ is None:
            filter_ = None
        elif isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ApiFilterUpdate.from_dict(_filter_)

        columns = []
        _columns = d.pop("Columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = ApiUserViewColumnUpdate.from_dict(columns_item_data)

            columns.append(columns_item)

        sorting_grouping = []
        _sorting_grouping = d.pop("SortingGrouping", UNSET)
        for sorting_grouping_item_data in _sorting_grouping or []:
            sorting_grouping_item = ApiUserViewColumnSortGroupUpdate.from_dict(sorting_grouping_item_data)

            sorting_grouping.append(sorting_grouping_item)

        api_user_view_update_fields_data = cls(
            item_type=item_type,
            filter_=filter_,
            columns=columns,
            sorting_grouping=sorting_grouping,
        )

        return api_user_view_update_fields_data
