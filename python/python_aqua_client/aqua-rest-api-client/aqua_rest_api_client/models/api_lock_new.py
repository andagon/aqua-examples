from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLockNew")


@attr.s(auto_attribs=True)
class ApiLockNew:
    """Contains the information necessary to lock an item for
    exclusive editing.

        Attributes:
            version (Union[Unset, int]): The version of the item to lock which the client currently knows.
    """

    version: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("Version", UNSET)

        api_lock_new = cls(
            version=version,
        )

        return api_lock_new
