from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_id_name import ApiProjectIdName
    from ..models.api_project_notification_template import ApiProjectNotificationTemplate


T = TypeVar("T", bound="ApiProjectNotificationTemplates")


@attr.s(auto_attribs=True)
class ApiProjectNotificationTemplates:
    """Contains the notification templates of a specific project togehter with
    some meta information.

        Attributes:
            project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
            is_shared (Union[Unset, bool]): Indicates whether the project configuration is shared with
                a different project.
            is_owned (Union[Unset, bool]): Indicates whether the project configuration is owned by the
                project for which this part of the configuration was requested.
            owning_project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
            templates (Union[Unset, None, List['ApiProjectNotificationTemplate']]): The notification templates.
    """

    project: Union[Unset, None, "ApiProjectIdName"] = UNSET
    is_shared: Union[Unset, bool] = UNSET
    is_owned: Union[Unset, bool] = UNSET
    owning_project: Union[Unset, None, "ApiProjectIdName"] = UNSET
    templates: Union[Unset, None, List["ApiProjectNotificationTemplate"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict() if self.project else None

        is_shared = self.is_shared
        is_owned = self.is_owned
        owning_project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owning_project, Unset):
            owning_project = self.owning_project.to_dict() if self.owning_project else None

        templates: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.templates, Unset):
            if self.templates is None:
                templates = None
            else:
                templates = []
                for templates_item_data in self.templates:
                    templates_item = templates_item_data.to_dict()

                    templates.append(templates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project is not UNSET:
            field_dict["Project"] = project
        if is_shared is not UNSET:
            field_dict["IsShared"] = is_shared
        if is_owned is not UNSET:
            field_dict["IsOwned"] = is_owned
        if owning_project is not UNSET:
            field_dict["OwningProject"] = owning_project
        if templates is not UNSET:
            field_dict["Templates"] = templates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_id_name import ApiProjectIdName
        from ..models.api_project_notification_template import ApiProjectNotificationTemplate

        d = src_dict.copy()
        _project = d.pop("Project", UNSET)
        project: Union[Unset, None, ApiProjectIdName]
        if _project is None:
            project = None
        elif isinstance(_project, Unset):
            project = UNSET
        else:
            project = ApiProjectIdName.from_dict(_project)

        is_shared = d.pop("IsShared", UNSET)

        is_owned = d.pop("IsOwned", UNSET)

        _owning_project = d.pop("OwningProject", UNSET)
        owning_project: Union[Unset, None, ApiProjectIdName]
        if _owning_project is None:
            owning_project = None
        elif isinstance(_owning_project, Unset):
            owning_project = UNSET
        else:
            owning_project = ApiProjectIdName.from_dict(_owning_project)

        templates = []
        _templates = d.pop("Templates", UNSET)
        for templates_item_data in _templates or []:
            templates_item = ApiProjectNotificationTemplate.from_dict(templates_item_data)

            templates.append(templates_item)

        api_project_notification_templates = cls(
            project=project,
            is_shared=is_shared,
            is_owned=is_owned,
            owning_project=owning_project,
            templates=templates,
        )

        return api_project_notification_templates
