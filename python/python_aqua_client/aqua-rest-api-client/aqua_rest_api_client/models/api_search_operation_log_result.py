from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_operation_log import ApiOperationLog


T = TypeVar("T", bound="ApiSearchOperationLogResult")


@attr.s(auto_attribs=True)
class ApiSearchOperationLogResult:
    """
    Attributes:
        count (Union[Unset, int]): Count of all records matching the search request.
        first_results (Union[Unset, None, int]): FirstResults from search request (if any)
        max_results (Union[Unset, None, int]): MaxResults from search request (if any)
        items (Union[Unset, None, List['ApiOperationLog']]): Contains found items matching the search criteria.
            If FirstResults/MaxResults have been provided in the search request then contains only appropriate portion of
            results,
    """

    count: Union[Unset, int] = UNSET
    first_results: Union[Unset, None, int] = UNSET
    max_results: Union[Unset, None, int] = UNSET
    items: Union[Unset, None, List["ApiOperationLog"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        first_results = self.first_results
        max_results = self.max_results
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
        if count is not UNSET:
            field_dict["Count"] = count
        if first_results is not UNSET:
            field_dict["FirstResults"] = first_results
        if max_results is not UNSET:
            field_dict["MaxResults"] = max_results
        if items is not UNSET:
            field_dict["Items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_operation_log import ApiOperationLog

        d = src_dict.copy()
        count = d.pop("Count", UNSET)

        first_results = d.pop("FirstResults", UNSET)

        max_results = d.pop("MaxResults", UNSET)

        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = ApiOperationLog.from_dict(items_item_data)

            items.append(items_item)

        api_search_operation_log_result = cls(
            count=count,
            first_results=first_results,
            max_results=max_results,
            items=items,
        )

        return api_search_operation_log_result
