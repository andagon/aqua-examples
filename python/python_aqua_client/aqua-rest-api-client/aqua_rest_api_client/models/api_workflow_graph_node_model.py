from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiWorkflowGraphNodeModel")


@attr.s(auto_attribs=True)
class ApiWorkflowGraphNodeModel:
    """Represents a workflow graph node.

    Attributes:
        name (Union[Unset, None, str]): node name.
        x (Union[Unset, float]): X coordinate to draw.
        y (Union[Unset, float]): Y coordinate to draw.
    """

    name: Union[Unset, None, str] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        x = self.x
        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if x is not UNSET:
            field_dict["X"] = x
        if y is not UNSET:
            field_dict["Y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        x = d.pop("X", UNSET)

        y = d.pop("Y", UNSET)

        api_workflow_graph_node_model = cls(
            name=name,
            x=x,
            y=y,
        )

        return api_workflow_graph_node_model
