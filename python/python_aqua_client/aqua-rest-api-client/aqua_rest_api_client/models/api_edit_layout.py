from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_edit_layout_entry import ApiEditLayoutEntry


T = TypeVar("T", bound="ApiEditLayout")


@attr.s(auto_attribs=True)
class ApiEditLayout:
    """
    Attributes:
        entries (Union[Unset, None, List['ApiEditLayoutEntry']]):
    """

    entries: Union[Unset, None, List["ApiEditLayoutEntry"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        entries: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            if self.entries is None:
                entries = None
            else:
                entries = []
                for entries_item_data in self.entries:
                    entries_item = entries_item_data.to_dict()

                    entries.append(entries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if entries is not UNSET:
            field_dict["Entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_edit_layout_entry import ApiEditLayoutEntry

        d = src_dict.copy()
        entries = []
        _entries = d.pop("Entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ApiEditLayoutEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        api_edit_layout = cls(
            entries=entries,
        )

        return api_edit_layout
