from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAutomatedTestScenarioExecutionResponse")


@attr.s(auto_attribs=True)
class ApiAutomatedTestScenarioExecutionResponse:
    """
    Attributes:
        test_scenario_execution_id (Union[Unset, int]): Contains the id of the test scenario execution.
        long_running_task_guid (Union[Unset, None, str]): Contains the long running task guid.
    """

    test_scenario_execution_id: Union[Unset, int] = UNSET
    long_running_task_guid: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        test_scenario_execution_id = self.test_scenario_execution_id
        long_running_task_guid = self.long_running_task_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if test_scenario_execution_id is not UNSET:
            field_dict["TestScenarioExecutionId"] = test_scenario_execution_id
        if long_running_task_guid is not UNSET:
            field_dict["LongRunningTaskGuid"] = long_running_task_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        test_scenario_execution_id = d.pop("TestScenarioExecutionId", UNSET)

        long_running_task_guid = d.pop("LongRunningTaskGuid", UNSET)

        api_automated_test_scenario_execution_response = cls(
            test_scenario_execution_id=test_scenario_execution_id,
            long_running_task_guid=long_running_task_guid,
        )

        return api_automated_test_scenario_execution_response
