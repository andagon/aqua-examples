from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAgentCreateCopySingleAgent")


@attr.s(auto_attribs=True)
class ApiAgentCreateCopySingleAgent:
    """
    Attributes:
        create_operation (str):
        project_id (int): The id of the project the agent is copied to.
        agent_id_to_copy (int): The id of the agent wich should be copied.
        name (Union[Unset, None, str]): The name of the copied agent.
    """

    create_operation: str
    project_id: int
    agent_id_to_copy: int
    name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        create_operation = self.create_operation
        project_id = self.project_id
        agent_id_to_copy = self.agent_id_to_copy
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CreateOperation": create_operation,
                "ProjectId": project_id,
                "AgentIdToCopy": agent_id_to_copy,
            }
        )
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        create_operation = d.pop("CreateOperation")

        project_id = d.pop("ProjectId")

        agent_id_to_copy = d.pop("AgentIdToCopy")

        name = d.pop("Name", UNSET)

        api_agent_create_copy_single_agent = cls(
            create_operation=create_operation,
            project_id=project_id,
            agent_id_to_copy=agent_id_to_copy,
            name=name,
        )

        api_agent_create_copy_single_agent.additional_properties = d
        return api_agent_create_copy_single_agent

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
