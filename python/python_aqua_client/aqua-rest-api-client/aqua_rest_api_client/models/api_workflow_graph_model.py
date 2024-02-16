from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_workflow_graph_node_model import ApiWorkflowGraphNodeModel
    from ..models.api_workflow_graph_transition_model import ApiWorkflowGraphTransitionModel


T = TypeVar("T", bound="ApiWorkflowGraphModel")


@attr.s(auto_attribs=True)
class ApiWorkflowGraphModel:
    """Represents a workflow graph.

    Attributes:
        nodes (Union[Unset, None, List['ApiWorkflowGraphNodeModel']]): List of nodes with coordinates.
        transitions (Union[Unset, None, List['ApiWorkflowGraphTransitionModel']]): List of transitions.
    """

    nodes: Union[Unset, None, List["ApiWorkflowGraphNodeModel"]] = UNSET
    transitions: Union[Unset, None, List["ApiWorkflowGraphTransitionModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        nodes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            if self.nodes is None:
                nodes = None
            else:
                nodes = []
                for nodes_item_data in self.nodes:
                    nodes_item = nodes_item_data.to_dict()

                    nodes.append(nodes_item)

        transitions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transitions, Unset):
            if self.transitions is None:
                transitions = None
            else:
                transitions = []
                for transitions_item_data in self.transitions:
                    transitions_item = transitions_item_data.to_dict()

                    transitions.append(transitions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if nodes is not UNSET:
            field_dict["Nodes"] = nodes
        if transitions is not UNSET:
            field_dict["Transitions"] = transitions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_workflow_graph_node_model import ApiWorkflowGraphNodeModel
        from ..models.api_workflow_graph_transition_model import ApiWorkflowGraphTransitionModel

        d = src_dict.copy()
        nodes = []
        _nodes = d.pop("Nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = ApiWorkflowGraphNodeModel.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        transitions = []
        _transitions = d.pop("Transitions", UNSET)
        for transitions_item_data in _transitions or []:
            transitions_item = ApiWorkflowGraphTransitionModel.from_dict(transitions_item_data)

            transitions.append(transitions_item)

        api_workflow_graph_model = cls(
            nodes=nodes,
            transitions=transitions,
        )

        return api_workflow_graph_model
