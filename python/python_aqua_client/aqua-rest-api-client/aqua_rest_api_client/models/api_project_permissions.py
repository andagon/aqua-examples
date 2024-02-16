from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectPermissions")


@attr.s(auto_attribs=True)
class ApiProjectPermissions:
    """Represents permissions in a project. Includes only project-level permissions.
    For permissions that can be defined on folder level (e.g. permissions to create items)
    please refer to ApiProjectFolderPermissions (this also included a project's root-folder permissions).

        Attributes:
            can_configure_project (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_use_notifications (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_edit_public_user_view (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_publish_user_view (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_view_report_definitions (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_create_report_definition (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
                check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_import_report_definition (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
                check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_configure_project_template (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
                check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_configure_project_workflows (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
                check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_manage_project_users (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_configure_default_notification_rules (Union[Unset, ApiPermissionResult]): Defined possible results of a
                permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_configure_notification_templates (Union[Unset, ApiPermissionResult]): Defined possible results of a
                permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_view_agents (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_manage_agents (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_add_dependency_any_subfolder (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
                check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_view_agile_board (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_create_edit_sprints (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_delete_sprints (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_plan_sprints (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
    """

    can_configure_project: Union[Unset, ApiPermissionResult] = UNSET
    can_use_notifications: Union[Unset, ApiPermissionResult] = UNSET
    can_edit_public_user_view: Union[Unset, ApiPermissionResult] = UNSET
    can_publish_user_view: Union[Unset, ApiPermissionResult] = UNSET
    can_view_report_definitions: Union[Unset, ApiPermissionResult] = UNSET
    can_create_report_definition: Union[Unset, ApiPermissionResult] = UNSET
    can_import_report_definition: Union[Unset, ApiPermissionResult] = UNSET
    can_configure_project_template: Union[Unset, ApiPermissionResult] = UNSET
    can_configure_project_workflows: Union[Unset, ApiPermissionResult] = UNSET
    can_manage_project_users: Union[Unset, ApiPermissionResult] = UNSET
    can_configure_default_notification_rules: Union[Unset, ApiPermissionResult] = UNSET
    can_configure_notification_templates: Union[Unset, ApiPermissionResult] = UNSET
    can_view_agents: Union[Unset, ApiPermissionResult] = UNSET
    can_manage_agents: Union[Unset, ApiPermissionResult] = UNSET
    can_add_dependency_any_subfolder: Union[Unset, ApiPermissionResult] = UNSET
    can_view_agile_board: Union[Unset, ApiPermissionResult] = UNSET
    can_create_edit_sprints: Union[Unset, ApiPermissionResult] = UNSET
    can_delete_sprints: Union[Unset, ApiPermissionResult] = UNSET
    can_plan_sprints: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_configure_project: Union[Unset, str] = UNSET
        if not isinstance(self.can_configure_project, Unset):
            can_configure_project = self.can_configure_project.value

        can_use_notifications: Union[Unset, str] = UNSET
        if not isinstance(self.can_use_notifications, Unset):
            can_use_notifications = self.can_use_notifications.value

        can_edit_public_user_view: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit_public_user_view, Unset):
            can_edit_public_user_view = self.can_edit_public_user_view.value

        can_publish_user_view: Union[Unset, str] = UNSET
        if not isinstance(self.can_publish_user_view, Unset):
            can_publish_user_view = self.can_publish_user_view.value

        can_view_report_definitions: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_report_definitions, Unset):
            can_view_report_definitions = self.can_view_report_definitions.value

        can_create_report_definition: Union[Unset, str] = UNSET
        if not isinstance(self.can_create_report_definition, Unset):
            can_create_report_definition = self.can_create_report_definition.value

        can_import_report_definition: Union[Unset, str] = UNSET
        if not isinstance(self.can_import_report_definition, Unset):
            can_import_report_definition = self.can_import_report_definition.value

        can_configure_project_template: Union[Unset, str] = UNSET
        if not isinstance(self.can_configure_project_template, Unset):
            can_configure_project_template = self.can_configure_project_template.value

        can_configure_project_workflows: Union[Unset, str] = UNSET
        if not isinstance(self.can_configure_project_workflows, Unset):
            can_configure_project_workflows = self.can_configure_project_workflows.value

        can_manage_project_users: Union[Unset, str] = UNSET
        if not isinstance(self.can_manage_project_users, Unset):
            can_manage_project_users = self.can_manage_project_users.value

        can_configure_default_notification_rules: Union[Unset, str] = UNSET
        if not isinstance(self.can_configure_default_notification_rules, Unset):
            can_configure_default_notification_rules = self.can_configure_default_notification_rules.value

        can_configure_notification_templates: Union[Unset, str] = UNSET
        if not isinstance(self.can_configure_notification_templates, Unset):
            can_configure_notification_templates = self.can_configure_notification_templates.value

        can_view_agents: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_agents, Unset):
            can_view_agents = self.can_view_agents.value

        can_manage_agents: Union[Unset, str] = UNSET
        if not isinstance(self.can_manage_agents, Unset):
            can_manage_agents = self.can_manage_agents.value

        can_add_dependency_any_subfolder: Union[Unset, str] = UNSET
        if not isinstance(self.can_add_dependency_any_subfolder, Unset):
            can_add_dependency_any_subfolder = self.can_add_dependency_any_subfolder.value

        can_view_agile_board: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_agile_board, Unset):
            can_view_agile_board = self.can_view_agile_board.value

        can_create_edit_sprints: Union[Unset, str] = UNSET
        if not isinstance(self.can_create_edit_sprints, Unset):
            can_create_edit_sprints = self.can_create_edit_sprints.value

        can_delete_sprints: Union[Unset, str] = UNSET
        if not isinstance(self.can_delete_sprints, Unset):
            can_delete_sprints = self.can_delete_sprints.value

        can_plan_sprints: Union[Unset, str] = UNSET
        if not isinstance(self.can_plan_sprints, Unset):
            can_plan_sprints = self.can_plan_sprints.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_configure_project is not UNSET:
            field_dict["CanConfigureProject"] = can_configure_project
        if can_use_notifications is not UNSET:
            field_dict["CanUseNotifications"] = can_use_notifications
        if can_edit_public_user_view is not UNSET:
            field_dict["CanEditPublicUserView"] = can_edit_public_user_view
        if can_publish_user_view is not UNSET:
            field_dict["CanPublishUserView"] = can_publish_user_view
        if can_view_report_definitions is not UNSET:
            field_dict["CanViewReportDefinitions"] = can_view_report_definitions
        if can_create_report_definition is not UNSET:
            field_dict["CanCreateReportDefinition"] = can_create_report_definition
        if can_import_report_definition is not UNSET:
            field_dict["CanImportReportDefinition"] = can_import_report_definition
        if can_configure_project_template is not UNSET:
            field_dict["CanConfigureProjectTemplate"] = can_configure_project_template
        if can_configure_project_workflows is not UNSET:
            field_dict["CanConfigureProjectWorkflows"] = can_configure_project_workflows
        if can_manage_project_users is not UNSET:
            field_dict["CanManageProjectUsers"] = can_manage_project_users
        if can_configure_default_notification_rules is not UNSET:
            field_dict["CanConfigureDefaultNotificationRules"] = can_configure_default_notification_rules
        if can_configure_notification_templates is not UNSET:
            field_dict["CanConfigureNotificationTemplates"] = can_configure_notification_templates
        if can_view_agents is not UNSET:
            field_dict["CanViewAgents"] = can_view_agents
        if can_manage_agents is not UNSET:
            field_dict["CanManageAgents"] = can_manage_agents
        if can_add_dependency_any_subfolder is not UNSET:
            field_dict["CanAddDependencyAnySubfolder"] = can_add_dependency_any_subfolder
        if can_view_agile_board is not UNSET:
            field_dict["CanViewAgileBoard"] = can_view_agile_board
        if can_create_edit_sprints is not UNSET:
            field_dict["CanCreateEditSprints"] = can_create_edit_sprints
        if can_delete_sprints is not UNSET:
            field_dict["CanDeleteSprints"] = can_delete_sprints
        if can_plan_sprints is not UNSET:
            field_dict["CanPlanSprints"] = can_plan_sprints

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _can_configure_project = d.pop("CanConfigureProject", UNSET)
        can_configure_project: Union[Unset, ApiPermissionResult]
        if isinstance(_can_configure_project, Unset):
            can_configure_project = UNSET
        else:
            can_configure_project = ApiPermissionResult(_can_configure_project)

        _can_use_notifications = d.pop("CanUseNotifications", UNSET)
        can_use_notifications: Union[Unset, ApiPermissionResult]
        if isinstance(_can_use_notifications, Unset):
            can_use_notifications = UNSET
        else:
            can_use_notifications = ApiPermissionResult(_can_use_notifications)

        _can_edit_public_user_view = d.pop("CanEditPublicUserView", UNSET)
        can_edit_public_user_view: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit_public_user_view, Unset):
            can_edit_public_user_view = UNSET
        else:
            can_edit_public_user_view = ApiPermissionResult(_can_edit_public_user_view)

        _can_publish_user_view = d.pop("CanPublishUserView", UNSET)
        can_publish_user_view: Union[Unset, ApiPermissionResult]
        if isinstance(_can_publish_user_view, Unset):
            can_publish_user_view = UNSET
        else:
            can_publish_user_view = ApiPermissionResult(_can_publish_user_view)

        _can_view_report_definitions = d.pop("CanViewReportDefinitions", UNSET)
        can_view_report_definitions: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_report_definitions, Unset):
            can_view_report_definitions = UNSET
        else:
            can_view_report_definitions = ApiPermissionResult(_can_view_report_definitions)

        _can_create_report_definition = d.pop("CanCreateReportDefinition", UNSET)
        can_create_report_definition: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create_report_definition, Unset):
            can_create_report_definition = UNSET
        else:
            can_create_report_definition = ApiPermissionResult(_can_create_report_definition)

        _can_import_report_definition = d.pop("CanImportReportDefinition", UNSET)
        can_import_report_definition: Union[Unset, ApiPermissionResult]
        if isinstance(_can_import_report_definition, Unset):
            can_import_report_definition = UNSET
        else:
            can_import_report_definition = ApiPermissionResult(_can_import_report_definition)

        _can_configure_project_template = d.pop("CanConfigureProjectTemplate", UNSET)
        can_configure_project_template: Union[Unset, ApiPermissionResult]
        if isinstance(_can_configure_project_template, Unset):
            can_configure_project_template = UNSET
        else:
            can_configure_project_template = ApiPermissionResult(_can_configure_project_template)

        _can_configure_project_workflows = d.pop("CanConfigureProjectWorkflows", UNSET)
        can_configure_project_workflows: Union[Unset, ApiPermissionResult]
        if isinstance(_can_configure_project_workflows, Unset):
            can_configure_project_workflows = UNSET
        else:
            can_configure_project_workflows = ApiPermissionResult(_can_configure_project_workflows)

        _can_manage_project_users = d.pop("CanManageProjectUsers", UNSET)
        can_manage_project_users: Union[Unset, ApiPermissionResult]
        if isinstance(_can_manage_project_users, Unset):
            can_manage_project_users = UNSET
        else:
            can_manage_project_users = ApiPermissionResult(_can_manage_project_users)

        _can_configure_default_notification_rules = d.pop("CanConfigureDefaultNotificationRules", UNSET)
        can_configure_default_notification_rules: Union[Unset, ApiPermissionResult]
        if isinstance(_can_configure_default_notification_rules, Unset):
            can_configure_default_notification_rules = UNSET
        else:
            can_configure_default_notification_rules = ApiPermissionResult(_can_configure_default_notification_rules)

        _can_configure_notification_templates = d.pop("CanConfigureNotificationTemplates", UNSET)
        can_configure_notification_templates: Union[Unset, ApiPermissionResult]
        if isinstance(_can_configure_notification_templates, Unset):
            can_configure_notification_templates = UNSET
        else:
            can_configure_notification_templates = ApiPermissionResult(_can_configure_notification_templates)

        _can_view_agents = d.pop("CanViewAgents", UNSET)
        can_view_agents: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_agents, Unset):
            can_view_agents = UNSET
        else:
            can_view_agents = ApiPermissionResult(_can_view_agents)

        _can_manage_agents = d.pop("CanManageAgents", UNSET)
        can_manage_agents: Union[Unset, ApiPermissionResult]
        if isinstance(_can_manage_agents, Unset):
            can_manage_agents = UNSET
        else:
            can_manage_agents = ApiPermissionResult(_can_manage_agents)

        _can_add_dependency_any_subfolder = d.pop("CanAddDependencyAnySubfolder", UNSET)
        can_add_dependency_any_subfolder: Union[Unset, ApiPermissionResult]
        if isinstance(_can_add_dependency_any_subfolder, Unset):
            can_add_dependency_any_subfolder = UNSET
        else:
            can_add_dependency_any_subfolder = ApiPermissionResult(_can_add_dependency_any_subfolder)

        _can_view_agile_board = d.pop("CanViewAgileBoard", UNSET)
        can_view_agile_board: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_agile_board, Unset):
            can_view_agile_board = UNSET
        else:
            can_view_agile_board = ApiPermissionResult(_can_view_agile_board)

        _can_create_edit_sprints = d.pop("CanCreateEditSprints", UNSET)
        can_create_edit_sprints: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create_edit_sprints, Unset):
            can_create_edit_sprints = UNSET
        else:
            can_create_edit_sprints = ApiPermissionResult(_can_create_edit_sprints)

        _can_delete_sprints = d.pop("CanDeleteSprints", UNSET)
        can_delete_sprints: Union[Unset, ApiPermissionResult]
        if isinstance(_can_delete_sprints, Unset):
            can_delete_sprints = UNSET
        else:
            can_delete_sprints = ApiPermissionResult(_can_delete_sprints)

        _can_plan_sprints = d.pop("CanPlanSprints", UNSET)
        can_plan_sprints: Union[Unset, ApiPermissionResult]
        if isinstance(_can_plan_sprints, Unset):
            can_plan_sprints = UNSET
        else:
            can_plan_sprints = ApiPermissionResult(_can_plan_sprints)

        api_project_permissions = cls(
            can_configure_project=can_configure_project,
            can_use_notifications=can_use_notifications,
            can_edit_public_user_view=can_edit_public_user_view,
            can_publish_user_view=can_publish_user_view,
            can_view_report_definitions=can_view_report_definitions,
            can_create_report_definition=can_create_report_definition,
            can_import_report_definition=can_import_report_definition,
            can_configure_project_template=can_configure_project_template,
            can_configure_project_workflows=can_configure_project_workflows,
            can_manage_project_users=can_manage_project_users,
            can_configure_default_notification_rules=can_configure_default_notification_rules,
            can_configure_notification_templates=can_configure_notification_templates,
            can_view_agents=can_view_agents,
            can_manage_agents=can_manage_agents,
            can_add_dependency_any_subfolder=can_add_dependency_any_subfolder,
            can_view_agile_board=can_view_agile_board,
            can_create_edit_sprints=can_create_edit_sprints,
            can_delete_sprints=can_delete_sprints,
            can_plan_sprints=can_plan_sprints,
        )

        return api_project_permissions
