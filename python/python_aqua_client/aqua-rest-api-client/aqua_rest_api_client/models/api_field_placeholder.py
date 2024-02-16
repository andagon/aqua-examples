from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_field_type import ApiFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldPlaceholder")


@attr.s(auto_attribs=True)
class ApiFieldPlaceholder:
    """A placeholder field to be replaced with a value from the
    TestCase on test execution

        Attributes:
            placeholder (Union[Unset, None, str]): The placeholder text for this field
            title (Union[Unset, None, str]): The field title for UI purposes
            field_id (Union[Unset, None, str]): The internal Id for the field.
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
    """

    placeholder: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    field_id: Union[Unset, None, str] = UNSET
    field_type: Union[Unset, ApiFieldType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        placeholder = self.placeholder
        title = self.title
        field_id = self.field_id
        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if placeholder is not UNSET:
            field_dict["Placeholder"] = placeholder
        if title is not UNSET:
            field_dict["Title"] = title
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if field_type is not UNSET:
            field_dict["FieldType"] = field_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        placeholder = d.pop("Placeholder", UNSET)

        title = d.pop("Title", UNSET)

        field_id = d.pop("FieldId", UNSET)

        _field_type = d.pop("FieldType", UNSET)
        field_type: Union[Unset, ApiFieldType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = ApiFieldType(_field_type)

        api_field_placeholder = cls(
            placeholder=placeholder,
            title=title,
            field_id=field_id,
            field_type=field_type,
        )

        return api_field_placeholder
