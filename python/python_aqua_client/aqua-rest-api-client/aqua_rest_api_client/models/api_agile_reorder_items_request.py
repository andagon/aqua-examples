from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAgileReorderItemsRequest")


@attr.s(auto_attribs=True)
class ApiAgileReorderItemsRequest:
    """Backlog items reorder request data

    Attributes:
        ids (Union[Unset, None, List[int]]): The ids of the items which will be reorderd.
        target_id (Union[Unset, int]): The id of the item which is used as anchor of the sorting.
        before_target (Union[Unset, bool]): Indicates whether items should be reorded before or after the target.
    """

    ids: Union[Unset, None, List[int]] = UNSET
    target_id: Union[Unset, int] = UNSET
    before_target: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.ids, Unset):
            if self.ids is None:
                ids = None
            else:
                ids = self.ids

        target_id = self.target_id
        before_target = self.before_target

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if target_id is not UNSET:
            field_dict["TargetId"] = target_id
        if before_target is not UNSET:
            field_dict["BeforeTarget"] = before_target

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = cast(List[int], d.pop("Ids", UNSET))

        target_id = d.pop("TargetId", UNSET)

        before_target = d.pop("BeforeTarget", UNSET)

        api_agile_reorder_items_request = cls(
            ids=ids,
            target_id=target_id,
            before_target=before_target,
        )

        return api_agile_reorder_items_request
