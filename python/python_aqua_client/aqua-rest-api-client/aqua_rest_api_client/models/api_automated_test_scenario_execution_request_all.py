from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAutomatedTestScenarioExecutionRequestAll")


@attr.s(auto_attribs=True)
class ApiAutomatedTestScenarioExecutionRequestAll:
    """
    Attributes:
        execution_type (str):
        agent_id (Union[Unset, None, int]): The id of the agent which should be used as a fallback when
            no agent is specified for a test job.
        sequential (Union[Unset, bool]): If true test jobs will be executed sequentially.
    """

    execution_type: str
    agent_id: Union[Unset, None, int] = UNSET
    sequential: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        execution_type = self.execution_type
        agent_id = self.agent_id
        sequential = self.sequential

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        api_automated_test_scenario_execution_request_all = cls(
            execution_type=execution_type,
            agent_id=agent_id,
            sequential=sequential,
        )

        api_automated_test_scenario_execution_request_all.additional_properties = d
        return api_automated_test_scenario_execution_request_all

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
