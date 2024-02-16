from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission import ApiPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDependenciesAddSinglePermissionPatchRequest")


@attr.s(auto_attribs=True)
class ApiDependenciesAddSinglePermissionPatchRequest:
    """
    Attributes:
        operation_type (str):
        all_permissions (Union[Unset, None, List[ApiPermission]]): List of permissions to validate.
        added_permission (Union[Unset, ApiPermission]): Represention of possible permissions.
            This enum has the following values:
              - `AGSprintCreateEditAll` Allows the user to create new sprints and edit existing ones.
              - `AGSprintDeleteAll` Allows the user to delete sprints.
              - `AGSprintPlanningAll` Allows the user to access the sprint planning.
              - `AGViewAll` Allows the user to see the agile board.
              - `DAChartEditPublicAll` Allows the user to change saved charts.
              - `DAChartPublishAll` Allows the user to save charts in the chart gallery.
              - `DAEditAll` Allows the user to add new charts or change visible charts.
              - `DAViewAll` Allows the user to see the dashboard.
              - `DFCreateAll` Allows the user to create new defects.
              - `DFCreateDependencyAll` Allows to create new defect dependencies.
              - `DFDeleteAll` Allows the user to delete all defects.
              - `DFDeleteAssigned` Allows the user to delete assigned defects.
              - `DFDeleteDependencyAll` Allows to delete existing defect dependencies.
              - `DFDeleteEnclosuresAll` Allows the user to delete enclosures of all defects.
              - `DFDeleteEnclosuresOwn` Allows the user to delete enclosures of own defects.
              - `DFDeleteOwn` Allows the user to delete own defects.
              - `DFEditAll` Allows the user to change all defects.
              - `DFEditAssigned` Allows the user to change assigned defects.
              - `DFEditBatchAll` Allows to batch change defects.
              - `DFEditEnclosuresAll` Allows the user to add or change enclosures, for all defects.
              - `DFEditEnclosuresOwn` Allows the user to add or change enclosures, for own defects.
              - `DFEditOwn` Allows the user to change own defects.
              - `DFMoveBetweenProjectsAll` Allows the user to move all defects between different projects.
              - `DFMoveBetweenProjectsAssigned` Allows the user to move assigned defects between different projects.
              - `DFMoveBetweenProjectsOwn` Allows the user to move own defects between different projects.
              - `DFMoveInProjectAll` Allows the user to move all defects within one project.
              - `DFMoveInProjectAssigned` Allows the user to move assigned defects within one project.
              - `DFMoveInProjectOwn` Allows the user to move own defects within one project.
              - `DFViewContentAll` Allows the user to open defects.
              - `EXFinalizeAll` Allows the user to finalize an execution.
              - `EXSchedulingAll` Allows the user to set up schedules for all regularly executed test scenarios.
              - `EXSchedulingAssigned` Allows the user to set up schedules for assigned regularly executed test scenarios.
              - `EXSchedulingOwn` Allows the user to set up schedules for own regularly executed test scenarios.
              - `EXSetRelevanceAll` Allows the user to mark and unmark executions as (ir)relevant.
              - `EXTCAutomatedAll` Allows the user to execute test cases which contain an automation.
              - `EXTCManualAll` Allows the user to manually execute test cases.
              - `EXTSAutomatedAll` Allows the user to execute test scenarios which contain an automation.
              - `EXTSManualAll` Allows the user to manually execute test scenarios.
              - `GEAttachmentsAddAll` Allows the user to add files.
              - `GEAttachmentsDeleteAll` Allows the user to delete attachments.
              - `GEAttachmentsViewOpenAll` Allows the user to open attached files.
              - `GEExportItemAll` Allows to export items.
              - `GEImportItemAll` Allows to import items.
              - `GEMindMapCreateEditAll` Allows the user to edit and create Mind Maps.
              - `GEMindMapViewAll` Allows the user to see Mind Maps.
              - `GENotificationsAll` Allows the user to configure notifications and receive them.
              - `GEProjectConfigureAll` Allows the user to add new projects and change configuration.
              - `GEProjectConfigureSubtemplateAll` Allows the user to configure the sub template of a project.
              - `GEProjectConfigureUsersAll` Allows the user to assign users to a project.
              - `GEProjectEditTreeAll` Allows the user to add sub folders to a project.
              - `GEProjectViewAllUsersAll` Allows the user to see all other users.
              - `GEViewsEditPublicAll` Allows the user to change public filtered views in project gallery.
              - `GEViewsPublishAll` Allows the user to publish saved filtered views in project gallery.
              - `PPCreateEditDeleteItemsAll` Allows the user to create / edit / delete items in the project plan.
              - `PPReportWorkAll` Allows the user to report work on items in the project plan.
              - `PPShowEarnedValueAnalysisAll` Allows the user to see the earned value analysis of a project plan.
              - `PPViewContentAll` Allows the user to open project plans.
              - `RPCreateTemplateEditLayoutAll` Allows the user to create new reports and edit existing ones.
              - `RPExportCSVAll` Allows the user to export reports to CSV format.
              - `RPExportDOCAll` Allows the user to export reports to DOC format.
              - `RPExportDOCXAll` Allows the user to export reports to DOCX format.
              - `RPExportHTMLAll` Allows the user to export reports to HTML format.
              - `RPExportImageFileAll` Allows the user to export reports to Image File.
              - `RPExportMHTAll` Allows the user to export reports to MHT format.
              - `RPExportODTAll` Allows the user to export reports to ODT format.
              - `RPExportPDFAll` Allows the user to export reports to PDF format.
              - `RPExportRTFAll` Allows the user to export reports to RTF format.
              - `RPExportTextFileAll` Allows the user to export reports to Text File.
              - `RPExportXLSAll` Allows the user to export reports to XLS format.
              - `RPExportXLSXAll` Allows the user to export reports to XLSX format.
              - `RPManageTemplatesAll` Allows to import/export report templates as well as to configure properties.
              - `RPSignPDFAll` Allows the user to sign reports which are exported as PDF.
              - `RPUseAll` Allows the user to see the reports.
              - `RQCreateDependencyAll` Allows to create new requirement dependencies.
              - `RQCreateEditCommentsAll` Allows the user to create comments in the description of the requirement.
              - `RQCreateEditFieldsDescriptionAll` Allows the user to create new requirements.
              - `RQCreateWordImportAll` Allows the user to import requirements from word.
              - `RQDeleteAll` Allows the user to delete all requirements.
              - `RQDeleteAssigned` Allows the user to delete assigned requirements.
              - `RQDeleteDependencyAll` Allows to delete existing requirement dependencies.
              - `RQDeleteOwn` Allows the user to delete own requirements.
              - `RQEditBatchAll` Allows to batch change requirements.
              - `RQEditCommentsAll` Allows the user to edit existing comments, for all requirements.
              - `RQEditCommentsAssigned` Allows the user to edit existing comments, for assigned requirements.
              - `RQEditCommentsOwn` Allows the user to edit existing comments, for own requirements.
              - `RQEditDescriptionAll` Allows the user to edit the description of a requirement, for all requirements.
              - `RQEditDescriptionAssigned` Allows the user to edit the description of a requirement, for assigned
            requirements.
              - `RQEditDescriptionOwn` Allows the user to edit the description of a requirement, for own requirements.
              - `RQEditFieldsAll` Allows the user to edit fields in the metadata, for all requirements.
              - `RQEditFieldsAssigned` Allows the user to edit fields in the metadata, for assigned requirements.
              - `RQEditFieldsOwn` Allows the user to edit fields in the metadata, for own requirements.
              - `RQEditStatusAll` Allows the user to change the status of a requirement, for all requirements.
              - `RQEditStatusAssigned` Allows the user to change the status of a requirement, for assigned requirements.
              - `RQEditStatusOwn` Allows the user to change the status of a requirement, for own requirements.
              - `RQEditWordImportAll` Allows to import a description from a Word-File, for all requirements.
              - `RQEditWordImportAssigned` Allows to import a description from a Word-File, for assigned requirements.
              - `RQEditWordImportOwn` Allows to import a description from a Word-File, for own requirements.
              - `RQMoveBetweenProjectsAll` Allows the user to move all requirements between different projects.
              - `RQMoveBetweenProjectsAssigned` Allows the user to move assigned requirements between different projects.
              - `RQMoveBetweenProjectsOwn` Allows the user to move own requirements between different projects.
              - `RQMoveInProjectAll` Allows the user to move all requirements within one project.
              - `RQMoveInProjectAssigned` Allows the user to move assigned requirements within one project.
              - `RQMoveInProjectOwn` Allows the user to move own requirements within one project.
              - `RQViewContentAll` Allows the user to open requirements.
              - `RQViewDiscussionsAll` Allows the user to open UMLs, for all requirements.
              - `RQViewWordExportAll` Allows the user to export all requirements to a Word document.
              - `RQViewWordExportAssigned` Allows the user to export assigned requirements to a Word document.
              - `RQViewWordExportOwn` Allows the user to export own requirements to a Word document.
              - `SCCreateAll` Allows the user to create new scripts.
              - `SCCreateDependencyAll` Allows to create new script dependencies.
              - `SCDeleteAll` Allows the user to delete all scripts.
              - `SCDeleteAssigned` Allows the user to delete assigned scripts.
              - `SCDeleteDependencyAll` Allows to delete existing script dependencies.
              - `SCDeleteOwn` Allows the user to delete own scripts.
              - `SCEditAll` Allows the user to edit all scripts.
              - `SCEditAssigned` Allows the user to edit assigned scripts.
              - `SCEditBatchAll` Allows to batch change scripts.
              - `SCEditOwn` Allows the user to edit own scripts.
              - `SCMoveBetweenProjectsAll` Allows the user to move all scripts between different projects.
              - `SCMoveBetweenProjectsAssigned` Allows the user to move assigned scripts between different projects.
              - `SCMoveBetweenProjectsOwn` Allows the user to move own scripts between different projects.
              - `SCMoveInProjectAll` Allows the user to move all scripts within one project.
              - `SCMoveInProjectAssigned` Allows the user to move assigned scripts within one project.
              - `SCMoveInProjectOwn` Allows the user to move own scripts within one project.
              - `SCViewContentAll` Allows the user to open scripts.
              - `TCCreateDependencyAll` Allows to create new test case dependencies.
              - `TCCreateEditFieldsDescriptionAll` Allows the user to create new test case.
              - `TCCreateEditNestingAll` Allows the user to nest a test case within a test step.
              - `TCCreateEditTestAutomationAll` Allows the user to use the automation tab to add new scripts.
              - `TCCreateEditVariablesAll` Allows the user to parameterize tests using the variable manager.
              - `TCDeleteAll` Allows the user to delete all test cases.
              - `TCDeleteAssigned` Allows the user to delete assigned test cases.
              - `TCDeleteDependencyAll` Allows to delete existing test case dependencies.
              - `TCDeleteOwn` Allows the user to delete own test cases.
              - `TCEditBatchAll` Allows to batch change test cases.
              - `TCEditFieldDescriptionAll` Allows the user to edit fields in the metadata and the description, for all test
            cases.
              - `TCEditFieldDescriptionAssigned` Allows the user to edit fields in the metadata and the description, for
            assigned test cases.
              - `TCEditFieldDescriptionOwn` Allows the user to edit fields in the metadata and the description, for own test
            cases.
              - `TCEditNestingAll` Allows the user to change nested test cases, for all test cases.
              - `TCEditNestingAssigned` Allows the user to change nested test cases, for assigned test cases.
              - `TCEditNestingOwn` Allows the user to change nested test cases, for own test cases.
              - `TCEditStatusAll` Allows the user to change the status of all test cases.
              - `TCEditStatusAssigned` Allows the user to change the status of assigned test cases.
              - `TCEditStatusOwn` Allows the user to change the status of own test cases.
              - `TCEditStepsAll` Allows the user to use the step designer, for all test cases.
              - `TCEditStepsAssigned` Allows the user to use the step designer, for assigned test cases.
              - `TCEditStepsOwn` Allows the user to use the step designer, for own test cases.
              - `TCEditTestAutomationAll` Allows the user to change test scripts in test steps, for all test cases.
              - `TCEditTestAutomationAssigned` Allows the user to change test scripts in test steps, for assigned test
            cases.
              - `TCEditTestAutomationOwn` Allows the user to change test scripts in test steps, for own test cases.
              - `TCEditVariablesAll` Allows the user to change variables in variable manager, for all test cases.
              - `TCEditVariablesAssigned` Allows the user to change variables in variable manager, for assigned test cases.
              - `TCEditVariablesOwn` Allows the user to change variables in variable manager, for own test cases.
              - `TCMoveBetweenProjectsAll` Allows the user to move all test cases between different projects.
              - `TCMoveBetweenProjectsAssigned` Allows the user to move assigned test cases between different projects.
              - `TCMoveBetweenProjectsOwn` Allows the user to move own test cases between different projects.
              - `TCMoveInProjectAll` Allows the user to move all test cases within one project.
              - `TCMoveInProjectAssigned` Allows the user to move assigned test cases within one project.
              - `TCMoveInProjectOwn` Allows the user to move own test cases within one project.
              - `TCViewContentAll` Allows the user to open test cases.
              - `TSCreateAll` Allows the user to create new test scenarios.
              - `TSCreateDependencyAll` Allows to create new dependencies, for test scenarios.
              - `TSDeleteAll` Allows the user to delete all test scenarios.
              - `TSDeleteAssigned` Allows the user to delete assigned test scenarios.
              - `TSDeleteDependencyAll` Allows to delete existing dependencies, for test scenarios.
              - `TSDeleteOwn` Allows the user to delete own test scenarios.
              - `TSEditAll` Allows the user to change all test scenarios.
              - `TSEditAssigned` Allows the user to change assigned test scenarios.
              - `TSEditBatchAll` Allows to batch change test scenarios.
              - `TSEditOwn` Allows the user to change own test scenarios.
              - `TSMoveBetweenProjectsAll` Allows the user to move all test scenarios between different projects.
              - `TSMoveBetweenProjectsAssigned` Allows the user to move assigned test scenarios between different projects.
              - `TSMoveBetweenProjectsOwn` Allows the user to move own test scenarios between different projects.
              - `TSMoveInProjectAll` Allows the user to move all test scenarios within one project.
              - `TSMoveInProjectAssigned` Allows the user to move assigned test scenarios within one project.
              - `TSMoveInProjectOwn` Allows the user to move own test scenarios within one project.
              - `TSViewContentAll` Allows the user to open test scenarios.
    """

    operation_type: str
    all_permissions: Union[Unset, None, List[ApiPermission]] = UNSET
    added_permission: Union[Unset, ApiPermission] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        all_permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.all_permissions, Unset):
            if self.all_permissions is None:
                all_permissions = None
            else:
                all_permissions = []
                for all_permissions_item_data in self.all_permissions:
                    all_permissions_item = all_permissions_item_data.value

                    all_permissions.append(all_permissions_item)

        added_permission: Union[Unset, str] = UNSET
        if not isinstance(self.added_permission, Unset):
            added_permission = self.added_permission.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if all_permissions is not UNSET:
            field_dict["AllPermissions"] = all_permissions
        if added_permission is not UNSET:
            field_dict["AddedPermission"] = added_permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        all_permissions = []
        _all_permissions = d.pop("AllPermissions", UNSET)
        for all_permissions_item_data in _all_permissions or []:
            all_permissions_item = ApiPermission(all_permissions_item_data)

            all_permissions.append(all_permissions_item)

        _added_permission = d.pop("AddedPermission", UNSET)
        added_permission: Union[Unset, ApiPermission]
        if isinstance(_added_permission, Unset):
            added_permission = UNSET
        else:
            added_permission = ApiPermission(_added_permission)

        api_dependencies_add_single_permission_patch_request = cls(
            operation_type=operation_type,
            all_permissions=all_permissions,
            added_permission=added_permission,
        )

        api_dependencies_add_single_permission_patch_request.additional_properties = d
        return api_dependencies_add_single_permission_patch_request

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
