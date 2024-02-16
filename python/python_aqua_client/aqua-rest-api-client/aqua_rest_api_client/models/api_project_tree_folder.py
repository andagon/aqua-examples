from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectTreeFolder")


@attr.s(auto_attribs=True)
class ApiProjectTreeFolder:
    """Holds the folder information required to render a projects/folders tree.

    Attributes:
        id (Union[Unset, int]): Id of folder
        project_id (Union[Unset, int]): Id of project where folder is located
        name (Union[Unset, None, str]): Name of folder
        parent_folder_id (Union[Unset, int]): Folder Id of Parent, '0' means it is a root folder of the given project
        has_subfolders (Union[Unset, bool]): Indicates whether this folder has any subfolders
    """

    id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    parent_folder_id: Union[Unset, int] = UNSET
    has_subfolders: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        project_id = self.project_id
        name = self.name
        parent_folder_id = self.parent_folder_id
        has_subfolders = self.has_subfolders

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if name is not UNSET:
            field_dict["Name"] = name
        if parent_folder_id is not UNSET:
            field_dict["ParentFolderId"] = parent_folder_id
        if has_subfolders is not UNSET:
            field_dict["HasSubfolders"] = has_subfolders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        name = d.pop("Name", UNSET)

        parent_folder_id = d.pop("ParentFolderId", UNSET)

        has_subfolders = d.pop("HasSubfolders", UNSET)

        api_project_tree_folder = cls(
            id=id,
            project_id=project_id,
            name=name,
            parent_folder_id=parent_folder_id,
            has_subfolders=has_subfolders,
        )

        return api_project_tree_folder
