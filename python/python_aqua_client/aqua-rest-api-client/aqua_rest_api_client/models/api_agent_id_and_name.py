from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAgentIdAndName")


@attr.s(auto_attribs=True)
class ApiAgentIdAndName:
    """Some minimal identifying information for an agent.

    Attributes:
        name (str): The name of the agent.
        id (Union[Unset, None, int]): The id of the agent. When the id is not provided, the agent
            has been deleted.
    """

    name: str
    id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Name": name,
            }
        )
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        id = d.pop("Id", UNSET)

        api_agent_id_and_name = cls(
            name=name,
            id=id,
        )

        return api_agent_id_and_name
