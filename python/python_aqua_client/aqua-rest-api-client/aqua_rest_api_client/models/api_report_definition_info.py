from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_id_name import ApiProjectIdName
    from ..models.api_report_permissions import ApiReportPermissions
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiReportDefinitionInfo")


@attr.s(auto_attribs=True)
class ApiReportDefinitionInfo:
    """Contains information about report definition.

    Attributes:
        id (Union[Unset, int]): The id of the report definition.
        name (Union[Unset, None, str]): The name of the report definition.
        owner (Union[Unset, None, ApiUserInfo]): The user information
        project_info (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
        color (Union[Unset, None, str]): The color of the report definition
        is_public (Union[Unset, bool]): If true indicates that the report definition is public.
        item_types (Union[Unset, None, List[ApiItemType]]): List of used ApiItemTypes for this report definition.
        permissions (Union[Unset, None, ApiReportPermissions]): Represents permissions for a report.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    owner: Union[Unset, None, "ApiUserInfo"] = UNSET
    project_info: Union[Unset, None, "ApiProjectIdName"] = UNSET
    color: Union[Unset, None, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    item_types: Union[Unset, None, List[ApiItemType]] = UNSET
    permissions: Union[Unset, None, "ApiReportPermissions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        owner: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict() if self.owner else None

        project_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project_info, Unset):
            project_info = self.project_info.to_dict() if self.project_info else None

        color = self.color
        is_public = self.is_public
        item_types: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.item_types, Unset):
            if self.item_types is None:
                item_types = None
            else:
                item_types = []
                for item_types_item_data in self.item_types:
                    item_types_item = item_types_item_data.value

                    item_types.append(item_types_item)

        permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict() if self.permissions else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if owner is not UNSET:
            field_dict["Owner"] = owner
        if project_info is not UNSET:
            field_dict["ProjectInfo"] = project_info
        if color is not UNSET:
            field_dict["Color"] = color
        if is_public is not UNSET:
            field_dict["IsPublic"] = is_public
        if item_types is not UNSET:
            field_dict["ItemTypes"] = item_types
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_id_name import ApiProjectIdName
        from ..models.api_report_permissions import ApiReportPermissions
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        _owner = d.pop("Owner", UNSET)
        owner: Union[Unset, None, ApiUserInfo]
        if _owner is None:
            owner = None
        elif isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = ApiUserInfo.from_dict(_owner)

        _project_info = d.pop("ProjectInfo", UNSET)
        project_info: Union[Unset, None, ApiProjectIdName]
        if _project_info is None:
            project_info = None
        elif isinstance(_project_info, Unset):
            project_info = UNSET
        else:
            project_info = ApiProjectIdName.from_dict(_project_info)

        color = d.pop("Color", UNSET)

        is_public = d.pop("IsPublic", UNSET)

        item_types = []
        _item_types = d.pop("ItemTypes", UNSET)
        for item_types_item_data in _item_types or []:
            item_types_item = ApiItemType(item_types_item_data)

            item_types.append(item_types_item)

        _permissions = d.pop("Permissions", UNSET)
        permissions: Union[Unset, None, ApiReportPermissions]
        if _permissions is None:
            permissions = None
        elif isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ApiReportPermissions.from_dict(_permissions)

        api_report_definition_info = cls(
            id=id,
            name=name,
            owner=owner,
            project_info=project_info,
            color=color,
            is_public=is_public,
            item_types=item_types,
            permissions=permissions,
        )

        return api_report_definition_info
