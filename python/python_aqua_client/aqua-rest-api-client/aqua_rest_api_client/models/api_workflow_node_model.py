from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiWorkflowNodeModel")


@attr.s(auto_attribs=True)
class ApiWorkflowNodeModel:
    """Represents a workflow node

    Attributes:
        name (Union[Unset, None, str]): node name.
        is_initial_node (Union[Unset, bool]): true if this node is intial node.
    """

    name: Union[Unset, None, str] = UNSET
    is_initial_node: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_initial_node = self.is_initial_node

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if is_initial_node is not UNSET:
            field_dict["IsInitialNode"] = is_initial_node

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        is_initial_node = d.pop("IsInitialNode", UNSET)

        api_workflow_node_model = cls(
            name=name,
            is_initial_node=is_initial_node,
        )

        return api_workflow_node_model
