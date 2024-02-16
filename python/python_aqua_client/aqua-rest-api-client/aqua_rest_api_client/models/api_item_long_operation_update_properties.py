from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_batch_field_update import ApiBatchFieldUpdate
    from ..models.api_item_long_operation_domain import ApiItemLongOperationDomain


T = TypeVar("T", bound="ApiItemLongOperationUpdateProperties")


@attr.s(auto_attribs=True)
class ApiItemLongOperationUpdateProperties:
    """Represents request to batch update items (update properties).

    Attributes:
        criteria (Union[Unset, None, ApiItemLongOperationDomain]): Defines set of items to be processed.
        updates (Union[Unset, None, List['ApiBatchFieldUpdate']]): List of updates to be applied.
    """

    criteria: Union[Unset, None, "ApiItemLongOperationDomain"] = UNSET
    updates: Union[Unset, None, List["ApiBatchFieldUpdate"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        criteria: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict() if self.criteria else None

        updates: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.updates, Unset):
            if self.updates is None:
                updates = None
            else:
                updates = []
                for updates_item_data in self.updates:
                    updates_item = updates_item_data.to_dict()

                    updates.append(updates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["Criteria"] = criteria
        if updates is not UNSET:
            field_dict["Updates"] = updates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_batch_field_update import ApiBatchFieldUpdate
        from ..models.api_item_long_operation_domain import ApiItemLongOperationDomain

        d = src_dict.copy()
        _criteria = d.pop("Criteria", UNSET)
        criteria: Union[Unset, None, ApiItemLongOperationDomain]
        if _criteria is None:
            criteria = None
        elif isinstance(_criteria, Unset):
            criteria = UNSET
        else:
            criteria = ApiItemLongOperationDomain.from_dict(_criteria)

        updates = []
        _updates = d.pop("Updates", UNSET)
        for updates_item_data in _updates or []:
            updates_item = ApiBatchFieldUpdate.from_dict(updates_item_data)

            updates.append(updates_item)

        api_item_long_operation_update_properties = cls(
            criteria=criteria,
            updates=updates,
        )

        return api_item_long_operation_update_properties
