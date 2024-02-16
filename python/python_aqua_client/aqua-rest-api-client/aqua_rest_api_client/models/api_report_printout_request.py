from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_object_report_options import ApiBaseObjectReportOptions
    from ..models.api_report_parameter_value import ApiReportParameterValue


T = TypeVar("T", bound="ApiReportPrintoutRequest")


@attr.s(auto_attribs=True)
class ApiReportPrintoutRequest:
    """Contains data required to generate a report printout.

    Attributes:
        report_id (Union[Unset, int]): ID of the report to generate.
        project_id (Union[Unset, int]): Id of the project where data (and report is located).
        folder_id (Union[Unset, int]): Id of the folder (zero means root folder).
        recursive (Union[Unset, bool]): If true, the report contains includes data from selected folder and all folders
            below.
            If false generated report contains data only from selected folder.
        report_options (Union[Unset, List['ApiBaseObjectReportOptions']]): Flat list of report options for corresponding
            levels (level is identified by Path property).
            Depending on item type the list of options varies (see subclasses of ApiBaseObjectReportOptions).
        include_archived (Union[Unset, bool]): If true the report includes archived data as well.
        related_projects (Union[Unset, None, List[int]]): Can be null. If not null then contains list of "related
            projects" (project sharing the same template
            as "main" project, specified in ProjectId) to fetch data from. Please note it make no sense
            to use FolderId other than zero in case when RelatedProjects are specified.
        parameter_values (Union[Unset, None, List['ApiReportParameterValue']]): Actual value for report parameters.
    """

    report_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    folder_id: Union[Unset, int] = UNSET
    recursive: Union[Unset, bool] = UNSET
    report_options: Union[Unset, List["ApiBaseObjectReportOptions"]] = UNSET
    include_archived: Union[Unset, bool] = UNSET
    related_projects: Union[Unset, None, List[int]] = UNSET
    parameter_values: Union[Unset, None, List["ApiReportParameterValue"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        report_id = self.report_id
        project_id = self.project_id
        folder_id = self.folder_id
        recursive = self.recursive
        report_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.report_options, Unset):
            report_options = []
            for report_options_item_data in self.report_options:
                report_options_item = report_options_item_data.to_dict()

                report_options.append(report_options_item)

        include_archived = self.include_archived
        related_projects: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.related_projects, Unset):
            if self.related_projects is None:
                related_projects = None
            else:
                related_projects = self.related_projects

        parameter_values: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameter_values, Unset):
            if self.parameter_values is None:
                parameter_values = None
            else:
                parameter_values = []
                for parameter_values_item_data in self.parameter_values:
                    parameter_values_item = parameter_values_item_data.to_dict()

                    parameter_values.append(parameter_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if report_id is not UNSET:
            field_dict["ReportId"] = report_id
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if recursive is not UNSET:
            field_dict["Recursive"] = recursive
        if report_options is not UNSET:
            field_dict["ReportOptions"] = report_options
        if include_archived is not UNSET:
            field_dict["IncludeArchived"] = include_archived
        if related_projects is not UNSET:
            field_dict["RelatedProjects"] = related_projects
        if parameter_values is not UNSET:
            field_dict["ParameterValues"] = parameter_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_object_report_options import ApiBaseObjectReportOptions
        from ..models.api_report_parameter_value import ApiReportParameterValue

        d = src_dict.copy()
        report_id = d.pop("ReportId", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        recursive = d.pop("Recursive", UNSET)

        report_options = []
        _report_options = d.pop("ReportOptions", UNSET)
        for report_options_item_data in _report_options or []:
            report_options_item = ApiBaseObjectReportOptions.from_dict(report_options_item_data)

            report_options.append(report_options_item)

        include_archived = d.pop("IncludeArchived", UNSET)

        related_projects = cast(List[int], d.pop("RelatedProjects", UNSET))

        parameter_values = []
        _parameter_values = d.pop("ParameterValues", UNSET)
        for parameter_values_item_data in _parameter_values or []:
            parameter_values_item = ApiReportParameterValue.from_dict(parameter_values_item_data)

            parameter_values.append(parameter_values_item)

        api_report_printout_request = cls(
            report_id=report_id,
            project_id=project_id,
            folder_id=folder_id,
            recursive=recursive,
            report_options=report_options,
            include_archived=include_archived,
            related_projects=related_projects,
            parameter_values=parameter_values,
        )

        return api_report_printout_request
