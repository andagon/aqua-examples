from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_global_search_area import ApiGlobalSearchArea
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiGlobalSearchRequest")


@attr.s(auto_attribs=True)
class ApiGlobalSearchRequest:
    """Represents a request for a global items search

    Attributes:
        search_area (Union[Unset, ApiGlobalSearchArea]): Represents available areas for search
            This enum has the following values:
              - `AllItems`
              - `Defects`
              - `Requirements`
              - `Scripts`
              - `TestCases`
              - `TestScenarios`
        search_text (Union[Unset, None, str]): Searching text
        include_archived (Union[Unset, bool]): Shows if archived projects will be included or not
        start_at (Union[Unset, int]): The number of items which were skipped in the list of results.
            This value is provided during the request.
        max_results (Union[Unset, int]): The maximum number of items which should be included in the result.
        project_id (Union[Unset, int]): Id of project where items will be searched. If value equals 0 it means that
            items will be searched among all projects
        folder_id (Union[Unset, int]): The id of the folder of which the items are loaded.
        include_subfolders (Union[Unset, bool]): Indicates whether items from sub folders should be included.
    """

    search_area: Union[Unset, ApiGlobalSearchArea] = UNSET
    search_text: Union[Unset, None, str] = UNSET
    include_archived: Union[Unset, bool] = UNSET
    start_at: Union[Unset, int] = UNSET
    max_results: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    folder_id: Union[Unset, int] = UNSET
    include_subfolders: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        search_area: Union[Unset, str] = UNSET
        if not isinstance(self.search_area, Unset):
            search_area = self.search_area.value

        search_text = self.search_text
        include_archived = self.include_archived
        start_at = self.start_at
        max_results = self.max_results
        project_id = self.project_id
        folder_id = self.folder_id
        include_subfolders = self.include_subfolders

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if search_area is not UNSET:
            field_dict["SearchArea"] = search_area
        if search_text is not UNSET:
            field_dict["SearchText"] = search_text
        if include_archived is not UNSET:
            field_dict["IncludeArchived"] = include_archived
        if start_at is not UNSET:
            field_dict["StartAt"] = start_at
        if max_results is not UNSET:
            field_dict["MaxResults"] = max_results
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if include_subfolders is not UNSET:
            field_dict["IncludeSubfolders"] = include_subfolders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _search_area = d.pop("SearchArea", UNSET)
        search_area: Union[Unset, ApiGlobalSearchArea]
        if isinstance(_search_area, Unset):
            search_area = UNSET
        else:
            search_area = ApiGlobalSearchArea(_search_area)

        search_text = d.pop("SearchText", UNSET)

        include_archived = d.pop("IncludeArchived", UNSET)

        start_at = d.pop("StartAt", UNSET)

        max_results = d.pop("MaxResults", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        include_subfolders = d.pop("IncludeSubfolders", UNSET)

        api_global_search_request = cls(
            search_area=search_area,
            search_text=search_text,
            include_archived=include_archived,
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
            folder_id=folder_id,
            include_subfolders=include_subfolders,
        )

        return api_global_search_request
