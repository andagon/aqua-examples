from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_field_value import ApiFieldValue


T = TypeVar("T", bound="ApiFieldValueRestriction")


@attr.s(auto_attribs=True)
class ApiFieldValueRestriction:
    """The restriction for certain field value.

    Attributes:
        value (ApiFieldValue):
        allowed_for (List['ApiFieldValue']): The values of the other field for which the specified
            value is allowed.
    """

    value: "ApiFieldValue"
    allowed_for: List["ApiFieldValue"]

    def to_dict(self) -> Dict[str, Any]:
        value = self.value.to_dict()

        allowed_for = []
        for allowed_for_item_data in self.allowed_for:
            allowed_for_item = allowed_for_item_data.to_dict()

            allowed_for.append(allowed_for_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Value": value,
                "AllowedFor": allowed_for,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value import ApiFieldValue

        d = src_dict.copy()
        value = ApiFieldValue.from_dict(d.pop("Value"))

        allowed_for = []
        _allowed_for = d.pop("AllowedFor")
        for allowed_for_item_data in _allowed_for:
            allowed_for_item = ApiFieldValue.from_dict(allowed_for_item_data)

            allowed_for.append(allowed_for_item)

        api_field_value_restriction = cls(
            value=value,
            allowed_for=allowed_for,
        )

        return api_field_value_restriction
