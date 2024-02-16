from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAutomatedTestScenarioExecutionRequest")


@attr.s(auto_attribs=True)
class ApiAutomatedTestScenarioExecutionRequest:
    """Base class for the different execution requests which can be used to start
    an automated execution of a test scenario.

        Attributes:
            execution_type (str):
            agent_id (Union[Unset, None, int]): The id of the agent which should be used as a fallback when
                no agent is specified for a test job.
            sequential (Union[Unset, bool]): If true test jobs will be executed sequentially.
    """

    execution_type: str
    agent_id: Union[Unset, None, int] = UNSET
    sequential: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        execution_type = self.execution_type
        agent_id = self.agent_id
        sequential = self.sequential

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ExecutionType": execution_type,
            }
        )
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if sequential is not UNSET:
            field_dict["Sequential"] = sequential

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        execution_type = d.pop("ExecutionType")

        agent_id = d.pop("AgentId", UNSET)

        sequential = d.pop("Sequential", UNSET)

        api_automated_test_scenario_execution_request = cls(
            execution_type=execution_type,
            agent_id=agent_id,
            sequential=sequential,
        )

        return api_automated_test_scenario_execution_request
