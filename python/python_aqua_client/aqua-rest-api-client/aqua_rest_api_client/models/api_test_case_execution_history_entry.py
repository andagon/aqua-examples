from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_test_case_run_status import ApiTestCaseRunStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value_date_time import ApiFieldValueDateTime


T = TypeVar("T", bound="ApiTestCaseExecutionHistoryEntry")


@attr.s(auto_attribs=True)
class ApiTestCaseExecutionHistoryEntry:
    """Contains history information for a single test execution.

    Attributes:
        execution_status (Union[Unset, ApiTestCaseRunStatus]): Identifies the status of an execution of a test case.
            This enum has the following values:
              - `Blocked` Execution has been blocked
              - `Failed` Execution has failed
              - `NotApplicable` Execution status is not applicable to result
              - `NotCompleted` Execution has started but not completed yet
              - `NotRun` Never executed
              - `Passed` Execution has passed
        execution_date (Union[Unset, None, ApiFieldValueDateTime]):
        test_scenario_id (Union[Unset, None, int]): The id of test scenario.
    """

    execution_status: Union[Unset, ApiTestCaseRunStatus] = UNSET
    execution_date: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    test_scenario_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        execution_status: Union[Unset, str] = UNSET
        if not isinstance(self.execution_status, Unset):
            execution_status = self.execution_status.value

        execution_date: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_date, Unset):
            execution_date = self.execution_date.to_dict() if self.execution_date else None

        test_scenario_id = self.test_scenario_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if execution_status is not UNSET:
            field_dict["ExecutionStatus"] = execution_status
        if execution_date is not UNSET:
            field_dict["ExecutionDate"] = execution_date
        if test_scenario_id is not UNSET:
            field_dict["TestScenarioId"] = test_scenario_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_date_time import ApiFieldValueDateTime

        d = src_dict.copy()
        _execution_status = d.pop("ExecutionStatus", UNSET)
        execution_status: Union[Unset, ApiTestCaseRunStatus]
        if isinstance(_execution_status, Unset):
            execution_status = UNSET
        else:
            execution_status = ApiTestCaseRunStatus(_execution_status)

        _execution_date = d.pop("ExecutionDate", UNSET)
        execution_date: Union[Unset, None, ApiFieldValueDateTime]
        if _execution_date is None:
            execution_date = None
        elif isinstance(_execution_date, Unset):
            execution_date = UNSET
        else:
            execution_date = ApiFieldValueDateTime.from_dict(_execution_date)

        test_scenario_id = d.pop("TestScenarioId", UNSET)

        api_test_case_execution_history_entry = cls(
            execution_status=execution_status,
            execution_date=execution_date,
            test_scenario_id=test_scenario_id,
        )

        return api_test_case_execution_history_entry
