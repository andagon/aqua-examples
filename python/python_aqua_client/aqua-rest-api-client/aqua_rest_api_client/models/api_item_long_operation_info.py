from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_long_operation_status import ApiLongOperationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_batch_item_operation_issue import ApiBatchItemOperationIssue


T = TypeVar("T", bound="ApiItemLongOperationInfo")


@attr.s(auto_attribs=True)
class ApiItemLongOperationInfo:
    """
    Attributes:
        info_type (str):
        status (Union[Unset, ApiLongOperationStatus]): Represents status of a long running operation.
            This enum has the following values:
              - `Aborted` Long operation has been aborted.
              - `BlockedByAnotherTask` Long operation has been blocked by another task.
              - `Failed` Long operation has failed.
              - `Finished` Long operation has finished without problems.
              - `FinishedWithWarning` Long operation has finished but there were some problems.
              - `InProgress` Long operation is in progress.
              - `Queued` Long operation has been queued, not started yet.
        done (Union[Unset, int]): Number of elements processed so far. Includes also failed elements.
        total (Union[Unset, int]): Number of all elements to be processed.
        failed (Union[Unset, int]): Number of all elements that could not be processed.
        issues (Union[Unset, None, List['ApiBatchItemOperationIssue']]): List of failures.
    """

    info_type: str
    status: Union[Unset, ApiLongOperationStatus] = UNSET
    done: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    failed: Union[Unset, int] = UNSET
    issues: Union[Unset, None, List["ApiBatchItemOperationIssue"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        info_type = self.info_type
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        done = self.done
        total = self.total
        failed = self.failed
        issues: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            if self.issues is None:
                issues = None
            else:
                issues = []
                for issues_item_data in self.issues:
                    issues_item = issues_item_data.to_dict()

                    issues.append(issues_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "InfoType": info_type,
            }
        )
        if status is not UNSET:
            field_dict["Status"] = status
        if done is not UNSET:
            field_dict["Done"] = done
        if total is not UNSET:
            field_dict["Total"] = total
        if failed is not UNSET:
            field_dict["Failed"] = failed
        if issues is not UNSET:
            field_dict["Issues"] = issues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_batch_item_operation_issue import ApiBatchItemOperationIssue

        d = src_dict.copy()
        info_type = d.pop("InfoType")

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiLongOperationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiLongOperationStatus(_status)

        done = d.pop("Done", UNSET)

        total = d.pop("Total", UNSET)

        failed = d.pop("Failed", UNSET)

        issues = []
        _issues = d.pop("Issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = ApiBatchItemOperationIssue.from_dict(issues_item_data)

            issues.append(issues_item)

        api_item_long_operation_info = cls(
            info_type=info_type,
            status=status,
            done=done,
            total=total,
            failed=failed,
            issues=issues,
        )

        api_item_long_operation_info.additional_properties = d
        return api_item_long_operation_info

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
