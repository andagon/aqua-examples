from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_id_name import ApiProjectIdName
    from ..models.api_role_id_name import ApiRoleIdName


T = TypeVar("T", bound="ApiDashboardNGShareProject")


@attr.s(auto_attribs=True)
class ApiDashboardNGShareProject:
    """Represents fact of sharing a dashboard with members of a given project (or all projects),
    optionally with a role. Please see below for possible combination:

    a) no project, no role: all users
    b) project, no role: all members of the project
    c) no project, role: all users having this role in any of the projects
    d) project, role: all members of the project in given role

        Attributes:
            project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
            role (Union[Unset, None, ApiRoleIdName]): Holds the id and the name of a role.
    """

    project: Union[Unset, None, "ApiProjectIdName"] = UNSET
    role: Union[Unset, None, "ApiRoleIdName"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict() if self.project else None

        role: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict() if self.role else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project is not UNSET:
            field_dict["Project"] = project
        if role is not UNSET:
            field_dict["Role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_id_name import ApiProjectIdName
        from ..models.api_role_id_name import ApiRoleIdName

        d = src_dict.copy()
        _project = d.pop("Project", UNSET)
        project: Union[Unset, None, ApiProjectIdName]
        if _project is None:
            project = None
        elif isinstance(_project, Unset):
            project = UNSET
        else:
            project = ApiProjectIdName.from_dict(_project)

        _role = d.pop("Role", UNSET)
        role: Union[Unset, None, ApiRoleIdName]
        if _role is None:
            role = None
        elif isinstance(_role, Unset):
            role = UNSET
        else:
            role = ApiRoleIdName.from_dict(_role)

        api_dashboard_ng_share_project = cls(
            project=project,
            role=role,
        )

        return api_dashboard_ng_share_project
