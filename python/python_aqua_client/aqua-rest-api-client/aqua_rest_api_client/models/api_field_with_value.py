from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_field_type import ApiFieldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_edit_meta import ApiFieldEditMeta
    from ..models.api_field_value import ApiFieldValue


T = TypeVar("T", bound="ApiFieldWithValue")


@attr.s(auto_attribs=True)
class ApiFieldWithValue:
    """
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
        value (Union[Unset, None, ApiFieldValue]):
    """

    id: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    field_type: Union[Unset, ApiFieldType] = UNSET
    edit_meta: Union[Unset, None, "ApiFieldEditMeta"] = UNSET
    value: Union[Unset, None, "ApiFieldValue"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        edit_meta: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_meta, Unset):
            edit_meta = self.edit_meta.to_dict() if self.edit_meta else None

        value: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict() if self.value else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if title is not UNSET:
            field_dict["Title"] = title
        if field_type is not UNSET:
            field_dict["FieldType"] = field_type
        if edit_meta is not UNSET:
            field_dict["EditMeta"] = edit_meta
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_edit_meta import ApiFieldEditMeta
        from ..models.api_field_value import ApiFieldValue

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

        _value = d.pop("Value", UNSET)
        value: Union[Unset, None, ApiFieldValue]
        if _value is None:
            value = None
        elif isinstance(_value, Unset):
            value = UNSET
        else:
            value = ApiFieldValue.from_dict(_value)

        api_field_with_value = cls(
            id=id,
            title=title,
            field_type=field_type,
            edit_meta=edit_meta,
            value=value,
        )

        api_field_with_value.additional_properties = d
        return api_field_with_value

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
