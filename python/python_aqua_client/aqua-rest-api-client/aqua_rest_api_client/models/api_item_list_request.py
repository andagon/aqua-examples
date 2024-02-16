from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemListRequest")


@attr.s(auto_attribs=True)
class ApiItemListRequest:
    """Items list request with filtering, sorting, and paging

    Attributes:
        project_id (Union[Unset, int]): The id of the project of which the items are loaded.
        folder_id (Union[Unset, int]): The id of the folder of which the items are loaded.
        item_types (Union[Unset, None, str]): The item types to import as comma-separated list.
            Possible values for item type are: Defect, Requirement, TestCase, TestScenario and Script.
        search (Union[Unset, None, str]): Contains filter and search information.
        sprint_id (Union[Unset, None, int]): Sprint filter:
            Not specified - do not filter by sprint
            0 - select items without psorint assigned only
            1+ - select items for specified sprint only
        order_by (Union[Unset, None, str]): Comma-separated list of properties which should be used to order
            the result list. ASC or DESC can be appended to indicate the sort order. Ascending sort
            order is assumed by default.
        include_subfolders (Union[Unset, bool]): Indicates whether items from sub folders should be included.
        include_archived (Union[Unset, bool]): Indicates whether archieved items should be included.
        start_at (Union[Unset, int]): Number of results to skip when the results are fetched.
            Can be used for pagination.
        max_results (Union[Unset, int]): Maximum number of results which are fetched.
            Can be used for pagination.
        is_filtered_by_status (Union[Unset, bool]): Indicates whether items should be filtered by status
        include_edit_layout (Union[Unset, bool]): Whether or not to include the edit layout in each item
    """

    project_id: Union[Unset, int] = UNSET
    folder_id: Union[Unset, int] = UNSET
    item_types: Union[Unset, None, str] = UNSET
    search: Union[Unset, None, str] = UNSET
    sprint_id: Union[Unset, None, int] = UNSET
    order_by: Union[Unset, None, str] = UNSET
    include_subfolders: Union[Unset, bool] = UNSET
    include_archived: Union[Unset, bool] = UNSET
    start_at: Union[Unset, int] = UNSET
    max_results: Union[Unset, int] = UNSET
    is_filtered_by_status: Union[Unset, bool] = UNSET
    include_edit_layout: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        folder_id = self.folder_id
        item_types = self.item_types
        search = self.search
        sprint_id = self.sprint_id
        order_by = self.order_by
        include_subfolders = self.include_subfolders
        include_archived = self.include_archived
        start_at = self.start_at
        max_results = self.max_results
        is_filtered_by_status = self.is_filtered_by_status
        include_edit_layout = self.include_edit_layout

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if item_types is not UNSET:
            field_dict["ItemTypes"] = item_types
        if search is not UNSET:
            field_dict["Search"] = search
        if sprint_id is not UNSET:
            field_dict["SprintId"] = sprint_id
        if order_by is not UNSET:
            field_dict["OrderBy"] = order_by
        if include_subfolders is not UNSET:
            field_dict["IncludeSubfolders"] = include_subfolders
        if include_archived is not UNSET:
            field_dict["IncludeArchived"] = include_archived
        if start_at is not UNSET:
            field_dict["StartAt"] = start_at
        if max_results is not UNSET:
            field_dict["MaxResults"] = max_results
        if is_filtered_by_status is not UNSET:
            field_dict["IsFilteredByStatus"] = is_filtered_by_status
        if include_edit_layout is not UNSET:
            field_dict["IncludeEditLayout"] = include_edit_layout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = d.pop("ProjectId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        item_types = d.pop("ItemTypes", UNSET)

        search = d.pop("Search", UNSET)

        sprint_id = d.pop("SprintId", UNSET)

        order_by = d.pop("OrderBy", UNSET)

        include_subfolders = d.pop("IncludeSubfolders", UNSET)

        include_archived = d.pop("IncludeArchived", UNSET)

        start_at = d.pop("StartAt", UNSET)

        max_results = d.pop("MaxResults", UNSET)

        is_filtered_by_status = d.pop("IsFilteredByStatus", UNSET)

        include_edit_layout = d.pop("IncludeEditLayout", UNSET)

        api_item_list_request = cls(
            project_id=project_id,
            folder_id=folder_id,
            item_types=item_types,
            search=search,
            sprint_id=sprint_id,
            order_by=order_by,
            include_subfolders=include_subfolders,
            include_archived=include_archived,
            start_at=start_at,
            max_results=max_results,
            is_filtered_by_status=is_filtered_by_status,
            include_edit_layout=include_edit_layout,
        )

        return api_item_list_request
