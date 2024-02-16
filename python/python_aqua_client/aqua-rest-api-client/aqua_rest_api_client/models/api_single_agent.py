from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_agent_execution_status import ApiAgentExecutionStatus
from ..models.api_agent_simple_status import ApiAgentSimpleStatus
from ..models.api_automation_technology import ApiAutomationTechnology

T = TypeVar("T", bound="ApiSingleAgent")


@attr.s(auto_attribs=True)
class ApiSingleAgent:
    """
    Attributes:
        id (int): The id of the agent.
        name (str): The name of the agent.
        project_id (int): The id of the project the agent is created in.
        code (str): The code of the agent.
        status (ApiAgentSimpleStatus): Represents current status of an automation agent
            This enum has the following values:
              - `Available`
              - `BlockedOrNoAgents`
              - `NoResponseYet`
              - `PartiallyAvailable`
              - `Unavailable`
        supported_technologies (List[ApiAutomationTechnology]): The technologies supported by this agent.
        agent_type (str):
        execution_status (ApiAgentExecutionStatus): Represents current execution status of an automation agent
            This enum has the following values:
              - `Executing`
              - `Idle`
              - `Offline`
    """

    id: int
    name: str
    project_id: int
    code: str
    status: ApiAgentSimpleStatus
    supported_technologies: List[ApiAutomationTechnology]
    agent_type: str
    execution_status: ApiAgentExecutionStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        project_id = self.project_id
        code = self.code
        status = self.status.value

        supported_technologies = []
        for supported_technologies_item_data in self.supported_technologies:
            supported_technologies_item = supported_technologies_item_data.value

            supported_technologies.append(supported_technologies_item)

        agent_type = self.agent_type
        execution_status = self.execution_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "Name": name,
                "ProjectId": project_id,
                "Code": code,
                "Status": status,
                "SupportedTechnologies": supported_technologies,
                "AgentType": agent_type,
                "ExecutionStatus": execution_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        name = d.pop("Name")

        project_id = d.pop("ProjectId")

        code = d.pop("Code")

        status = ApiAgentSimpleStatus(d.pop("Status"))

        supported_technologies = []
        _supported_technologies = d.pop("SupportedTechnologies")
        for supported_technologies_item_data in _supported_technologies:
            supported_technologies_item = ApiAutomationTechnology(supported_technologies_item_data)

            supported_technologies.append(supported_technologies_item)

        agent_type = d.pop("AgentType")

        execution_status = ApiAgentExecutionStatus(d.pop("ExecutionStatus"))

        api_single_agent = cls(
            id=id,
            name=name,
            project_id=project_id,
            code=code,
            status=status,
            supported_technologies=supported_technologies,
            agent_type=agent_type,
            execution_status=execution_status,
        )

        api_single_agent.additional_properties = d
        return api_single_agent

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
