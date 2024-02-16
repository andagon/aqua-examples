from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_user_info import ApiUserInfo
    from ..models.api_user_view_permissions import ApiUserViewPermissions


T = TypeVar("T", bound="ApiUserViewInfo")


@attr.s(auto_attribs=True)
class ApiUserViewInfo:
    """Contains some basic information on the user view.

    Attributes:
        id (Union[Unset, int]): The id of the view.
        owner (Union[Unset, None, ApiUserInfo]): The user information
        name (Union[Unset, None, str]): The name of the view.
        description (Union[Unset, None, str]): The description of the view.
        color (Union[Unset, None, str]): The color of the view.
        is_public (Union[Unset, bool]): Indicates whether the view is public or not.
        is_favorite (Union[Unset, bool]): Indicates whether the view is favorite or not.
        permissions (Union[Unset, None, ApiUserViewPermissions]): Represents permissions for a report.
        applicable_item_types (Union[Unset, None, List[ApiItemType]]): List of ApiItemTypes for wich this user view is
            applicable.
    """

    id: Union[Unset, int] = UNSET
    owner: Union[Unset, None, "ApiUserInfo"] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    color: Union[Unset, None, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    permissions: Union[Unset, None, "ApiUserViewPermissions"] = UNSET
    applicable_item_types: Union[Unset, None, List[ApiItemType]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        owner: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict() if self.owner else None

        name = self.name
        description = self.description
        color = self.color
        is_public = self.is_public
        is_favorite = self.is_favorite
        permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict() if self.permissions else None

        applicable_item_types: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.applicable_item_types, Unset):
            if self.applicable_item_types is None:
                applicable_item_types = None
            else:
                applicable_item_types = []
                for applicable_item_types_item_data in self.applicable_item_types:
                    applicable_item_types_item = applicable_item_types_item_data.value

                    applicable_item_types.append(applicable_item_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if owner is not UNSET:
            field_dict["Owner"] = owner
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if color is not UNSET:
            field_dict["Color"] = color
        if is_public is not UNSET:
            field_dict["IsPublic"] = is_public
        if is_favorite is not UNSET:
            field_dict["IsFavorite"] = is_favorite
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions
        if applicable_item_types is not UNSET:
            field_dict["ApplicableItemTypes"] = applicable_item_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_user_info import ApiUserInfo
        from ..models.api_user_view_permissions import ApiUserViewPermissions

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _owner = d.pop("Owner", UNSET)
        owner: Union[Unset, None, ApiUserInfo]
        if _owner is None:
            owner = None
        elif isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = ApiUserInfo.from_dict(_owner)

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        color = d.pop("Color", UNSET)

        is_public = d.pop("IsPublic", UNSET)

        is_favorite = d.pop("IsFavorite", UNSET)

        _permissions = d.pop("Permissions", UNSET)
        permissions: Union[Unset, None, ApiUserViewPermissions]
        if _permissions is None:
            permissions = None
        elif isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ApiUserViewPermissions.from_dict(_permissions)

        applicable_item_types = []
        _applicable_item_types = d.pop("ApplicableItemTypes", UNSET)
        for applicable_item_types_item_data in _applicable_item_types or []:
            applicable_item_types_item = ApiItemType(applicable_item_types_item_data)

            applicable_item_types.append(applicable_item_types_item)

        api_user_view_info = cls(
            id=id,
            owner=owner,
            name=name,
            description=description,
            color=color,
            is_public=is_public,
            is_favorite=is_favorite,
            permissions=permissions,
            applicable_item_types=applicable_item_types,
        )

        return api_user_view_info
