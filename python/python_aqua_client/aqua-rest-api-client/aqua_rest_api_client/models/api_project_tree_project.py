from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectTreeProject")


@attr.s(auto_attribs=True)
class ApiProjectTreeProject:
    """Holds the project information required to render a projects/folders tree.

    Attributes:
        id (Union[Unset, int]): The id of the project.
        name (Union[Unset, None, str]): The name of the project.
        has_subfolders (Union[Unset, bool]): Indicates whether this project has any subfolders
        archived (Union[Unset, bool]): Indicates whether this project is archived
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    has_subfolders: Union[Unset, bool] = UNSET
    archived: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        has_subfolders = self.has_subfolders
        archived = self.archived

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if has_subfolders is not UNSET:
            field_dict["HasSubfolders"] = has_subfolders
        if archived is not UNSET:
            field_dict["Archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        has_subfolders = d.pop("HasSubfolders", UNSET)

        archived = d.pop("Archived", UNSET)

        api_project_tree_project = cls(
            id=id,
            name=name,
            has_subfolders=has_subfolders,
            archived=archived,
        )

        return api_project_tree_project
