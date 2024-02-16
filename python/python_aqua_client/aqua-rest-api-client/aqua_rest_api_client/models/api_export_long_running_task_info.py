from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_long_operation_status import ApiLongOperationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiExportLongRunningTaskInfo")


@attr.s(auto_attribs=True)
class ApiExportLongRunningTaskInfo:
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
        export_file_guid (Union[Unset, None, str]): When finished, this will contain the file guid to the export file
    """

    info_type: str
    status: Union[Unset, ApiLongOperationStatus] = UNSET
    done: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    failed: Union[Unset, int] = UNSET
    export_file_guid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        info_type = self.info_type
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        done = self.done
        total = self.total
        failed = self.failed
        export_file_guid = self.export_file_guid

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
        if export_file_guid is not UNSET:
            field_dict["ExportFileGuid"] = export_file_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        export_file_guid = d.pop("ExportFileGuid", UNSET)

        api_export_long_running_task_info = cls(
            info_type=info_type,
            status=status,
            done=done,
            total=total,
            failed=failed,
            export_file_guid=export_file_guid,
        )

        api_export_long_running_task_info.additional_properties = d
        return api_export_long_running_task_info

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
