from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_info import ApiItemInfo


T = TypeVar("T", bound="ApiItemSearchResult")


@attr.s(auto_attribs=True)
class ApiItemSearchResult:
    """The list of search results and some meta information regarding
    the search.

        Attributes:
            search_term (Union[Unset, None, str]): The term for which the search has been performed
            count (Union[Unset, int]): The overall number of results.
            items (Union[Unset, None, List['ApiItemInfo']]): The results of the search. The list contains basic information
                for each search result.
    """

    search_term: Union[Unset, None, str] = UNSET
    count: Union[Unset, int] = UNSET
    items: Union[Unset, None, List["ApiItemInfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        search_term = self.search_term
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
        if search_term is not UNSET:
            field_dict["SearchTerm"] = search_term
        if count is not UNSET:
            field_dict["Count"] = count
        if items is not UNSET:
            field_dict["Items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_info import ApiItemInfo

        d = src_dict.copy()
        search_term = d.pop("SearchTerm", UNSET)

        count = d.pop("Count", UNSET)

        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = ApiItemInfo.from_dict(items_item_data)

            items.append(items_item)

        api_item_search_result = cls(
            search_term=search_term,
            count=count,
            items=items,
        )

        return api_item_search_result
