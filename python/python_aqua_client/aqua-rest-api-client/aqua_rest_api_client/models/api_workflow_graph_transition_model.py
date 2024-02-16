from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiWorkflowGraphTransitionModel")


@attr.s(auto_attribs=True)
class ApiWorkflowGraphTransitionModel:
    """Represents a workflow graph transition.

    Attributes:
        node_from (Union[Unset, None, str]): Node name from which you are changing.
        node_to (Union[Unset, None, str]): Node name to which you want to switch.
    """

    node_from: Union[Unset, None, str] = UNSET
    node_to: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        node_from = self.node_from
        node_to = self.node_to

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if node_from is not UNSET:
            field_dict["NodeFrom"] = node_from
        if node_to is not UNSET:
            field_dict["NodeTo"] = node_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_from = d.pop("NodeFrom", UNSET)

        node_to = d.pop("NodeTo", UNSET)

        api_workflow_graph_transition_model = cls(
            node_from=node_from,
            node_to=node_to,
        )

        return api_workflow_graph_transition_model
