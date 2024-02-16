from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_batch_item_operation_issue_type import ApiBatchItemOperationIssueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_batch_item_update_issue_details_base import ApiBatchItemUpdateIssueDetailsBase
    from ..models.api_item_identifier import ApiItemIdentifier


T = TypeVar("T", bound="ApiBatchItemOperationIssue")


@attr.s(auto_attribs=True)
class ApiBatchItemOperationIssue:
    """Represents a failure of batch-item update operation for a single item.

    Attributes:
        item (Union[Unset, None, ApiItemIdentifier]):
        reason (Union[Unset, None, ApiBatchItemUpdateIssueDetailsBase]):
        issue_type (Union[Unset, ApiBatchItemOperationIssueType]):
            This enum has the following values:
              - `FieldError`
              - `FieldInformation`
              - `FieldWarning`
              - `ItemError`
              - `ItemInformation`
              - `ItemWarning`
    """

    item: Union[Unset, None, "ApiItemIdentifier"] = UNSET
    reason: Union[Unset, None, "ApiBatchItemUpdateIssueDetailsBase"] = UNSET
    issue_type: Union[Unset, ApiBatchItemOperationIssueType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict() if self.item else None

        reason: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict() if self.reason else None

        issue_type: Union[Unset, str] = UNSET
        if not isinstance(self.issue_type, Unset):
            issue_type = self.issue_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item is not UNSET:
            field_dict["Item"] = item
        if reason is not UNSET:
            field_dict["Reason"] = reason
        if issue_type is not UNSET:
            field_dict["IssueType"] = issue_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_batch_item_update_issue_details_base import ApiBatchItemUpdateIssueDetailsBase
        from ..models.api_item_identifier import ApiItemIdentifier

        d = src_dict.copy()
        _item = d.pop("Item", UNSET)
        item: Union[Unset, None, ApiItemIdentifier]
        if _item is None:
            item = None
        elif isinstance(_item, Unset):
            item = UNSET
        else:
            item = ApiItemIdentifier.from_dict(_item)

        _reason = d.pop("Reason", UNSET)
        reason: Union[Unset, None, ApiBatchItemUpdateIssueDetailsBase]
        if _reason is None:
            reason = None
        elif isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ApiBatchItemUpdateIssueDetailsBase.from_dict(_reason)

        _issue_type = d.pop("IssueType", UNSET)
        issue_type: Union[Unset, ApiBatchItemOperationIssueType]
        if isinstance(_issue_type, Unset):
            issue_type = UNSET
        else:
            issue_type = ApiBatchItemOperationIssueType(_issue_type)

        api_batch_item_operation_issue = cls(
            item=item,
            reason=reason,
            issue_type=issue_type,
        )

        return api_batch_item_operation_issue
