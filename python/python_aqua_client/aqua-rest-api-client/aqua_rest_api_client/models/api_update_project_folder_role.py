from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUpdateProjectFolderRole")


@attr.s(auto_attribs=True)
class ApiUpdateProjectFolderRole:
    """
    Attributes:
        folder_id (Union[Unset, int]): The id of the folder.
        user_id (Union[Unset, int]): The id of the user.
        role_id (Union[Unset, int]): The role id for the folder.
    """

    folder_id: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    role_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        folder_id = self.folder_id
        user_id = self.user_id
        role_id = self.role_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if role_id is not UNSET:
            field_dict["RoleId"] = role_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        folder_id = d.pop("FolderId", UNSET)

        user_id = d.pop("UserId", UNSET)

        role_id = d.pop("RoleId", UNSET)

        api_update_project_folder_role = cls(
            folder_id=folder_id,
            user_id=user_id,
            role_id=role_id,
        )

        api_update_project_folder_role.additional_properties = d
        return api_update_project_folder_role

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
