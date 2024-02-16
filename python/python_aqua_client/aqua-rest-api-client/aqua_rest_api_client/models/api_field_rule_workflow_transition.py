from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_field_rule_workflow_actions import ApiFieldRuleWorkflowActions
    from ..models.api_field_value import ApiFieldValue


T = TypeVar("T", bound="ApiFieldRuleWorkflowTransition")


@attr.s(auto_attribs=True)
class ApiFieldRuleWorkflowTransition:
    """Contains all the actions which should be performed when the dictionary
    field is changed to the specified value.

        Attributes:
            value (ApiFieldValue):
            actions (List['ApiFieldRuleWorkflowActions']): The list of actions which are executed when the value of the
                dictionary field is changed to the specified value.
    """

    value: "ApiFieldValue"
    actions: List["ApiFieldRuleWorkflowActions"]

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
        from ..models.api_field_rule_workflow_actions import ApiFieldRuleWorkflowActions
        from ..models.api_field_value import ApiFieldValue

        d = src_dict.copy()
        value = ApiFieldValue.from_dict(d.pop("Value"))

        actions = []
        _actions = d.pop("Actions")
        for actions_item_data in _actions:
            actions_item = ApiFieldRuleWorkflowActions.from_dict(actions_item_data)

            actions.append(actions_item)

        api_field_rule_workflow_transition = cls(
            value=value,
            actions=actions,
        )

        return api_field_rule_workflow_transition
