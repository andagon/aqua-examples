from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiWatcherNew")


@attr.s(auto_attribs=True)
class ApiWatcherNew:
    """Represents a new watcher to be added.

    Attributes:
        user_id (Union[Unset, int]): The id of the involved user.
    """

    user_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("UserId", UNSET)

        api_watcher_new = cls(
            user_id=user_id,
        )

        return api_watcher_new
