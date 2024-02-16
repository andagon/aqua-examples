from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_config_info import ApiProjectConfigInfo
    from ..models.api_project_folder_permissions import ApiProjectFolderPermissions
    from ..models.api_project_permissions import ApiProjectPermissions
    from ..models.api_system_permissions import ApiSystemPermissions


T = TypeVar("T", bound="ApiProjectInfo")


@attr.s(auto_attribs=True)
class ApiProjectInfo:
    """
    Attributes:
        id (Union[Unset, int]): The id of the project.
        name (Union[Unset, None, str]): The name of the project.
        is_archived (Union[Unset, bool]): True if project was makred as archived.
        is_favourite (Union[Unset, bool]): true if project was makred as favourite
        has_subfolders (Union[Unset, bool]): Indicates whether this project has any subfolders.
        short_description (Union[Unset, None, str]): short description of this project
        project_permissions (Union[Unset, None, ApiProjectPermissions]): Represents permissions in a project. Includes
            only project-level permissions.
            For permissions that can be defined on folder level (e.g. permissions to create items)
            please refer to ApiProjectFolderPermissions (this also included a project's root-folder permissions).
        system_permissions (Union[Unset, None, ApiSystemPermissions]): Represents permissions in a system.
        folder_permissions (Union[Unset, None, ApiProjectFolderPermissions]): Represents permissions in a project.
        project_config (Union[Unset, None, ApiProjectConfigInfo]): Some basic information regarding the project
            configuration
            (template, etc.).
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    is_favourite: Union[Unset, bool] = UNSET
    has_subfolders: Union[Unset, bool] = UNSET
    short_description: Union[Unset, None, str] = UNSET
    project_permissions: Union[Unset, None, "ApiProjectPermissions"] = UNSET
    system_permissions: Union[Unset, None, "ApiSystemPermissions"] = UNSET
    folder_permissions: Union[Unset, None, "ApiProjectFolderPermissions"] = UNSET
    project_config: Union[Unset, None, "ApiProjectConfigInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        is_archived = self.is_archived
        is_favourite = self.is_favourite
        has_subfolders = self.has_subfolders
        short_description = self.short_description
        project_permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project_permissions, Unset):
            project_permissions = self.project_permissions.to_dict() if self.project_permissions else None

        system_permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.system_permissions, Unset):
            system_permissions = self.system_permissions.to_dict() if self.system_permissions else None

        folder_permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.folder_permissions, Unset):
            folder_permissions = self.folder_permissions.to_dict() if self.folder_permissions else None

        project_config: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project_config, Unset):
            project_config = self.project_config.to_dict() if self.project_config else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if is_archived is not UNSET:
            field_dict["IsArchived"] = is_archived
        if is_favourite is not UNSET:
            field_dict["IsFavourite"] = is_favourite
        if has_subfolders is not UNSET:
            field_dict["HasSubfolders"] = has_subfolders
        if short_description is not UNSET:
            field_dict["ShortDescription"] = short_description
        if project_permissions is not UNSET:
            field_dict["ProjectPermissions"] = project_permissions
        if system_permissions is not UNSET:
            field_dict["SystemPermissions"] = system_permissions
        if folder_permissions is not UNSET:
            field_dict["FolderPermissions"] = folder_permissions
        if project_config is not UNSET:
            field_dict["ProjectConfig"] = project_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_config_info import ApiProjectConfigInfo
        from ..models.api_project_folder_permissions import ApiProjectFolderPermissions
        from ..models.api_project_permissions import ApiProjectPermissions
        from ..models.api_system_permissions import ApiSystemPermissions

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        is_archived = d.pop("IsArchived", UNSET)

        is_favourite = d.pop("IsFavourite", UNSET)

        has_subfolders = d.pop("HasSubfolders", UNSET)

        short_description = d.pop("ShortDescription", UNSET)

        _project_permissions = d.pop("ProjectPermissions", UNSET)
        project_permissions: Union[Unset, None, ApiProjectPermissions]
        if _project_permissions is None:
            project_permissions = None
        elif isinstance(_project_permissions, Unset):
            project_permissions = UNSET
        else:
            project_permissions = ApiProjectPermissions.from_dict(_project_permissions)

        _system_permissions = d.pop("SystemPermissions", UNSET)
        system_permissions: Union[Unset, None, ApiSystemPermissions]
        if _system_permissions is None:
            system_permissions = None
        elif isinstance(_system_permissions, Unset):
            system_permissions = UNSET
        else:
            system_permissions = ApiSystemPermissions.from_dict(_system_permissions)

        _folder_permissions = d.pop("FolderPermissions", UNSET)
        folder_permissions: Union[Unset, None, ApiProjectFolderPermissions]
        if _folder_permissions is None:
            folder_permissions = None
        elif isinstance(_folder_permissions, Unset):
            folder_permissions = UNSET
        else:
            folder_permissions = ApiProjectFolderPermissions.from_dict(_folder_permissions)

        _project_config = d.pop("ProjectConfig", UNSET)
        project_config: Union[Unset, None, ApiProjectConfigInfo]
        if _project_config is None:
            project_config = None
        elif isinstance(_project_config, Unset):
            project_config = UNSET
        else:
            project_config = ApiProjectConfigInfo.from_dict(_project_config)

        api_project_info = cls(
            id=id,
            name=name,
            is_archived=is_archived,
            is_favourite=is_favourite,
            has_subfolders=has_subfolders,
            short_description=short_description,
            project_permissions=project_permissions,
            system_permissions=system_permissions,
            folder_permissions=folder_permissions,
            project_config=project_config,
        )

        api_project_info.additional_properties = d
        return api_project_info

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
