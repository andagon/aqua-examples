from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistoryItemMoved")


@attr.s(auto_attribs=True)
class ApiHistoryItemMoved:
    """
    Attributes:
        old_path (Union[Unset, None, str]): The old path of the item before it was moved
        new_path (Union[Unset, None, str]): The new path of the item after it was moved
    """

    old_path: Union[Unset, None, str] = UNSET
    new_path: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        old_path = self.old_path
        new_path = self.new_path

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if old_path is not UNSET:
            field_dict["OldPath"] = old_path
        if new_path is not UNSET:
            field_dict["NewPath"] = new_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        old_path = d.pop("OldPath", UNSET)

        new_path = d.pop("NewPath", UNSET)

        api_history_item_moved = cls(
            old_path=old_path,
            new_path=new_path,
        )

        return api_history_item_moved
