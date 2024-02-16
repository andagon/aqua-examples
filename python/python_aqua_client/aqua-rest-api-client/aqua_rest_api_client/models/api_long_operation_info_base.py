from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_long_operation_status import ApiLongOperationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLongOperationInfoBase")


@attr.s(auto_attribs=True)
class ApiLongOperationInfoBase:
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
    """

    info_type: str
    status: Union[Unset, ApiLongOperationStatus] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        info_type = self.info_type
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "InfoType": info_type,
            }
        )
        if status is not UNSET:
            field_dict["Status"] = status

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

        api_long_operation_info_base = cls(
            info_type=info_type,
            status=status,
        )

        return api_long_operation_info_base
