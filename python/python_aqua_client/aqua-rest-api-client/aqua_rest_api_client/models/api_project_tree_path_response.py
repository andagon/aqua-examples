from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_tree_folder import ApiProjectTreeFolder
    from ..models.api_project_tree_project import ApiProjectTreeProject


T = TypeVar("T", bound="ApiProjectTreePathResponse")


@attr.s(auto_attribs=True)
class ApiProjectTreePathResponse:
    """Contains information about requested folder "path" i.e.
    includes project information and information of all parents of a given folder
    up to the top.

        Attributes:
            project (Union[Unset, None, ApiProjectTreeProject]): Holds the project information required to render a
                projects/folders tree.
            folders_path (Union[Unset, None, List['ApiProjectTreeFolder']]): Contains folder path, in top-down order.
    """

    project: Union[Unset, None, "ApiProjectTreeProject"] = UNSET
    folders_path: Union[Unset, None, List["ApiProjectTreeFolder"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict() if self.project else None

        folders_path: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.folders_path, Unset):
            if self.folders_path is None:
                folders_path = None
            else:
                folders_path = []
                for folders_path_item_data in self.folders_path:
                    folders_path_item = folders_path_item_data.to_dict()

                    folders_path.append(folders_path_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project is not UNSET:
            field_dict["Project"] = project
        if folders_path is not UNSET:
            field_dict["FoldersPath"] = folders_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_tree_folder import ApiProjectTreeFolder
        from ..models.api_project_tree_project import ApiProjectTreeProject

        d = src_dict.copy()
        _project = d.pop("Project", UNSET)
        project: Union[Unset, None, ApiProjectTreeProject]
        if _project is None:
            project = None
        elif isinstance(_project, Unset):
            project = UNSET
        else:
            project = ApiProjectTreeProject.from_dict(_project)

        folders_path = []
        _folders_path = d.pop("FoldersPath", UNSET)
        for folders_path_item_data in _folders_path or []:
            folders_path_item = ApiProjectTreeFolder.from_dict(folders_path_item_data)

            folders_path.append(folders_path_item)

        api_project_tree_path_response = cls(
            project=project,
            folders_path=folders_path,
        )

        return api_project_tree_path_response
