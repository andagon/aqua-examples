from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_edit_layout import ApiEditLayout
    from ..models.api_field import ApiField


T = TypeVar("T", bound="ApiItemEditMeta")


@attr.s(auto_attribs=True)
class ApiItemEditMeta:
    """Contains the metadata of fields of an item being edited.

    Attributes:
        fields (Union[Unset, None, List['ApiField']]): Contains all available fields together with their metadata.
        edit_layout (Union[Unset, None, ApiEditLayout]):
    """

    fields: Union[Unset, None, List["ApiField"]] = UNSET
    edit_layout: Union[Unset, None, "ApiEditLayout"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if fields is not UNSET:
            field_dict["Fields"] = fields
        if edit_layout is not UNSET:
            field_dict["EditLayout"] = edit_layout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_edit_layout import ApiEditLayout
        from ..models.api_field import ApiField

        d = src_dict.copy()
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

        api_item_edit_meta = cls(
            fields=fields,
            edit_layout=edit_layout,
        )

        return api_item_edit_meta
