from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBatchAllowedValuesRequest")


@attr.s(auto_attribs=True)
class ApiBatchAllowedValuesRequest:
    """A request for the values which are alllowed for a batch update of
    given field in the given items.

        Attributes:
            item_ids (Union[Unset, None, List[int]]): The ids of the items for which the possible values should
                be computed
            field_ids (Union[Unset, None, List[str]]): The ids of the field for which the possible values should
                be computed.
            limit (Union[Unset, int]): Limit on number of returned values per field (0 means unlimited).
                If found more values than allowed limit then return only the part (not more than limit) and additionally
                count of all values.
    """

    item_ids: Union[Unset, None, List[int]] = UNSET
    field_ids: Union[Unset, None, List[str]] = UNSET
    limit: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.item_ids, Unset):
            if self.item_ids is None:
                item_ids = None
            else:
                item_ids = self.item_ids

        field_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.field_ids, Unset):
            if self.field_ids is None:
                field_ids = None
            else:
                field_ids = self.field_ids

        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_ids is not UNSET:
            field_dict["ItemIds"] = item_ids
        if field_ids is not UNSET:
            field_dict["FieldIds"] = field_ids
        if limit is not UNSET:
            field_dict["Limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_ids = cast(List[int], d.pop("ItemIds", UNSET))

        field_ids = cast(List[str], d.pop("FieldIds", UNSET))

        limit = d.pop("Limit", UNSET)

        api_batch_allowed_values_request = cls(
            item_ids=item_ids,
            field_ids=field_ids,
            limit=limit,
        )

        return api_batch_allowed_values_request
