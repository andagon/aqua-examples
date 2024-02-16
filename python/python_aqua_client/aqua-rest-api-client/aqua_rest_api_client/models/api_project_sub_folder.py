from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_folder_permissions import ApiProjectFolderPermissions


T = TypeVar("T", bound="ApiProjectSubFolder")


@attr.s(auto_attribs=True)
class ApiProjectSubFolder:
    """
    Attributes:
        id (Union[Unset, int]): Id of folder
        name (Union[Unset, None, str]): Name of folder
        parent_folder_id (Union[Unset, int]): Folder Id of Parent, '0' means it is a root folder of the given project
        folder_permissions (Union[Unset, None, ApiProjectFolderPermissions]): Represents permissions in a project.
        has_subfolders (Union[Unset, bool]): Indicates whether this folder has any subfolders.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    parent_folder_id: Union[Unset, int] = UNSET
    folder_permissions: Union[Unset, None, "ApiProjectFolderPermissions"] = UNSET
    has_subfolders: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        parent_folder_id = self.parent_folder_id
        folder_permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.folder_permissions, Unset):
            folder_permissions = self.folder_permissions.to_dict() if self.folder_permissions else None

        has_subfolders = self.has_subfolders

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if parent_folder_id is not UNSET:
            field_dict["ParentFolderId"] = parent_folder_id
        if folder_permissions is not UNSET:
            field_dict["FolderPermissions"] = folder_permissions
        if has_subfolders is not UNSET:
            field_dict["HasSubfolders"] = has_subfolders

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

        has_subfolders = d.pop("HasSubfolders", UNSET)

        api_project_sub_folder = cls(
            id=id,
            name=name,
            parent_folder_id=parent_folder_id,
            folder_permissions=folder_permissions,
            has_subfolders=has_subfolders,
        )

        api_project_sub_folder.additional_properties = d
        return api_project_sub_folder

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
