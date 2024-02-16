from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyValuePairOfStringAndIEnumerableOfString")


@attr.s(auto_attribs=True)
class KeyValuePairOfStringAndIEnumerableOfString:
    """
    Attributes:
        key (Union[Unset, None, str]):
        value (Union[Unset, None, List[str]]):
    """

    key: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        value: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.value, Unset):
            if self.value is None:
                value = None
            else:
                value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if key is not UNSET:
            field_dict["Key"] = key
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("Key", UNSET)

        value = cast(List[str], d.pop("Value", UNSET))

        key_value_pair_of_string_and_i_enumerable_of_string = cls(
            key=key,
            value=value,
        )

        return key_value_pair_of_string_and_i_enumerable_of_string
