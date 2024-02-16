from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_tree_folder import ApiProjectTreeFolder
    from ..models.api_project_tree_project import ApiProjectTreeProject


T = TypeVar("T", bound="ApiProjectTreeResponse")


@attr.s(auto_attribs=True)
class ApiProjectTreeResponse:
    """Contains information about requested projects and subfolders,
    mainly for rendering the project tree.

        Attributes:
            projects (Union[Unset, None, List['ApiProjectTreeProject']]): Contains list of available projects.
                This field is filled only if requested, may be null.
            subfolders (Union[Unset, None, List[List['ApiProjectTreeFolder']]]): Contains subfolders info for requested
                nodes.
                The response is returned in the same order as in the request.
    """

    projects: Union[Unset, None, List["ApiProjectTreeProject"]] = UNSET
    subfolders: Union[Unset, None, List[List["ApiProjectTreeFolder"]]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        projects: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            if self.projects is None:
                projects = None
            else:
                projects = []
                for projects_item_data in self.projects:
                    projects_item = projects_item_data.to_dict()

                    projects.append(projects_item)

        subfolders: Union[Unset, None, List[List[Dict[str, Any]]]] = UNSET
        if not isinstance(self.subfolders, Unset):
            if self.subfolders is None:
                subfolders = None
            else:
                subfolders = []
                for subfolders_item_data in self.subfolders:
                    subfolders_item = []
                    for subfolders_item_item_data in subfolders_item_data:
                        subfolders_item_item = subfolders_item_item_data.to_dict()

                        subfolders_item.append(subfolders_item_item)

                    subfolders.append(subfolders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if projects is not UNSET:
            field_dict["Projects"] = projects
        if subfolders is not UNSET:
            field_dict["Subfolders"] = subfolders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_tree_folder import ApiProjectTreeFolder
        from ..models.api_project_tree_project import ApiProjectTreeProject

        d = src_dict.copy()
        projects = []
        _projects = d.pop("Projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = ApiProjectTreeProject.from_dict(projects_item_data)

            projects.append(projects_item)

        subfolders = []
        _subfolders = d.pop("Subfolders", UNSET)
        for subfolders_item_data in _subfolders or []:
            subfolders_item = []
            _subfolders_item = subfolders_item_data
            for subfolders_item_item_data in _subfolders_item:
                subfolders_item_item = ApiProjectTreeFolder.from_dict(subfolders_item_item_data)

                subfolders_item.append(subfolders_item_item)

            subfolders.append(subfolders_item)

        api_project_tree_response = cls(
            projects=projects,
            subfolders=subfolders,
        )

        return api_project_tree_response
