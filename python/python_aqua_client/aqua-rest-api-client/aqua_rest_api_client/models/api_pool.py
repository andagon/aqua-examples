from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.api_agent_simple_status import ApiAgentSimpleStatus
from ..models.api_automation_technology import ApiAutomationTechnology

if TYPE_CHECKING:
    from ..models.api_agent_id_and_name import ApiAgentIdAndName


T = TypeVar("T", bound="ApiPool")


@attr.s(auto_attribs=True)
class ApiPool:
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
        agents (List['ApiAgentIdAndName']): List of agent ids included in this pool.
    """

    id: int
    name: str
    project_id: int
    code: str
    status: ApiAgentSimpleStatus
    supported_technologies: List[ApiAutomationTechnology]
    agent_type: str
    agents: List["ApiAgentIdAndName"]
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
        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()

            agents.append(agents_item)

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
                "Agents": agents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_agent_id_and_name import ApiAgentIdAndName

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

        agents = []
        _agents = d.pop("Agents")
        for agents_item_data in _agents:
            agents_item = ApiAgentIdAndName.from_dict(agents_item_data)

            agents.append(agents_item)

        api_pool = cls(
            id=id,
            name=name,
            project_id=project_id,
            code=code,
            status=status,
            supported_technologies=supported_technologies,
            agent_type=agent_type,
            agents=agents,
        )

        api_pool.additional_properties = d
        return api_pool

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
