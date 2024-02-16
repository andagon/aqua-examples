from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiEditLayoutEntry")


@attr.s(auto_attribs=True)
class ApiEditLayoutEntry:
    """Edit layout entry. Depending on type different properties are available
    (see subclasses).

        Attributes:
            entry_type (str):
    """

    entry_type: str

    def to_dict(self) -> Dict[str, Any]:
        entry_type = self.entry_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "EntryType": entry_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry_type = d.pop("EntryType")

        api_edit_layout_entry = cls(
            entry_type=entry_type,
        )

        return api_edit_layout_entry
