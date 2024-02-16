from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSubrequirementUpdate")


@attr.s(auto_attribs=True)
class ApiSubrequirementUpdate:
    """The information to update in a given sub requirement.

    Attributes:
        child_index (Union[Unset, int]): The new child index of the sub requirement.
    """

    child_index: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        child_index = self.child_index

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if child_index is not UNSET:
            field_dict["ChildIndex"] = child_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        child_index = d.pop("ChildIndex", UNSET)

        api_subrequirement_update = cls(
            child_index=child_index,
        )

        return api_subrequirement_update
