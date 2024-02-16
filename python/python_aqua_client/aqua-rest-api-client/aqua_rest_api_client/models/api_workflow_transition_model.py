from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_workflow_node_model import ApiWorkflowNodeModel


T = TypeVar("T", bound="ApiWorkflowTransitionModel")


@attr.s(auto_attribs=True)
class ApiWorkflowTransitionModel:
    """Represents a workflow transition.

    Attributes:
        node_from (Union[Unset, None, ApiWorkflowNodeModel]): Represents a workflow node
        node_to (Union[Unset, None, ApiWorkflowNodeModel]): Represents a workflow node
    """

    node_from: Union[Unset, None, "ApiWorkflowNodeModel"] = UNSET
    node_to: Union[Unset, None, "ApiWorkflowNodeModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        node_from: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.node_from, Unset):
            node_from = self.node_from.to_dict() if self.node_from else None

        node_to: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.node_to, Unset):
            node_to = self.node_to.to_dict() if self.node_to else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if node_from is not UNSET:
            field_dict["NodeFrom"] = node_from
        if node_to is not UNSET:
            field_dict["NodeTo"] = node_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_workflow_node_model import ApiWorkflowNodeModel

        d = src_dict.copy()
        _node_from = d.pop("NodeFrom", UNSET)
        node_from: Union[Unset, None, ApiWorkflowNodeModel]
        if _node_from is None:
            node_from = None
        elif isinstance(_node_from, Unset):
            node_from = UNSET
        else:
            node_from = ApiWorkflowNodeModel.from_dict(_node_from)

        _node_to = d.pop("NodeTo", UNSET)
        node_to: Union[Unset, None, ApiWorkflowNodeModel]
        if _node_to is None:
            node_to = None
        elif isinstance(_node_to, Unset):
            node_to = UNSET
        else:
            node_to = ApiWorkflowNodeModel.from_dict(_node_to)

        api_workflow_transition_model = cls(
            node_from=node_from,
            node_to=node_to,
        )

        return api_workflow_transition_model
