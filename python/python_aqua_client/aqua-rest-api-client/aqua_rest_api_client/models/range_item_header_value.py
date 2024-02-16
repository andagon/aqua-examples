from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RangeItemHeaderValue")


@attr.s(auto_attribs=True)
class RangeItemHeaderValue:
    """
    Attributes:
        from_ (Union[Unset, None, int]):
        to (Union[Unset, None, int]):
    """

    from_: Union[Unset, None, int] = UNSET
    to: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_
        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["From"] = from_
        if to is not UNSET:
            field_dict["To"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("From", UNSET)

        to = d.pop("To", UNSET)

        range_item_header_value = cls(
            from_=from_,
            to=to,
        )

        return range_item_header_value
