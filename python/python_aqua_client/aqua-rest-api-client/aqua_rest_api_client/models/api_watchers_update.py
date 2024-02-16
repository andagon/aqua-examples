from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiWatchersUpdate")


@attr.s(auto_attribs=True)
class ApiWatchersUpdate:
    """Represents an update to the watchers list.

    Attributes:
        user_ids_added (Union[Unset, None, List[int]]): Ids of the users to be added to the watchers list
        user_ids_removed (Union[Unset, None, List[int]]): Ids of the users to be removed from the watchers list
    """

    user_ids_added: Union[Unset, None, List[int]] = UNSET
    user_ids_removed: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_ids_added: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.user_ids_added, Unset):
            if self.user_ids_added is None:
                user_ids_added = None
            else:
                user_ids_added = self.user_ids_added

        user_ids_removed: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.user_ids_removed, Unset):
            if self.user_ids_removed is None:
                user_ids_removed = None
            else:
                user_ids_removed = self.user_ids_removed

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_ids_added is not UNSET:
            field_dict["UserIdsAdded"] = user_ids_added
        if user_ids_removed is not UNSET:
            field_dict["UserIdsRemoved"] = user_ids_removed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_ids_added = cast(List[int], d.pop("UserIdsAdded", UNSET))

        user_ids_removed = cast(List[int], d.pop("UserIdsRemoved", UNSET))

        api_watchers_update = cls(
            user_ids_added=user_ids_added,
            user_ids_removed=user_ids_removed,
        )

        return api_watchers_update
