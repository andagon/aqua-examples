from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value import ApiFieldValue


T = TypeVar("T", bound="ApiFieldDefaultValue")


@attr.s(auto_attribs=True)
class ApiFieldDefaultValue:
    """Contains the default value for certain field.

    Attributes:
        value (Union[Unset, None, ApiFieldValue]):
        mandatory (Union[Unset, bool]): Indicates that the field must be set to the default value. The field
            is fixed to this exact value.
    """

    value: Union[Unset, None, "ApiFieldValue"] = UNSET
    mandatory: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict() if self.value else None

        mandatory = self.mandatory

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["Value"] = value
        if mandatory is not UNSET:
            field_dict["Mandatory"] = mandatory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value import ApiFieldValue

        d = src_dict.copy()
        _value = d.pop("Value", UNSET)
        value: Union[Unset, None, ApiFieldValue]
        if _value is None:
            value = None
        elif isinstance(_value, Unset):
            value = UNSET
        else:
            value = ApiFieldValue.from_dict(_value)

        mandatory = d.pop("Mandatory", UNSET)

        api_field_default_value = cls(
            value=value,
            mandatory=mandatory,
        )

        return api_field_default_value
