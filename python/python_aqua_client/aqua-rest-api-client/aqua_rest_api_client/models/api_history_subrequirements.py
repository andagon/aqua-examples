from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistorySubrequirements")


@attr.s(auto_attribs=True)
class ApiHistorySubrequirements:
    """The list of changes to the sub requirements of a requirement.

    Attributes:
        added (Union[Unset, None, List[str]]): The list of names of the sub requirements which were added
            to the requirement
        removed (Union[Unset, None, List[str]]): The list of names of the sub requirements which were removed
            from the requirement
        rearranged (Union[Unset, bool]): True is any subrequirements have been rearranged (i.e. changed their
            positions).
    """

    added: Union[Unset, None, List[str]] = UNSET
    removed: Union[Unset, None, List[str]] = UNSET
    rearranged: Union[Unset, bool] = UNSET

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

        rearranged = self.rearranged

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if added is not UNSET:
            field_dict["Added"] = added
        if removed is not UNSET:
            field_dict["Removed"] = removed
        if rearranged is not UNSET:
            field_dict["Rearranged"] = rearranged

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        added = cast(List[str], d.pop("Added", UNSET))

        removed = cast(List[str], d.pop("Removed", UNSET))

        rearranged = d.pop("Rearranged", UNSET)

        api_history_subrequirements = cls(
            added=added,
            removed=removed,
            rearranged=rearranged,
        )

        return api_history_subrequirements
