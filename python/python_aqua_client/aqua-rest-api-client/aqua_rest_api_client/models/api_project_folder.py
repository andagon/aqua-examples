from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_folder_permissions import ApiProjectFolderPermissions


T = TypeVar("T", bound="ApiProjectFolder")


@attr.s(auto_attribs=True)
class ApiProjectFolder:
    """
    Attributes:
        id (Union[Unset, int]): Id of folder
        name (Union[Unset, None, str]): Name of folder
        parent_folder_id (Union[Unset, int]): Folder Id of Parent, '0' means it is a root folder of the given project
        folder_permissions (Union[Unset, None, ApiProjectFolderPermissions]): Represents permissions in a project.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    parent_folder_id: Union[Unset, int] = UNSET
    folder_permissions: Union[Unset, None, "ApiProjectFolderPermissions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        parent_folder_id = self.parent_folder_id
        folder_permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.folder_permissions, Unset):
            folder_permissions = self.folder_permissions.to_dict() if self.folder_permissions else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if parent_folder_id is not UNSET:
            field_dict["ParentFolderId"] = parent_folder_id
        if folder_permissions is not UNSET:
            field_dict["FolderPermissions"] = folder_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_folder_permissions import ApiProjectFolderPermissions

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        parent_folder_id = d.pop("ParentFolderId", UNSET)

        _folder_permissions = d.pop("FolderPermissions", UNSET)
        folder_permissions: Union[Unset, None, ApiProjectFolderPermissions]
        if _folder_permissions is None:
            folder_permissions = None
        elif isinstance(_folder_permissions, Unset):
            folder_permissions = UNSET
        else:
            folder_permissions = ApiProjectFolderPermissions.from_dict(_folder_permissions)

        api_project_folder = cls(
            id=id,
            name=name,
            parent_folder_id=parent_folder_id,
            folder_permissions=folder_permissions,
        )

        return api_project_folder
