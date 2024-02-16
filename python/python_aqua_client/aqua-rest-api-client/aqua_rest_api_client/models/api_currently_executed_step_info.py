from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCurrentlyExecutedStepInfo")


@attr.s(auto_attribs=True)
class ApiCurrentlyExecutedStepInfo:
    """Encapsulates basic information about currently executing task on an agent.

    Attributes:
        project_id (Union[Unset, int]): The id of the project where the execution is performed
        test_step_execution_id (Union[Unset, int]): The id of the step execution
        test_job_execution_id (Union[Unset, int]): The id of the execution
        test_case_id (Union[Unset, int]): The id of related test case.
        test_scenario_id (Union[Unset, int]): The id of related test scenario (or 0 if none).
        can_view_test_scenario (Union[Unset, None, ApiPermissionResult]): Defined possible results of a permission
            check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_view_test_case (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_view_test_job_execution (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
    """

    project_id: Union[Unset, int] = UNSET
    test_step_execution_id: Union[Unset, int] = UNSET
    test_job_execution_id: Union[Unset, int] = UNSET
    test_case_id: Union[Unset, int] = UNSET
    test_scenario_id: Union[Unset, int] = UNSET
    can_view_test_scenario: Union[Unset, None, ApiPermissionResult] = UNSET
    can_view_test_case: Union[Unset, ApiPermissionResult] = UNSET
    can_view_test_job_execution: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        test_step_execution_id = self.test_step_execution_id
        test_job_execution_id = self.test_job_execution_id
        test_case_id = self.test_case_id
        test_scenario_id = self.test_scenario_id
        can_view_test_scenario: Union[Unset, None, str] = UNSET
        if not isinstance(self.can_view_test_scenario, Unset):
            can_view_test_scenario = self.can_view_test_scenario.value if self.can_view_test_scenario else None

        can_view_test_case: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_test_case, Unset):
            can_view_test_case = self.can_view_test_case.value

        can_view_test_job_execution: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_test_job_execution, Unset):
            can_view_test_job_execution = self.can_view_test_job_execution.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if test_step_execution_id is not UNSET:
            field_dict["TestStepExecutionId"] = test_step_execution_id
        if test_job_execution_id is not UNSET:
            field_dict["TestJobExecutionId"] = test_job_execution_id
        if test_case_id is not UNSET:
            field_dict["TestCaseId"] = test_case_id
        if test_scenario_id is not UNSET:
            field_dict["TestScenarioId"] = test_scenario_id
        if can_view_test_scenario is not UNSET:
            field_dict["CanViewTestScenario"] = can_view_test_scenario
        if can_view_test_case is not UNSET:
            field_dict["CanViewTestCase"] = can_view_test_case
        if can_view_test_job_execution is not UNSET:
            field_dict["CanViewTestJobExecution"] = can_view_test_job_execution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = d.pop("ProjectId", UNSET)

        test_step_execution_id = d.pop("TestStepExecutionId", UNSET)

        test_job_execution_id = d.pop("TestJobExecutionId", UNSET)

        test_case_id = d.pop("TestCaseId", UNSET)

        test_scenario_id = d.pop("TestScenarioId", UNSET)

        _can_view_test_scenario = d.pop("CanViewTestScenario", UNSET)
        can_view_test_scenario: Union[Unset, None, ApiPermissionResult]
        if _can_view_test_scenario is None:
            can_view_test_scenario = None
        elif isinstance(_can_view_test_scenario, Unset):
            can_view_test_scenario = UNSET
        else:
            can_view_test_scenario = ApiPermissionResult(_can_view_test_scenario)

        _can_view_test_case = d.pop("CanViewTestCase", UNSET)
        can_view_test_case: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_test_case, Unset):
            can_view_test_case = UNSET
        else:
            can_view_test_case = ApiPermissionResult(_can_view_test_case)

        _can_view_test_job_execution = d.pop("CanViewTestJobExecution", UNSET)
        can_view_test_job_execution: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_test_job_execution, Unset):
            can_view_test_job_execution = UNSET
        else:
            can_view_test_job_execution = ApiPermissionResult(_can_view_test_job_execution)

        api_currently_executed_step_info = cls(
            project_id=project_id,
            test_step_execution_id=test_step_execution_id,
            test_job_execution_id=test_job_execution_id,
            test_case_id=test_case_id,
            test_scenario_id=test_scenario_id,
            can_view_test_scenario=can_view_test_scenario,
            can_view_test_case=can_view_test_case,
            can_view_test_job_execution=can_view_test_job_execution,
        )

        return api_currently_executed_step_info
