from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_allowed_option import ApiAllowedOption
from ..models.api_item_type import ApiItemType
from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_filter import ApiFilter


T = TypeVar("T", bound="ApiBaseObjectReportAllowedOptions")


@attr.s(auto_attribs=True)
class ApiBaseObjectReportAllowedOptions:
    """Represents the report allowed options.
    Please note this model represent options as set by user when editing report options.
    Please do not confuse with so called "actual" report options, used when user generates the report.
    The main difference is that allowed options contain three-state values: always/user decides/never
    whilst actual options contain the actual selection: true/false.

        Attributes:
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
            path (Union[Unset, None, List[ApiItemType]]): The path of the options.
            filter_ (Union[Unset, None, ApiFilter]): Represents the filter.
            data_allowed (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
    """

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
    item_type: Union[Unset, ApiItemType] = UNSET
    path: Union[Unset, None, List[ApiItemType]] = UNSET
    filter_: Union[Unset, None, "ApiFilter"] = UNSET
    data_allowed: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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

        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

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

        data_allowed: Union[Unset, str] = UNSET
        if not isinstance(self.data_allowed, Unset):
            data_allowed = self.data_allowed.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
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
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if path is not UNSET:
            field_dict["Path"] = path
        if filter_ is not UNSET:
            field_dict["Filter"] = filter_
        if data_allowed is not UNSET:
            field_dict["DataAllowed"] = data_allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_filter import ApiFilter

        d = src_dict.copy()
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

        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        path = []
        _path = d.pop("Path", UNSET)
        for path_item_data in _path or []:
            path_item = ApiItemType(path_item_data)

            path.append(path_item)

        _filter_ = d.pop("Filter", UNSET)
        filter_: Union[Unset, None, ApiFilter]
        if _filter_ is None:
            filter_ = None
        elif isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ApiFilter.from_dict(_filter_)

        _data_allowed = d.pop("DataAllowed", UNSET)
        data_allowed: Union[Unset, ApiPermissionResult]
        if isinstance(_data_allowed, Unset):
            data_allowed = UNSET
        else:
            data_allowed = ApiPermissionResult(_data_allowed)

        api_base_object_report_allowed_options = cls(
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
            item_type=item_type,
            path=path,
            filter_=filter_,
            data_allowed=data_allowed,
        )

        return api_base_object_report_allowed_options
