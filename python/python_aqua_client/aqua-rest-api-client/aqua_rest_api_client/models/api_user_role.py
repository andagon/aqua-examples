from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_role_id_name import ApiRoleIdName
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiUserRole")


@attr.s(auto_attribs=True)
class ApiUserRole:
    """Represents the user. the assigned role and the folder.

    Attributes:
        role (Union[Unset, None, ApiRoleIdName]): Holds the id and the name of a role.
        user (Union[Unset, None, ApiUserInfo]): The user information
        folder_id (Union[Unset, int]): The folder id.
    """

    role: Union[Unset, None, "ApiRoleIdName"] = UNSET
    user: Union[Unset, None, "ApiUserInfo"] = UNSET
    folder_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        role: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict() if self.role else None

        user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict() if self.user else None

        folder_id = self.folder_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if role is not UNSET:
            field_dict["Role"] = role
        if user is not UNSET:
            field_dict["User"] = user
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_role_id_name import ApiRoleIdName
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        _role = d.pop("Role", UNSET)
        role: Union[Unset, None, ApiRoleIdName]
        if _role is None:
            role = None
        elif isinstance(_role, Unset):
            role = UNSET
        else:
            role = ApiRoleIdName.from_dict(_role)

        _user = d.pop("User", UNSET)
        user: Union[Unset, None, ApiUserInfo]
        if _user is None:
            user = None
        elif isinstance(_user, Unset):
            user = UNSET
        else:
            user = ApiUserInfo.from_dict(_user)

        folder_id = d.pop("FolderId", UNSET)

        api_user_role = cls(
            role=role,
            user=user,
            folder_id=folder_id,
        )

        return api_user_role
