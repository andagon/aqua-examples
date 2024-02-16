from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_field_rule_workflow_actions_update import ApiFieldRuleWorkflowActionsUpdate
    from ..models.api_field_value import ApiFieldValue


T = TypeVar("T", bound="ApiFieldRuleWorkflowTransitionUpdate")


@attr.s(auto_attribs=True)
class ApiFieldRuleWorkflowTransitionUpdate:
    """Contains all the actions which should be performed when the dictionary
    field is changed to the specified value.

        Attributes:
            value (ApiFieldValue):
            actions (List['ApiFieldRuleWorkflowActionsUpdate']): The list of actions which are executed when the value of
                the
                dictionary field is changed to the specified value.
    """

    value: "ApiFieldValue"
    actions: List["ApiFieldRuleWorkflowActionsUpdate"]

    def to_dict(self) -> Dict[str, Any]:
        value = self.value.to_dict()

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Value": value,
                "Actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_rule_workflow_actions_update import ApiFieldRuleWorkflowActionsUpdate
        from ..models.api_field_value import ApiFieldValue

        d = src_dict.copy()
        value = ApiFieldValue.from_dict(d.pop("Value"))

        actions = []
        _actions = d.pop("Actions")
        for actions_item_data in _actions:
            actions_item = ApiFieldRuleWorkflowActionsUpdate.from_dict(actions_item_data)

            actions.append(actions_item)

        api_field_rule_workflow_transition_update = cls(
            value=value,
            actions=actions,
        )

        return api_field_rule_workflow_transition_update
