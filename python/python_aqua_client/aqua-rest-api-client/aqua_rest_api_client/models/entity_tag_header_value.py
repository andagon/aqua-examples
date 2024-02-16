from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityTagHeaderValue")


@attr.s(auto_attribs=True)
class EntityTagHeaderValue:
    """
    Attributes:
        tag (Union[Unset, None, str]):
        is_weak (Union[Unset, bool]):
    """

    tag: Union[Unset, None, str] = UNSET
    is_weak: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tag = self.tag
        is_weak = self.is_weak

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tag is not UNSET:
            field_dict["Tag"] = tag
        if is_weak is not UNSET:
            field_dict["IsWeak"] = is_weak

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag = d.pop("Tag", UNSET)

        is_weak = d.pop("IsWeak", UNSET)

        entity_tag_header_value = cls(
            tag=tag,
            is_weak=is_weak,
        )

        return entity_tag_header_value
