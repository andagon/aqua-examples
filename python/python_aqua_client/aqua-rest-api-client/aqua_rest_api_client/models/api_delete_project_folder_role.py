from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDeleteProjectFolderRole")


@attr.s(auto_attribs=True)
class ApiDeleteProjectFolderRole:
    """
    Attributes:
        folder_id (Union[Unset, int]): The id of the folder.
        user_id (Union[Unset, int]): The id of the user.
    """

    folder_id: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        folder_id = self.folder_id
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        folder_id = d.pop("FolderId", UNSET)

        user_id = d.pop("UserId", UNSET)

        api_delete_project_folder_role = cls(
            folder_id=folder_id,
            user_id=user_id,
        )

        return api_delete_project_folder_role
