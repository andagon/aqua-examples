from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_batch_item_update_issue_details_type import ApiBatchItemUpdateIssueDetailsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBatchItemUpdateIssueDetailsBase")


@attr.s(auto_attribs=True)
class ApiBatchItemUpdateIssueDetailsBase:
    """
    Attributes:
        details_type (str):
        type (Union[Unset, ApiBatchItemUpdateIssueDetailsType]): Represents reason of a failure of batch-item update
            operation
            This enum has the following values:
              - `Denied` Access to the item has been denied
              - `Failure` Uncategorized failure
              - `FieldIncompatible` A field could not be converted due to incompatibility
              - `Locked` Item was currently edited by someone
              - `NotFound` Item has not been found
              - `ValueNotAllowed` When updating an item, the given value was not allowed (e.g. due to format, length, denied
            by workflow rules etc.)
    """

    details_type: str
    type: Union[Unset, ApiBatchItemUpdateIssueDetailsType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        details_type = self.details_type
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "DetailsType": details_type,
            }
        )
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        details_type = d.pop("DetailsType")

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiBatchItemUpdateIssueDetailsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiBatchItemUpdateIssueDetailsType(_type)

        api_batch_item_update_issue_details_base = cls(
            details_type=details_type,
            type=type,
        )

        return api_batch_item_update_issue_details_base
