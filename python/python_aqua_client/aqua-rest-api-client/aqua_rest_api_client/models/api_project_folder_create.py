from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_folder_create_source_folder import ApiProjectFolderCreateSourceFolder


T = TypeVar("T", bound="ApiProjectFolderCreate")


@attr.s(auto_attribs=True)
class ApiProjectFolderCreate:
    """
    Attributes:
        name (Union[Unset, None, str]): Name fo the folder to be created.
            If SourceFolder is provided then Name must be null, what means using the same name as name of the source folder.
            If SourceFolder is not provided then Name is required (not empty).
            Note: folder names must be unique (on one level).
        source_folder (Union[Unset, None, ApiProjectFolderCreateSourceFolder]): Encapsulated information about location
            of a source folder.
    """

    name: Union[Unset, None, str] = UNSET
    source_folder: Union[Unset, None, "ApiProjectFolderCreateSourceFolder"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        source_folder: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.source_folder, Unset):
            source_folder = self.source_folder.to_dict() if self.source_folder else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if source_folder is not UNSET:
            field_dict["SourceFolder"] = source_folder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_folder_create_source_folder import ApiProjectFolderCreateSourceFolder

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        _source_folder = d.pop("SourceFolder", UNSET)
        source_folder: Union[Unset, None, ApiProjectFolderCreateSourceFolder]
        if _source_folder is None:
            source_folder = None
        elif isinstance(_source_folder, Unset):
            source_folder = UNSET
        else:
            source_folder = ApiProjectFolderCreateSourceFolder.from_dict(_source_folder)

        api_project_folder_create = cls(
            name=name,
            source_folder=source_folder,
        )

        return api_project_folder_create
