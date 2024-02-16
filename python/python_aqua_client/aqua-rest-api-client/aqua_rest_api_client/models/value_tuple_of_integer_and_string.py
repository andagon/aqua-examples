from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValueTupleOfIntegerAndString")


@attr.s(auto_attribs=True)
class ValueTupleOfIntegerAndString:
    """
    Attributes:
        item_1 (Union[Unset, int]):
        item_2 (Union[Unset, None, str]):
    """

    item_1: Union[Unset, int] = UNSET
    item_2: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_1 = self.item_1
        item_2 = self.item_2

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_1 is not UNSET:
            field_dict["Item1"] = item_1
        if item_2 is not UNSET:
            field_dict["Item2"] = item_2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_1 = d.pop("Item1", UNSET)

        item_2 = d.pop("Item2", UNSET)

        value_tuple_of_integer_and_string = cls(
            item_1=item_1,
            item_2=item_2,
        )

        return value_tuple_of_integer_and_string
