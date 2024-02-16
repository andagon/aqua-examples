from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiAgentPatchUpdateSingleAgent")


@attr.s(auto_attribs=True)
class ApiAgentPatchUpdateSingleAgent:
    """
    Attributes:
        patch_operation (str):
        new_name (str): New name of the single agent.
    """

    patch_operation: str
    new_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_operation = self.patch_operation
        new_name = self.new_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PatchOperation": patch_operation,
                "NewName": new_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_operation = d.pop("PatchOperation")

        new_name = d.pop("NewName")

        api_agent_patch_update_single_agent = cls(
            patch_operation=patch_operation,
            new_name=new_name,
        )

        api_agent_patch_update_single_agent.additional_properties = d
        return api_agent_patch_update_single_agent

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
