from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldUpdate")


@attr.s(auto_attribs=True)
class ApiFieldUpdate:
    """Specifies the update to perform on a specific field.

    Attributes:
        field_id (Union[Unset, None, str]): The id of the field to update.
        value (Union[Unset, Any]): The value to which the field will be changed. The exact type of the
            value depends on the field of the type:

                String: the value as string
                Decimal: the value as number
                Datetime: a string defining the date and time in the following format: yyyy-MM-ddTHH:mm:ssK or
                yyyy-MM-ddTHH:mm:ss.fffK. The K represents optional time zone information (Z for UTC or a time zone offset).
                E.g.: 2018-03-15T21:42:42, 2018-03-15T21:42:42.123, 2018-03-15T21:42:42.123Z, 2018-03-15T21:42:42.123+02:00.
                Dictionary: the id of the field value as number (or null for empty)
                MultiChoiceDictionary: a list of numbers where each number is a field value id. E.g.: [1,2] (or [] for
            empty)
                User: the user id as number (or null for empty)
                MultiChoiceUser: a list of numbers where each number is a user id. E.g.: [1,2] (or [] for empty)
                TimeSpan: the value of the time span as number e.g.: {"FieldId": {"Value": 4,"Unit": "Hour"}}.
                Sprint: the id of the sprint as number (or null for empty)
                Text: ApiRichText object, e.g.: {{  "html": "sometext",  "incompatibleRichTextFeatures": false}}
    """

    field_id: Union[Unset, None, str] = UNSET
    value: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId", UNSET)

        value = d.pop("Value", UNSET)

        api_field_update = cls(
            field_id=field_id,
            value=value,
        )

        return api_field_update
