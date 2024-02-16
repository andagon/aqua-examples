from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StringWithQualityHeaderValue")


@attr.s(auto_attribs=True)
class StringWithQualityHeaderValue:
    """
    Attributes:
        value (Union[Unset, None, str]):
        quality (Union[Unset, None, float]):
    """

    value: Union[Unset, None, str] = UNSET
    quality: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        quality = self.quality

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["Value"] = value
        if quality is not UNSET:
            field_dict["Quality"] = quality

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("Value", UNSET)

        quality = d.pop("Quality", UNSET)

        string_with_quality_header_value = cls(
            value=value,
            quality=quality,
        )

        return string_with_quality_header_value
