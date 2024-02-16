from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistoryUserCCs")


@attr.s(auto_attribs=True)
class ApiHistoryUserCCs:
    """Contains the changes to the list of users which have subscribed
    to the item and are notified about any changes.

        Attributes:
            added (Union[Unset, None, List[str]]): The list of full names of users which were added to the list
                of subscribers.
            removed (Union[Unset, None, List[str]]): The list of full names of users which were removed from the
                list of subscribers.
    """

    added: Union[Unset, None, List[str]] = UNSET
    removed: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        added: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.added, Unset):
            if self.added is None:
                added = None
            else:
                added = self.added

        removed: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.removed, Unset):
            if self.removed is None:
                removed = None
            else:
                removed = self.removed

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if added is not UNSET:
            field_dict["Added"] = added
        if removed is not UNSET:
            field_dict["Removed"] = removed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        added = cast(List[str], d.pop("Added", UNSET))

        removed = cast(List[str], d.pop("Removed", UNSET))

        api_history_user_c_cs = cls(
            added=added,
            removed=removed,
        )

        return api_history_user_c_cs
