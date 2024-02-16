import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_test_case_run_status import ApiTestCaseRunStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLastExecutionInfo")


@attr.s(auto_attribs=True)
class ApiLastExecutionInfo:
    """Contains information about the last execution.

    Attributes:
        last_execution_id (Union[Unset, None, int]): The id of the last execution.
        last_execution_status (Union[Unset, ApiTestCaseRunStatus]): Identifies the status of an execution of a test
            case.
            This enum has the following values:
              - `Blocked` Execution has been blocked
              - `Failed` Execution has failed
              - `NotApplicable` Execution status is not applicable to result
              - `NotCompleted` Execution has started but not completed yet
              - `NotRun` Never executed
              - `Passed` Execution has passed
        last_execution_date (Union[Unset, None, datetime.datetime]): Contains the last test job execution status date.
    """

    last_execution_id: Union[Unset, None, int] = UNSET
    last_execution_status: Union[Unset, ApiTestCaseRunStatus] = UNSET
    last_execution_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        last_execution_id = self.last_execution_id
        last_execution_status: Union[Unset, str] = UNSET
        if not isinstance(self.last_execution_status, Unset):
            last_execution_status = self.last_execution_status.value

        last_execution_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_execution_date, Unset):
            last_execution_date = self.last_execution_date.isoformat() if self.last_execution_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if last_execution_id is not UNSET:
            field_dict["LastExecutionId"] = last_execution_id
        if last_execution_status is not UNSET:
            field_dict["LastExecutionStatus"] = last_execution_status
        if last_execution_date is not UNSET:
            field_dict["LastExecutionDate"] = last_execution_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_execution_id = d.pop("LastExecutionId", UNSET)

        _last_execution_status = d.pop("LastExecutionStatus", UNSET)
        last_execution_status: Union[Unset, ApiTestCaseRunStatus]
        if isinstance(_last_execution_status, Unset):
            last_execution_status = UNSET
        else:
            last_execution_status = ApiTestCaseRunStatus(_last_execution_status)

        _last_execution_date = d.pop("LastExecutionDate", UNSET)
        last_execution_date: Union[Unset, None, datetime.datetime]
        if _last_execution_date is None:
            last_execution_date = None
        elif isinstance(_last_execution_date, Unset):
            last_execution_date = UNSET
        else:
            last_execution_date = isoparse(_last_execution_date)

        api_last_execution_info = cls(
            last_execution_id=last_execution_id,
            last_execution_status=last_execution_status,
            last_execution_date=last_execution_date,
        )

        return api_last_execution_info
