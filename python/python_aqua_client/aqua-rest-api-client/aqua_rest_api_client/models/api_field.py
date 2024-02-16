from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_field_type import ApiFieldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_edit_meta import ApiFieldEditMeta


T = TypeVar("T", bound="ApiField")


@attr.s(auto_attribs=True)
class ApiField:
    """Contains meta information for a specific field of an item.

    Attributes:
        id (Union[Unset, None, str]): The id of the field. The field id is identical to the internal property name.
            Therefore, it is
            only unique in scope of the same project and item type.
        title (Union[Unset, None, str]): The title for the field which should be shown in the user interface.
        field_type (Union[Unset, ApiFieldType]): Identifies the type of a field in aqua.
            This enum has the following values:
              - `DateTime`
              - `Decimal`
              - `Dictionary`
              - `DictionaryMultiChoice`
              - `ExecutionHistory`
              - `Flag`
              - `Id`
              - `Json`
              - `Sprint`
              - `String`
              - `StringAutoComplete`
              - `StringList`
              - `TestJobStatistics`
              - `TestScenarios`
              - `Text`
              - `TimeSpan`
              - `User`
              - `UserMultiChoice`
        edit_meta (Union[Unset, None, ApiFieldEditMeta]): Contains the information for a specific field of an item
            including
            the field's value.
    """

    id: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    field_type: Union[Unset, ApiFieldType] = UNSET
    edit_meta: Union[Unset, None, "ApiFieldEditMeta"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        edit_meta: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_meta, Unset):
            edit_meta = self.edit_meta.to_dict() if self.edit_meta else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if title is not UNSET:
            field_dict["Title"] = title
        if field_type is not UNSET:
            field_dict["FieldType"] = field_type
        if edit_meta is not UNSET:
            field_dict["EditMeta"] = edit_meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_edit_meta import ApiFieldEditMeta

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        title = d.pop("Title", UNSET)

        _field_type = d.pop("FieldType", UNSET)
        field_type: Union[Unset, ApiFieldType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = ApiFieldType(_field_type)

        _edit_meta = d.pop("EditMeta", UNSET)
        edit_meta: Union[Unset, None, ApiFieldEditMeta]
        if _edit_meta is None:
            edit_meta = None
        elif isinstance(_edit_meta, Unset):
            edit_meta = UNSET
        else:
            edit_meta = ApiFieldEditMeta.from_dict(_edit_meta)

        api_field = cls(
            id=id,
            title=title,
            field_type=field_type,
            edit_meta=edit_meta,
        )

        return api_field
