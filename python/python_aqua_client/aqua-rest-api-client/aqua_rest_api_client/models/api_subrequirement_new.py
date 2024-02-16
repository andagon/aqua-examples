from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSubrequirementNew")


@attr.s(auto_attribs=True)
class ApiSubrequirementNew:
    """The information necessary to create a new sub requirement.

    Attributes:
        id (Union[Unset, int]): The id of the requirement which become the new sub requirement.
    """

    id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        api_subrequirement_new = cls(
            id=id,
        )

        return api_subrequirement_new
