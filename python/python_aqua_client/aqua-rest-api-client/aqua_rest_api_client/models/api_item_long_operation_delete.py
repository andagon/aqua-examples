from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_long_operation_domain import ApiItemLongOperationDomain


T = TypeVar("T", bound="ApiItemLongOperationDelete")


@attr.s(auto_attribs=True)
class ApiItemLongOperationDelete:
    """Represents request to batch delete items.

    Attributes:
        criteria (Union[Unset, None, ApiItemLongOperationDomain]): Defines set of items to be processed.
    """

    criteria: Union[Unset, None, "ApiItemLongOperationDomain"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        criteria: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict() if self.criteria else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["Criteria"] = criteria

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        api_item_long_operation_delete = cls(
            criteria=criteria,
        )

        return api_item_long_operation_delete
