from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_workflow_graph_model import ApiWorkflowGraphModel
    from ..models.api_workflow_node_model import ApiWorkflowNodeModel
    from ..models.api_workflow_transition_model import ApiWorkflowTransitionModel


T = TypeVar("T", bound="ApiWorkflow")


@attr.s(auto_attribs=True)
class ApiWorkflow:
    """Represents a workflow.

    Attributes:
        nodes (Union[Unset, None, List['ApiWorkflowNodeModel']]): A list of all workflow nodes.
        actions (Union[Unset, None, List['ApiWorkflowTransitionModel']]): A list of all workflow transitions.
        graph (Union[Unset, None, ApiWorkflowGraphModel]): Represents a workflow graph.
    """

    nodes: Union[Unset, None, List["ApiWorkflowNodeModel"]] = UNSET
    actions: Union[Unset, None, List["ApiWorkflowTransitionModel"]] = UNSET
    graph: Union[Unset, None, "ApiWorkflowGraphModel"] = UNSET

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

        actions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            if self.actions is None:
                actions = None
            else:
                actions = []
                for actions_item_data in self.actions:
                    actions_item = actions_item_data.to_dict()

                    actions.append(actions_item)

        graph: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.graph, Unset):
            graph = self.graph.to_dict() if self.graph else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if nodes is not UNSET:
            field_dict["Nodes"] = nodes
        if actions is not UNSET:
            field_dict["Actions"] = actions
        if graph is not UNSET:
            field_dict["Graph"] = graph

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_workflow_graph_model import ApiWorkflowGraphModel
        from ..models.api_workflow_node_model import ApiWorkflowNodeModel
        from ..models.api_workflow_transition_model import ApiWorkflowTransitionModel

        d = src_dict.copy()
        nodes = []
        _nodes = d.pop("Nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = ApiWorkflowNodeModel.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        actions = []
        _actions = d.pop("Actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = ApiWorkflowTransitionModel.from_dict(actions_item_data)

            actions.append(actions_item)

        _graph = d.pop("Graph", UNSET)
        graph: Union[Unset, None, ApiWorkflowGraphModel]
        if _graph is None:
            graph = None
        elif isinstance(_graph, Unset):
            graph = UNSET
        else:
            graph = ApiWorkflowGraphModel.from_dict(_graph)

        api_workflow = cls(
            nodes=nodes,
            actions=actions,
            graph=graph,
        )

        return api_workflow
