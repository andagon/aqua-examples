from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserProjectFolderAssignment")


@attr.s(auto_attribs=True)
class ApiUserProjectFolderAssignment:
    """The user project assignment.

    Attributes:
        user_id (Union[Unset, int]): User Id.
        folder_id (Union[Unset, int]): Project folder id, for the project assignment use id 0.
        role_id (Union[Unset, int]): Role id.
    """

    user_id: Union[Unset, int] = UNSET
    folder_id: Union[Unset, int] = UNSET
    role_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        folder_id = self.folder_id
        role_id = self.role_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if role_id is not UNSET:
            field_dict["RoleId"] = role_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("UserId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        role_id = d.pop("RoleId", UNSET)

        api_user_project_folder_assignment = cls(
            user_id=user_id,
            folder_id=folder_id,
            role_id=role_id,
        )

        return api_user_project_folder_assignment
