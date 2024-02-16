from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAgentPatchUpdatePool")


@attr.s(auto_attribs=True)
class ApiAgentPatchUpdatePool:
    """
    Attributes:
        patch_operation (str):
        new_name (Union[Unset, None, str]): New name of the pool.
        agents (Union[Unset, None, List[int]]): A list of agent ids included in this pool.
    """

    patch_operation: str
    new_name: Union[Unset, None, str] = UNSET
    agents: Union[Unset, None, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_operation = self.patch_operation
        new_name = self.new_name
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
                "PatchOperation": patch_operation,
            }
        )
        if new_name is not UNSET:
            field_dict["NewName"] = new_name
        if agents is not UNSET:
            field_dict["Agents"] = agents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_operation = d.pop("PatchOperation")

        new_name = d.pop("NewName", UNSET)

        agents = cast(List[int], d.pop("Agents", UNSET))

        api_agent_patch_update_pool = cls(
            patch_operation=patch_operation,
            new_name=new_name,
            agents=agents,
        )

        api_agent_patch_update_pool.additional_properties = d
        return api_agent_patch_update_pool

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
