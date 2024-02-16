from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_long_operation_domain import ApiItemLongOperationDomain


T = TypeVar("T", bound="ApiItemLongOperationArchive")


@attr.s(auto_attribs=True)
class ApiItemLongOperationArchive:
    """Represents request to batch archive (or un-archive) items.

    Attributes:
        criteria (Union[Unset, None, ApiItemLongOperationDomain]): Defines set of items to be processed.
        archive (Union[Unset, bool]): If true, the items will be marked as archived.
            If false, the items will be marked as non-archived.
    """

    criteria: Union[Unset, None, "ApiItemLongOperationDomain"] = UNSET
    archive: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        criteria: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict() if self.criteria else None

        archive = self.archive

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["Criteria"] = criteria
        if archive is not UNSET:
            field_dict["Archive"] = archive

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

        archive = d.pop("Archive", UNSET)

        api_item_long_operation_archive = cls(
            criteria=criteria,
            archive=archive,
        )

        return api_item_long_operation_archive
