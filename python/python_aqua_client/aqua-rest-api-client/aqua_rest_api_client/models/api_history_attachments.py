from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistoryAttachments")


@attr.s(auto_attribs=True)
class ApiHistoryAttachments:
    """The list of changes to the attachments of an item.

    Attributes:
        added (Union[Unset, None, List[str]]): The list of names of the attachments which were added
            to the item
        removed (Union[Unset, None, List[str]]): The list of names of the attachments which were removed
            from the item
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

        api_history_attachments = cls(
            added=added,
            removed=removed,
        )

        return api_history_attachments
