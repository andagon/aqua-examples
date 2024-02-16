from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_filter_update import ApiFilterUpdate


T = TypeVar("T", bound="ApiTestScenarioReportOptions")


@attr.s(auto_attribs=True)
class ApiTestScenarioReportOptions:
    """
    Attributes:
        item_type (str):
        path (Union[Unset, None, List[ApiItemType]]): The path of the options.
        filter_ (Union[Unset, None, ApiFilterUpdate]): Contains the new filter expression.
        include_description (Union[Unset, bool]): Option, include description.
        include_pictures (Union[Unset, bool]): Option, include pictures.
        show_details (Union[Unset, bool]): Option, show details.
        include_history (Union[Unset, bool]): Option, include history.
        include_attachments (Union[Unset, bool]): Option, include attachments.
        include_jira_items (Union[Unset, bool]): Option, include attachments.
        show_related_defects (Union[Unset, bool]): Option, show related defects.
        show_related_requirements (Union[Unset, bool]): Option, show related requirements.
        show_related_test_cases (Union[Unset, bool]): Option, show related test cases.
        show_related_test_scenarios (Union[Unset, bool]): Option, show related test scenarios.
        include_test_jobs (Union[Unset, bool]): Option, include test jobs.
        include_executions (Union[Unset, bool]): Option, include executions.
    """

    item_type: str
    path: Union[Unset, None, List[ApiItemType]] = UNSET
    filter_: Union[Unset, None, "ApiFilterUpdate"] = UNSET
    include_description: Union[Unset, bool] = UNSET
    include_pictures: Union[Unset, bool] = UNSET
    show_details: Union[Unset, bool] = UNSET
    include_history: Union[Unset, bool] = UNSET
    include_attachments: Union[Unset, bool] = UNSET
    include_jira_items: Union[Unset, bool] = UNSET
    show_related_defects: Union[Unset, bool] = UNSET
    show_related_requirements: Union[Unset, bool] = UNSET
    show_related_test_cases: Union[Unset, bool] = UNSET
    show_related_test_scenarios: Union[Unset, bool] = UNSET
    include_test_jobs: Union[Unset, bool] = UNSET
    include_executions: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_type = self.item_type
        path: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.path, Unset):
            if self.path is None:
                path = None
            else:
                path = []
                for path_item_data in self.path:
                    path_item = path_item_data.value

                    path.append(path_item)

        filter_: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict() if self.filter_ else None

        include_description = self.include_description
        include_pictures = self.include_pictures
        show_details = self.show_details
        include_history = self.include_history
        include_attachments = self.include_attachments
        include_jira_items = self.include_jira_items
        show_related_defects = self.show_related_defects
        show_related_requirements = self.show_related_requirements
        show_related_test_cases = self.show_related_test_cases
        show_related_test_scenarios = self.show_related_test_scenarios
        include_test_jobs = self.include_test_jobs
        include_executions = self.include_executions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ItemType": item_type,
            }
        )
        if path is not UNSET:
            field_dict["Path"] = path
        if filter_ is not UNSET:
            field_dict["Filter"] = filter_
        if include_description is not UNSET:
            field_dict["IncludeDescription"] = include_description
        if include_pictures is not UNSET:
            field_dict["IncludePictures"] = include_pictures
        if show_details is not UNSET:
            field_dict["ShowDetails"] = show_details
        if include_history is not UNSET:
            field_dict["IncludeHistory"] = include_history
        if include_attachments is not UNSET:
            field_dict["IncludeAttachments"] = include_attachments
        if include_jira_items is not UNSET:
            field_dict["IncludeJiraItems"] = include_jira_items
        if show_related_defects is not UNSET:
            field_dict["ShowRelatedDefects"] = show_related_defects
        if show_related_requirements is not UNSET:
            field_dict["ShowRelatedRequirements"] = show_related_requirements
        if show_related_test_cases is not UNSET:
            field_dict["ShowRelatedTestCases"] = show_related_test_cases
        if show_related_test_scenarios is not UNSET:
            field_dict["ShowRelatedTestScenarios"] = show_related_test_scenarios
        if include_test_jobs is not UNSET:
            field_dict["IncludeTestJobs"] = include_test_jobs
        if include_executions is not UNSET:
            field_dict["IncludeExecutions"] = include_executions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_filter_update import ApiFilterUpdate

        d = src_dict.copy()
        item_type = d.pop("ItemType")

        path = []
        _path = d.pop("Path", UNSET)
        for path_item_data in _path or []:
            path_item = ApiItemType(path_item_data)

            path.append(path_item)

        _filter_ = d.pop("Filter", UNSET)
        filter_: Union[Unset, None, ApiFilterUpdate]
        if _filter_ is None:
            filter_ = None
        elif isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ApiFilterUpdate.from_dict(_filter_)

        include_description = d.pop("IncludeDescription", UNSET)

        include_pictures = d.pop("IncludePictures", UNSET)

        show_details = d.pop("ShowDetails", UNSET)

        include_history = d.pop("IncludeHistory", UNSET)

        include_attachments = d.pop("IncludeAttachments", UNSET)

        include_jira_items = d.pop("IncludeJiraItems", UNSET)

        show_related_defects = d.pop("ShowRelatedDefects", UNSET)

        show_related_requirements = d.pop("ShowRelatedRequirements", UNSET)

        show_related_test_cases = d.pop("ShowRelatedTestCases", UNSET)

        show_related_test_scenarios = d.pop("ShowRelatedTestScenarios", UNSET)

        include_test_jobs = d.pop("IncludeTestJobs", UNSET)

        include_executions = d.pop("IncludeExecutions", UNSET)

        api_test_scenario_report_options = cls(
            item_type=item_type,
            path=path,
            filter_=filter_,
            include_description=include_description,
            include_pictures=include_pictures,
            show_details=show_details,
            include_history=include_history,
            include_attachments=include_attachments,
            include_jira_items=include_jira_items,
            show_related_defects=show_related_defects,
            show_related_requirements=show_related_requirements,
            show_related_test_cases=show_related_test_cases,
            show_related_test_scenarios=show_related_test_scenarios,
            include_test_jobs=include_test_jobs,
            include_executions=include_executions,
        )

        api_test_scenario_report_options.additional_properties = d
        return api_test_scenario_report_options

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
