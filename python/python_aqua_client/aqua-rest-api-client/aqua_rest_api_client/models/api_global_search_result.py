from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_global_search_item import ApiGlobalSearchItem


T = TypeVar("T", bound="ApiGlobalSearchResult")


@attr.s(auto_attribs=True)
class ApiGlobalSearchResult:
    """Represents the result of a global items search

    Attributes:
        start_at (Union[Unset, int]): The number of items which were skipped in the list of results.
            This value is provided during the request.
        max_results (Union[Unset, int]): The maximum number of items which should be included in the result.
        count (Union[Unset, int]): The overall number of items which are available. When using pagination,
            this number is higher than the number of items which are included in the result.
        items (Union[Unset, None, List['ApiGlobalSearchItem']]): The list of items.
    """

    start_at: Union[Unset, int] = UNSET
    max_results: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    items: Union[Unset, None, List["ApiGlobalSearchItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start_at = self.start_at
        max_results = self.max_results
        count = self.count
        items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            if self.items is None:
                items = None
            else:
                items = []
                for items_item_data in self.items:
                    items_item = items_item_data.to_dict()

                    items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if start_at is not UNSET:
            field_dict["StartAt"] = start_at
        if max_results is not UNSET:
            field_dict["MaxResults"] = max_results
        if count is not UNSET:
            field_dict["Count"] = count
        if items is not UNSET:
            field_dict["Items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_global_search_item import ApiGlobalSearchItem

        d = src_dict.copy()
        start_at = d.pop("StartAt", UNSET)

        max_results = d.pop("MaxResults", UNSET)

        count = d.pop("Count", UNSET)

        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = ApiGlobalSearchItem.from_dict(items_item_data)

            items.append(items_item)

        api_global_search_result = cls(
            start_at=start_at,
            max_results=max_results,
            count=count,
            items=items,
        )

        return api_global_search_result
