from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentRangeHeaderValue")


@attr.s(auto_attribs=True)
class ContentRangeHeaderValue:
    """
    Attributes:
        unit (Union[Unset, None, str]):
        from_ (Union[Unset, None, int]):
        to (Union[Unset, None, int]):
        length (Union[Unset, None, int]):
        has_length (Union[Unset, bool]):
        has_range (Union[Unset, bool]):
    """

    unit: Union[Unset, None, str] = UNSET
    from_: Union[Unset, None, int] = UNSET
    to: Union[Unset, None, int] = UNSET
    length: Union[Unset, None, int] = UNSET
    has_length: Union[Unset, bool] = UNSET
    has_range: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        unit = self.unit
        from_ = self.from_
        to = self.to
        length = self.length
        has_length = self.has_length
        has_range = self.has_range

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if unit is not UNSET:
            field_dict["Unit"] = unit
        if from_ is not UNSET:
            field_dict["From"] = from_
        if to is not UNSET:
            field_dict["To"] = to
        if length is not UNSET:
            field_dict["Length"] = length
        if has_length is not UNSET:
            field_dict["HasLength"] = has_length
        if has_range is not UNSET:
            field_dict["HasRange"] = has_range

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit = d.pop("Unit", UNSET)

        from_ = d.pop("From", UNSET)

        to = d.pop("To", UNSET)

        length = d.pop("Length", UNSET)

        has_length = d.pop("HasLength", UNSET)

        has_range = d.pop("HasRange", UNSET)

        content_range_header_value = cls(
            unit=unit,
            from_=from_,
            to=to,
            length=length,
            has_length=has_length,
            has_range=has_range,
        )

        return content_range_header_value
