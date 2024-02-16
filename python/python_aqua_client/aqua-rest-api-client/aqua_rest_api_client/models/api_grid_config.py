from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_grid_config_column import ApiGridConfigColumn
    from ..models.api_grid_config_column_sort_group import ApiGridConfigColumnSortGroup


T = TypeVar("T", bound="ApiGridConfig")


@attr.s(auto_attribs=True)
class ApiGridConfig:
    """The configuration of the item grid for a specific
    project and item type

        Attributes:
            active_user_view_id (Union[Unset, None, int]): The id of the currently selected user view.
                Can be null when no user view is selected
            include_subfolders (Union[Unset, bool]): Indicates whether sub folder should be included
            include_archived_items (Union[Unset, bool]): Indicates whether archieved items should be
                included
            show_filter_row (Union[Unset, bool]): Indicates whether the filter row of the grid
                is visible.
            filter_expression (Union[Unset, None, List[Any]]): The currently set filter
            is_filter_active (Union[Unset, bool]): indicates whether the filter is active
            columns (Union[Unset, None, List['ApiGridConfigColumn']]): The list of visible columns
            sort_group (Union[Unset, None, List['ApiGridConfigColumnSortGroup']]): The list of columns for which the data is
                sorted
                or grouped by
    """

    active_user_view_id: Union[Unset, None, int] = UNSET
    include_subfolders: Union[Unset, bool] = UNSET
    include_archived_items: Union[Unset, bool] = UNSET
    show_filter_row: Union[Unset, bool] = UNSET
    filter_expression: Union[Unset, None, List[Any]] = UNSET
    is_filter_active: Union[Unset, bool] = UNSET
    columns: Union[Unset, None, List["ApiGridConfigColumn"]] = UNSET
    sort_group: Union[Unset, None, List["ApiGridConfigColumnSortGroup"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        active_user_view_id = self.active_user_view_id
        include_subfolders = self.include_subfolders
        include_archived_items = self.include_archived_items
        show_filter_row = self.show_filter_row
        filter_expression: Union[Unset, None, List[Any]] = UNSET
        if not isinstance(self.filter_expression, Unset):
            if self.filter_expression is None:
                filter_expression = None
            else:
                filter_expression = self.filter_expression

        is_filter_active = self.is_filter_active
        columns: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            if self.columns is None:
                columns = None
            else:
                columns = []
                for columns_item_data in self.columns:
                    columns_item = columns_item_data.to_dict()

                    columns.append(columns_item)

        sort_group: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sort_group, Unset):
            if self.sort_group is None:
                sort_group = None
            else:
                sort_group = []
                for sort_group_item_data in self.sort_group:
                    sort_group_item = sort_group_item_data.to_dict()

                    sort_group.append(sort_group_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if active_user_view_id is not UNSET:
            field_dict["ActiveUserViewId"] = active_user_view_id
        if include_subfolders is not UNSET:
            field_dict["IncludeSubfolders"] = include_subfolders
        if include_archived_items is not UNSET:
            field_dict["IncludeArchivedItems"] = include_archived_items
        if show_filter_row is not UNSET:
            field_dict["ShowFilterRow"] = show_filter_row
        if filter_expression is not UNSET:
            field_dict["FilterExpression"] = filter_expression
        if is_filter_active is not UNSET:
            field_dict["IsFilterActive"] = is_filter_active
        if columns is not UNSET:
            field_dict["Columns"] = columns
        if sort_group is not UNSET:
            field_dict["SortGroup"] = sort_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_grid_config_column import ApiGridConfigColumn
        from ..models.api_grid_config_column_sort_group import ApiGridConfigColumnSortGroup

        d = src_dict.copy()
        active_user_view_id = d.pop("ActiveUserViewId", UNSET)

        include_subfolders = d.pop("IncludeSubfolders", UNSET)

        include_archived_items = d.pop("IncludeArchivedItems", UNSET)

        show_filter_row = d.pop("ShowFilterRow", UNSET)

        filter_expression = cast(List[Any], d.pop("FilterExpression", UNSET))

        is_filter_active = d.pop("IsFilterActive", UNSET)

        columns = []
        _columns = d.pop("Columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = ApiGridConfigColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        sort_group = []
        _sort_group = d.pop("SortGroup", UNSET)
        for sort_group_item_data in _sort_group or []:
            sort_group_item = ApiGridConfigColumnSortGroup.from_dict(sort_group_item_data)

            sort_group.append(sort_group_item)

        api_grid_config = cls(
            active_user_view_id=active_user_view_id,
            include_subfolders=include_subfolders,
            include_archived_items=include_archived_items,
            show_filter_row=show_filter_row,
            filter_expression=filter_expression,
            is_filter_active=is_filter_active,
            columns=columns,
            sort_group=sort_group,
        )

        return api_grid_config
