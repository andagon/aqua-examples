from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAgentCreatePool")


@attr.s(auto_attribs=True)
class ApiAgentCreatePool:
    """
    Attributes:
        create_operation (str):
        project_id (int): The id of the project the agent is created in.
        name (str): The name of the agent pool.
        agents (Union[Unset, None, List[int]]): A list of agent ids included in this pool.
    """

    create_operation: str
    project_id: int
    name: str
    agents: Union[Unset, None, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        create_operation = self.create_operation
        project_id = self.project_id
        name = self.name
        agents: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.agents, Unset):
            if self.agents is None:
                agents = None
            else:
                agents = self.agents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CreateOperation": create_operation,
                "ProjectId": project_id,
                "Name": name,
            }
        )
        if agents is not UNSET:
            field_dict["Agents"] = agents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        create_operation = d.pop("CreateOperation")

        project_id = d.pop("ProjectId")

        name = d.pop("Name")

        agents = cast(List[int], d.pop("Agents", UNSET))

        api_agent_create_pool = cls(
            create_operation=create_operation,
            project_id=project_id,
            name=name,
            agents=agents,
        )

        api_agent_create_pool.additional_properties = d
        return api_agent_create_pool

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
