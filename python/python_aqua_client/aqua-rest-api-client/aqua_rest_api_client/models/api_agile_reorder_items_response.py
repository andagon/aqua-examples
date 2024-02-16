from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_agile_reorder_items_response_reordered_priority import (
        ApiAgileReorderItemsResponseReorderedPriority,
    )


T = TypeVar("T", bound="ApiAgileReorderItemsResponse")


@attr.s(auto_attribs=True)
class ApiAgileReorderItemsResponse:
    """Contains the reorderd agile priority.

    Attributes:
        reordered_priority (Union[Unset, None, ApiAgileReorderItemsResponseReorderedPriority]): Dictionary containing
            the item id and the new order of the item.
    """

    reordered_priority: Union[Unset, None, "ApiAgileReorderItemsResponseReorderedPriority"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        reordered_priority: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.reordered_priority, Unset):
            reordered_priority = self.reordered_priority.to_dict() if self.reordered_priority else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if reordered_priority is not UNSET:
            field_dict["ReorderedPriority"] = reordered_priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_agile_reorder_items_response_reordered_priority import (
            ApiAgileReorderItemsResponseReorderedPriority,
        )

        d = src_dict.copy()
        _reordered_priority = d.pop("ReorderedPriority", UNSET)
        reordered_priority: Union[Unset, None, ApiAgileReorderItemsResponseReorderedPriority]
        if _reordered_priority is None:
            reordered_priority = None
        elif isinstance(_reordered_priority, Unset):
            reordered_priority = UNSET
        else:
            reordered_priority = ApiAgileReorderItemsResponseReorderedPriority.from_dict(_reordered_priority)

        api_agile_reorder_items_response = cls(
            reordered_priority=reordered_priority,
        )

        return api_agile_reorder_items_response
