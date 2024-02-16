from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_edit_layout import ApiEditLayout
    from ..models.api_field import ApiField
    from ..models.api_item_location import ApiItemLocation
    from ..models.api_item_permissions import ApiItemPermissions


T = TypeVar("T", bound="ApiItemCreateMeta")


@attr.s(auto_attribs=True)
class ApiItemCreateMeta:
    """Contains the metadata which is necessary for creating a new item.

    Attributes:
        location (Union[Unset, None, ApiItemLocation]): Specifies the location (project and folder) of an item
        fields (Union[Unset, None, List['ApiField']]): Contains all available fields together with their metadata.
        edit_layout (Union[Unset, None, ApiEditLayout]):
        permissions (Union[Unset, None, ApiItemPermissions]): Represents permissions of an item. Intended to be
            subclassed
            by classes with more fine-grained permission set for given context.
    """

    location: Union[Unset, None, "ApiItemLocation"] = UNSET
    fields: Union[Unset, None, List["ApiField"]] = UNSET
    edit_layout: Union[Unset, None, "ApiEditLayout"] = UNSET
    permissions: Union[Unset, None, "ApiItemPermissions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            if self.fields is None:
                fields = None
            else:
                fields = []
                for fields_item_data in self.fields:
                    fields_item = fields_item_data.to_dict()

                    fields.append(fields_item)

        edit_layout: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_layout, Unset):
            edit_layout = self.edit_layout.to_dict() if self.edit_layout else None

        permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict() if self.permissions else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if location is not UNSET:
            field_dict["Location"] = location
        if fields is not UNSET:
            field_dict["Fields"] = fields
        if edit_layout is not UNSET:
            field_dict["EditLayout"] = edit_layout
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_edit_layout import ApiEditLayout
        from ..models.api_field import ApiField
        from ..models.api_item_location import ApiItemLocation
        from ..models.api_item_permissions import ApiItemPermissions

        d = src_dict.copy()
        _location = d.pop("Location", UNSET)
        location: Union[Unset, None, ApiItemLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = ApiItemLocation.from_dict(_location)

        fields = []
        _fields = d.pop("Fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ApiField.from_dict(fields_item_data)

            fields.append(fields_item)

        _edit_layout = d.pop("EditLayout", UNSET)
        edit_layout: Union[Unset, None, ApiEditLayout]
        if _edit_layout is None:
            edit_layout = None
        elif isinstance(_edit_layout, Unset):
            edit_layout = UNSET
        else:
            edit_layout = ApiEditLayout.from_dict(_edit_layout)

        _permissions = d.pop("Permissions", UNSET)
        permissions: Union[Unset, None, ApiItemPermissions]
        if _permissions is None:
            permissions = None
        elif isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ApiItemPermissions.from_dict(_permissions)

        api_item_create_meta = cls(
            location=location,
            fields=fields,
            edit_layout=edit_layout,
            permissions=permissions,
        )

        return api_item_create_meta
