from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_agent_simple_status import ApiAgentSimpleStatus
from ..models.api_automation_technology import ApiAutomationTechnology

T = TypeVar("T", bound="ApiAgentBase")


@attr.s(auto_attribs=True)
class ApiAgentBase:
    """An automation agent or pool (configured in a project).

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
    """

    id: int
    name: str
    project_id: int
    code: str
    status: ApiAgentSimpleStatus
    supported_technologies: List[ApiAutomationTechnology]
    agent_type: str

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Id": id,
                "Name": name,
                "ProjectId": project_id,
                "Code": code,
                "Status": status,
                "SupportedTechnologies": supported_technologies,
                "AgentType": agent_type,
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

        api_agent_base = cls(
            id=id,
            name=name,
            project_id=project_id,
            code=code,
            status=status,
            supported_technologies=supported_technologies,
            agent_type=agent_type,
        )

        return api_agent_base
