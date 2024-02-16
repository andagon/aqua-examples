from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_test_case_run_status import ApiTestCaseRunStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestJobStatisticsEntry")


@attr.s(auto_attribs=True)
class ApiTestJobStatisticsEntry:
    """Holds statistical information for test jobs with
    a single last execution status.

        Attributes:
            status (Union[Unset, ApiTestCaseRunStatus]): Identifies the status of an execution of a test case.
                This enum has the following values:
                  - `Blocked` Execution has been blocked
                  - `Failed` Execution has failed
                  - `NotApplicable` Execution status is not applicable to result
                  - `NotCompleted` Execution has started but not completed yet
                  - `NotRun` Never executed
                  - `Passed` Execution has passed
            title (Union[Unset, None, str]): The title of the execution status.
            count (Union[Unset, int]): The number of test jobs which reached this status
                during their last execution.
            percentage (Union[Unset, float]): The percentage of test jobs which reached this status
                during their last execution.
    """

    status: Union[Unset, ApiTestCaseRunStatus] = UNSET
    title: Union[Unset, None, str] = UNSET
    count: Union[Unset, int] = UNSET
    percentage: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        title = self.title
        count = self.count
        percentage = self.percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status is not UNSET:
            field_dict["Status"] = status
        if title is not UNSET:
            field_dict["Title"] = title
        if count is not UNSET:
            field_dict["Count"] = count
        if percentage is not UNSET:
            field_dict["Percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiTestCaseRunStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiTestCaseRunStatus(_status)

        title = d.pop("Title", UNSET)

        count = d.pop("Count", UNSET)

        percentage = d.pop("Percentage", UNSET)

        api_test_job_statistics_entry = cls(
            status=status,
            title=title,
            count=count,
            percentage=percentage,
        )

        return api_test_job_statistics_entry
