from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ApiFieldValueRestrictionUpdate")


@attr.s(auto_attribs=True)
class ApiFieldValueRestrictionUpdate:
    """Represents the modification of a restriction, which restricts
    the value of field based on the values of another field.

        Attributes:
            value (Any): The value which should be restricted.
            allowed_for (List[Any]): A list of values of the other field for which the current
                value is allowed.
    """

    value: Any
    allowed_for: List[Any]

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        allowed_for = self.allowed_for

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
        d = src_dict.copy()
        value = d.pop("Value")

        allowed_for = cast(List[Any], d.pop("AllowedFor"))

        api_field_value_restriction_update = cls(
            value=value,
            allowed_for=allowed_for,
        )

        return api_field_value_restriction_update
