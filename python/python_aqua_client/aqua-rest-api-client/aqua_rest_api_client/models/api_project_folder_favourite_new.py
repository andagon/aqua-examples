from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectFolderFavouriteNew")


@attr.s(auto_attribs=True)
class ApiProjectFolderFavouriteNew:
    """Represents a new folder favourite.

    Attributes:
        project_id (Union[Unset, int]): Id of the project where the favorite is to be created
        folder_id (Union[Unset, int]): Id of the folder where the favorite is to refer to.
            May be zero, what indicates favorite of root folder (i.e. project level)
        label (Union[Unset, None, str]): Custom label of this folder favorite. Empty values (and nulls) are allowed.
    """

    project_id: Union[Unset, int] = UNSET
    folder_id: Union[Unset, int] = UNSET
    label: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        folder_id = self.folder_id
        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if label is not UNSET:
            field_dict["Label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = d.pop("ProjectId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        label = d.pop("Label", UNSET)

        api_project_folder_favourite_new = cls(
            project_id=project_id,
            folder_id=folder_id,
            label=label,
        )

        return api_project_folder_favourite_new
