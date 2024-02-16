from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_batch_allowed_values_response_entry import ApiBatchAllowedValuesResponseEntry
    from ..models.api_item_identifier import ApiItemIdentifier


T = TypeVar("T", bound="ApiBatchAllowedValuesResponse")


@attr.s(auto_attribs=True)
class ApiBatchAllowedValuesResponse:
    """Contains the values which are allowed for a batch update
    of the specified fields in the specified items.

        Attributes:
            items (Union[Unset, None, List['ApiItemIdentifier']]): The items for which this response is valid.
            entries (Union[Unset, None, List['ApiBatchAllowedValuesResponseEntry']]): Entries containing information for
                each requested field.
    """

    items: Union[Unset, None, List["ApiItemIdentifier"]] = UNSET
    entries: Union[Unset, None, List["ApiBatchAllowedValuesResponseEntry"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            if self.items is None:
                items = None
            else:
                items = []
                for items_item_data in self.items:
                    items_item = items_item_data.to_dict()

                    items.append(items_item)

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
        if items is not UNSET:
            field_dict["Items"] = items
        if entries is not UNSET:
            field_dict["Entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_batch_allowed_values_response_entry import ApiBatchAllowedValuesResponseEntry
        from ..models.api_item_identifier import ApiItemIdentifier

        d = src_dict.copy()
        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = ApiItemIdentifier.from_dict(items_item_data)

            items.append(items_item)

        entries = []
        _entries = d.pop("Entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ApiBatchAllowedValuesResponseEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        api_batch_allowed_values_response = cls(
            items=items,
            entries=entries,
        )

        return api_batch_allowed_values_response
