from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldRange")


@attr.s(auto_attribs=True)
class ApiFieldRange:
    """
    Attributes:
        min_ (Union[Unset, None, float]): If the field has the type decimal, this field contains the minimal value.
        max_ (Union[Unset, None, float]): If the field has the type decimal, this field contains the maximal value.
    """

    min_: Union[Unset, None, float] = UNSET
    max_: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_
        max_ = self.max_

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["Min"] = min_
        if max_ is not UNSET:
            field_dict["Max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("Min", UNSET)

        max_ = d.pop("Max", UNSET)

        api_field_range = cls(
            min_=min_,
            max_=max_,
        )

        return api_field_range
