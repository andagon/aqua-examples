from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_allowed_option import ApiAllowedOption
from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_filter_update import ApiFilterUpdate


T = TypeVar("T", bound="ApiTestScenarioReportAllowedOptionsUpdate")


@attr.s(auto_attribs=True)
class ApiTestScenarioReportAllowedOptionsUpdate:
    """
    Attributes:
        item_type (str):
        include_description (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        include_pictures (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        allow_to_show_hide_details (Union[Unset, bool]): Option, show details.
        include_history (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        include_attachments (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        show_related_defects (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        show_related_requirements (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        show_related_test_cases (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        show_related_test_scenarios (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        include_jira_items (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        path (Union[Unset, None, List[ApiItemType]]): The path of the options.
        filter_ (Union[Unset, None, ApiFilterUpdate]): Contains the new filter expression.
        include_test_jobs (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
        include_executions (Union[Unset, ApiAllowedOption]): Represents possible values for the report option.
            This enum has the following values:
              - `AlwaysFalse` Always false.
              - `AlwaysTrue` Always true.
              - `AskUser` Ask user.
    """

    item_type: str
    include_description: Union[Unset, ApiAllowedOption] = UNSET
    include_pictures: Union[Unset, ApiAllowedOption] = UNSET
    allow_to_show_hide_details: Union[Unset, bool] = UNSET
    include_history: Union[Unset, ApiAllowedOption] = UNSET
    include_attachments: Union[Unset, ApiAllowedOption] = UNSET
    show_related_defects: Union[Unset, ApiAllowedOption] = UNSET
    show_related_requirements: Union[Unset, ApiAllowedOption] = UNSET
    show_related_test_cases: Union[Unset, ApiAllowedOption] = UNSET
    show_related_test_scenarios: Union[Unset, ApiAllowedOption] = UNSET
    include_jira_items: Union[Unset, ApiAllowedOption] = UNSET
    path: Union[Unset, None, List[ApiItemType]] = UNSET
    filter_: Union[Unset, None, "ApiFilterUpdate"] = UNSET
    include_test_jobs: Union[Unset, ApiAllowedOption] = UNSET
    include_executions: Union[Unset, ApiAllowedOption] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_type = self.item_type
        include_description: Union[Unset, str] = UNSET
        if not isinstance(self.include_description, Unset):
            include_description = self.include_description.value

        include_pictures: Union[Unset, str] = UNSET
        if not isinstance(self.include_pictures, Unset):
            include_pictures = self.include_pictures.value

        allow_to_show_hide_details = self.allow_to_show_hide_details
        include_history: Union[Unset, str] = UNSET
        if not isinstance(self.include_history, Unset):
            include_history = self.include_history.value

        include_attachments: Union[Unset, str] = UNSET
        if not isinstance(self.include_attachments, Unset):
            include_attachments = self.include_attachments.value

        show_related_defects: Union[Unset, str] = UNSET
        if not isinstance(self.show_related_defects, Unset):
            show_related_defects = self.show_related_defects.value

        show_related_requirements: Union[Unset, str] = UNSET
        if not isinstance(self.show_related_requirements, Unset):
            show_related_requirements = self.show_related_requirements.value

        show_related_test_cases: Union[Unset, str] = UNSET
        if not isinstance(self.show_related_test_cases, Unset):
            show_related_test_cases = self.show_related_test_cases.value

        show_related_test_scenarios: Union[Unset, str] = UNSET
        if not isinstance(self.show_related_test_scenarios, Unset):
            show_related_test_scenarios = self.show_related_test_scenarios.value

        include_jira_items: Union[Unset, str] = UNSET
        if not isinstance(self.include_jira_items, Unset):
            include_jira_items = self.include_jira_items.value

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

        include_test_jobs: Union[Unset, str] = UNSET
        if not isinstance(self.include_test_jobs, Unset):
            include_test_jobs = self.include_test_jobs.value

        include_executions: Union[Unset, str] = UNSET
        if not isinstance(self.include_executions, Unset):
            include_executions = self.include_executions.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ItemType": item_type,
            }
        )
        if include_description is not UNSET:
            field_dict["IncludeDescription"] = include_description
        if include_pictures is not UNSET:
            field_dict["IncludePictures"] = include_pictures
        if allow_to_show_hide_details is not UNSET:
            field_dict["AllowToShowHideDetails"] = allow_to_show_hide_details
        if include_history is not UNSET:
            field_dict["IncludeHistory"] = include_history
        if include_attachments is not UNSET:
            field_dict["IncludeAttachments"] = include_attachments
        if show_related_defects is not UNSET:
            field_dict["ShowRelatedDefects"] = show_related_defects
        if show_related_requirements is not UNSET:
            field_dict["ShowRelatedRequirements"] = show_related_requirements
        if show_related_test_cases is not UNSET:
            field_dict["ShowRelatedTestCases"] = show_related_test_cases
        if show_related_test_scenarios is not UNSET:
            field_dict["ShowRelatedTestScenarios"] = show_related_test_scenarios
        if include_jira_items is not UNSET:
            field_dict["IncludeJiraItems"] = include_jira_items
        if path is not UNSET:
            field_dict["Path"] = path
        if filter_ is not UNSET:
            field_dict["Filter"] = filter_
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

        _include_description = d.pop("IncludeDescription", UNSET)
        include_description: Union[Unset, ApiAllowedOption]
        if isinstance(_include_description, Unset):
            include_description = UNSET
        else:
            include_description = ApiAllowedOption(_include_description)

        _include_pictures = d.pop("IncludePictures", UNSET)
        include_pictures: Union[Unset, ApiAllowedOption]
        if isinstance(_include_pictures, Unset):
            include_pictures = UNSET
        else:
            include_pictures = ApiAllowedOption(_include_pictures)

        allow_to_show_hide_details = d.pop("AllowToShowHideDetails", UNSET)

        _include_history = d.pop("IncludeHistory", UNSET)
        include_history: Union[Unset, ApiAllowedOption]
        if isinstance(_include_history, Unset):
            include_history = UNSET
        else:
            include_history = ApiAllowedOption(_include_history)

        _include_attachments = d.pop("IncludeAttachments", UNSET)
        include_attachments: Union[Unset, ApiAllowedOption]
        if isinstance(_include_attachments, Unset):
            include_attachments = UNSET
        else:
            include_attachments = ApiAllowedOption(_include_attachments)

        _show_related_defects = d.pop("ShowRelatedDefects", UNSET)
        show_related_defects: Union[Unset, ApiAllowedOption]
        if isinstance(_show_related_defects, Unset):
            show_related_defects = UNSET
        else:
            show_related_defects = ApiAllowedOption(_show_related_defects)

        _show_related_requirements = d.pop("ShowRelatedRequirements", UNSET)
        show_related_requirements: Union[Unset, ApiAllowedOption]
        if isinstance(_show_related_requirements, Unset):
            show_related_requirements = UNSET
        else:
            show_related_requirements = ApiAllowedOption(_show_related_requirements)

        _show_related_test_cases = d.pop("ShowRelatedTestCases", UNSET)
        show_related_test_cases: Union[Unset, ApiAllowedOption]
        if isinstance(_show_related_test_cases, Unset):
            show_related_test_cases = UNSET
        else:
            show_related_test_cases = ApiAllowedOption(_show_related_test_cases)

        _show_related_test_scenarios = d.pop("ShowRelatedTestScenarios", UNSET)
        show_related_test_scenarios: Union[Unset, ApiAllowedOption]
        if isinstance(_show_related_test_scenarios, Unset):
            show_related_test_scenarios = UNSET
        else:
            show_related_test_scenarios = ApiAllowedOption(_show_related_test_scenarios)

        _include_jira_items = d.pop("IncludeJiraItems", UNSET)
        include_jira_items: Union[Unset, ApiAllowedOption]
        if isinstance(_include_jira_items, Unset):
            include_jira_items = UNSET
        else:
            include_jira_items = ApiAllowedOption(_include_jira_items)

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

        _include_test_jobs = d.pop("IncludeTestJobs", UNSET)
        include_test_jobs: Union[Unset, ApiAllowedOption]
        if isinstance(_include_test_jobs, Unset):
            include_test_jobs = UNSET
        else:
            include_test_jobs = ApiAllowedOption(_include_test_jobs)

        _include_executions = d.pop("IncludeExecutions", UNSET)
        include_executions: Union[Unset, ApiAllowedOption]
        if isinstance(_include_executions, Unset):
            include_executions = UNSET
        else:
            include_executions = ApiAllowedOption(_include_executions)

        api_test_scenario_report_allowed_options_update = cls(
            item_type=item_type,
            include_description=include_description,
            include_pictures=include_pictures,
            allow_to_show_hide_details=allow_to_show_hide_details,
            include_history=include_history,
            include_attachments=include_attachments,
            show_related_defects=show_related_defects,
            show_related_requirements=show_related_requirements,
            show_related_test_cases=show_related_test_cases,
            show_related_test_scenarios=show_related_test_scenarios,
            include_jira_items=include_jira_items,
            path=path,
            filter_=filter_,
            include_test_jobs=include_test_jobs,
            include_executions=include_executions,
        )

        api_test_scenario_report_allowed_options_update.additional_properties = d
        return api_test_scenario_report_allowed_options_update

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
