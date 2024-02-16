from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_type_is_web_layout_info import ApiItemTypeIsWebLayoutInfo
    from ..models.api_project_id_name import ApiProjectIdName


T = TypeVar("T", bound="ApiProjectTemplateInformation")


@attr.s(auto_attribs=True)
class ApiProjectTemplateInformation:
    """Contains the meta-information of a project template.

    Attributes:
        affected_projects (Union[Unset, None, List['ApiProjectIdName']]): List of projects which share the template.
        api_item_type_is_web_layout (Union[Unset, None, List['ApiItemTypeIsWebLayoutInfo']]): List which indicates for
            each item type whether the layout was created in web client.
        project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
        is_shared (Union[Unset, bool]): Indicates whether the project configuration is shared with
            a different project.
        is_owned (Union[Unset, bool]): Indicates whether the project configuration is owned by the
            project for which this part of the configuration was requested.
        owning_project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
    """

    affected_projects: Union[Unset, None, List["ApiProjectIdName"]] = UNSET
    api_item_type_is_web_layout: Union[Unset, None, List["ApiItemTypeIsWebLayoutInfo"]] = UNSET
    project: Union[Unset, None, "ApiProjectIdName"] = UNSET
    is_shared: Union[Unset, bool] = UNSET
    is_owned: Union[Unset, bool] = UNSET
    owning_project: Union[Unset, None, "ApiProjectIdName"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        affected_projects: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.affected_projects, Unset):
            if self.affected_projects is None:
                affected_projects = None
            else:
                affected_projects = []
                for affected_projects_item_data in self.affected_projects:
                    affected_projects_item = affected_projects_item_data.to_dict()

                    affected_projects.append(affected_projects_item)

        api_item_type_is_web_layout: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.api_item_type_is_web_layout, Unset):
            if self.api_item_type_is_web_layout is None:
                api_item_type_is_web_layout = None
            else:
                api_item_type_is_web_layout = []
                for api_item_type_is_web_layout_item_data in self.api_item_type_is_web_layout:
                    api_item_type_is_web_layout_item = api_item_type_is_web_layout_item_data.to_dict()

                    api_item_type_is_web_layout.append(api_item_type_is_web_layout_item)

        project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict() if self.project else None

        is_shared = self.is_shared
        is_owned = self.is_owned
        owning_project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owning_project, Unset):
            owning_project = self.owning_project.to_dict() if self.owning_project else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if affected_projects is not UNSET:
            field_dict["AffectedProjects"] = affected_projects
        if api_item_type_is_web_layout is not UNSET:
            field_dict["ApiItemTypeIsWebLayout"] = api_item_type_is_web_layout
        if project is not UNSET:
            field_dict["Project"] = project
        if is_shared is not UNSET:
            field_dict["IsShared"] = is_shared
        if is_owned is not UNSET:
            field_dict["IsOwned"] = is_owned
        if owning_project is not UNSET:
            field_dict["OwningProject"] = owning_project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_type_is_web_layout_info import ApiItemTypeIsWebLayoutInfo
        from ..models.api_project_id_name import ApiProjectIdName

        d = src_dict.copy()
        affected_projects = []
        _affected_projects = d.pop("AffectedProjects", UNSET)
        for affected_projects_item_data in _affected_projects or []:
            affected_projects_item = ApiProjectIdName.from_dict(affected_projects_item_data)

            affected_projects.append(affected_projects_item)

        api_item_type_is_web_layout = []
        _api_item_type_is_web_layout = d.pop("ApiItemTypeIsWebLayout", UNSET)
        for api_item_type_is_web_layout_item_data in _api_item_type_is_web_layout or []:
            api_item_type_is_web_layout_item = ApiItemTypeIsWebLayoutInfo.from_dict(
                api_item_type_is_web_layout_item_data
            )

            api_item_type_is_web_layout.append(api_item_type_is_web_layout_item)

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

        api_project_template_information = cls(
            affected_projects=affected_projects,
            api_item_type_is_web_layout=api_item_type_is_web_layout,
            project=project,
            is_shared=is_shared,
            is_owned=is_owned,
            owning_project=owning_project,
        )

        return api_project_template_information
