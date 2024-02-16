from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectFolderCreateSourceFolder")


@attr.s(auto_attribs=True)
class ApiProjectFolderCreateSourceFolder:
    """Encapsulated information about location of a source folder.

    Attributes:
        folder_id (Union[Unset, int]): Id of the source folder (in the source project).
            Zero is not supported here.
    """

    folder_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        folder_id = self.folder_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        folder_id = d.pop("FolderId", UNSET)

        api_project_folder_create_source_folder = cls(
            folder_id=folder_id,
        )

        return api_project_folder_create_source_folder
