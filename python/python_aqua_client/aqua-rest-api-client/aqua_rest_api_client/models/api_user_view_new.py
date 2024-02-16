from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_user_view_update_fields_data import ApiUserViewUpdateFieldsData


T = TypeVar("T", bound="ApiUserViewNew")


@attr.s(auto_attribs=True)
class ApiUserViewNew:
    """
    Attributes:
        name (Union[Unset, None, str]): The name of the view.
        description (Union[Unset, None, str]): The description of the view.
        color (Union[Unset, None, str]): The color of the view.
            Allowed are only predefined colors, for more information see: [Get predefined
            colors](#operation/System_GetColors).
        is_public (Union[Unset, None, bool]): Indicates whether the view is public or not.
        fields_data (Union[Unset, None, ApiUserViewUpdateFieldsData]): Contains all changes of a user view which depend
            on the
            item type: filter, sorting/grouping and columns.
        applicable_item_types (Union[Unset, None, List[ApiItemType]]): List of ApiItemTypes for wich this user view is
            applicable.
        project_id (Union[Unset, int]): The id of the project.
    """

    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    color: Union[Unset, None, str] = UNSET
    is_public: Union[Unset, None, bool] = UNSET
    fields_data: Union[Unset, None, "ApiUserViewUpdateFieldsData"] = UNSET
    applicable_item_types: Union[Unset, None, List[ApiItemType]] = UNSET
    project_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        color = self.color
        is_public = self.is_public
        fields_data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.fields_data, Unset):
            fields_data = self.fields_data.to_dict() if self.fields_data else None

        applicable_item_types: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.applicable_item_types, Unset):
            if self.applicable_item_types is None:
                applicable_item_types = None
            else:
                applicable_item_types = []
                for applicable_item_types_item_data in self.applicable_item_types:
                    applicable_item_types_item = applicable_item_types_item_data.value

                    applicable_item_types.append(applicable_item_types_item)

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if color is not UNSET:
            field_dict["Color"] = color
        if is_public is not UNSET:
            field_dict["IsPublic"] = is_public
        if fields_data is not UNSET:
            field_dict["FieldsData"] = fields_data
        if applicable_item_types is not UNSET:
            field_dict["ApplicableItemTypes"] = applicable_item_types
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_user_view_update_fields_data import ApiUserViewUpdateFieldsData

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        color = d.pop("Color", UNSET)

        is_public = d.pop("IsPublic", UNSET)

        _fields_data = d.pop("FieldsData", UNSET)
        fields_data: Union[Unset, None, ApiUserViewUpdateFieldsData]
        if _fields_data is None:
            fields_data = None
        elif isinstance(_fields_data, Unset):
            fields_data = UNSET
        else:
            fields_data = ApiUserViewUpdateFieldsData.from_dict(_fields_data)

        applicable_item_types = []
        _applicable_item_types = d.pop("ApplicableItemTypes", UNSET)
        for applicable_item_types_item_data in _applicable_item_types or []:
            applicable_item_types_item = ApiItemType(applicable_item_types_item_data)

            applicable_item_types.append(applicable_item_types_item)

        project_id = d.pop("ProjectId", UNSET)

        api_user_view_new = cls(
            name=name,
            description=description,
            color=color,
            is_public=is_public,
            fields_data=fields_data,
            applicable_item_types=applicable_item_types,
            project_id=project_id,
        )

        api_user_view_new.additional_properties = d
        return api_user_view_new

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
