from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_batch_item_update_issue_details_type import ApiBatchItemUpdateIssueDetailsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBatchItemUpdateFieldIssueDetails")


@attr.s(auto_attribs=True)
class ApiBatchItemUpdateFieldIssueDetails:
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
        source_field_name (Union[Unset, None, str]):
        target_field_name (Union[Unset, None, str]):
    """

    details_type: str
    type: Union[Unset, ApiBatchItemUpdateIssueDetailsType] = UNSET
    source_field_name: Union[Unset, None, str] = UNSET
    target_field_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        details_type = self.details_type
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        source_field_name = self.source_field_name
        target_field_name = self.target_field_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DetailsType": details_type,
            }
        )
        if type is not UNSET:
            field_dict["Type"] = type
        if source_field_name is not UNSET:
            field_dict["SourceFieldName"] = source_field_name
        if target_field_name is not UNSET:
            field_dict["TargetFieldName"] = target_field_name

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

        source_field_name = d.pop("SourceFieldName", UNSET)

        target_field_name = d.pop("TargetFieldName", UNSET)

        api_batch_item_update_field_issue_details = cls(
            details_type=details_type,
            type=type,
            source_field_name=source_field_name,
            target_field_name=target_field_name,
        )

        api_batch_item_update_field_issue_details.additional_properties = d
        return api_batch_item_update_field_issue_details

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
