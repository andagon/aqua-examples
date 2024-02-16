from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_field_rule_workflow_transition_update import ApiFieldRuleWorkflowTransitionUpdate


T = TypeVar("T", bound="ApiFieldRuleWorkflowUpdate")


@attr.s(auto_attribs=True)
class ApiFieldRuleWorkflowUpdate:
    """
    Attributes:
        field_id (str): The id of the field to which the rule applies.
        rule_type (str):
        transitions (List['ApiFieldRuleWorkflowTransitionUpdate']): The list of transitions which this rule defines.
            Each transition
            specifies a list of actions which should be performed when the
            field is changed to the specified value.
    """

    field_id: str
    rule_type: str
    transitions: List["ApiFieldRuleWorkflowTransitionUpdate"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        rule_type = self.rule_type
        transitions = []
        for transitions_item_data in self.transitions:
            transitions_item = transitions_item_data.to_dict()

            transitions.append(transitions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldId": field_id,
                "RuleType": rule_type,
                "Transitions": transitions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_rule_workflow_transition_update import ApiFieldRuleWorkflowTransitionUpdate

        d = src_dict.copy()
        field_id = d.pop("FieldId")

        rule_type = d.pop("RuleType")

        transitions = []
        _transitions = d.pop("Transitions")
        for transitions_item_data in _transitions:
            transitions_item = ApiFieldRuleWorkflowTransitionUpdate.from_dict(transitions_item_data)

            transitions.append(transitions_item)

        api_field_rule_workflow_update = cls(
            field_id=field_id,
            rule_type=rule_type,
            transitions=transitions,
        )

        api_field_rule_workflow_update.additional_properties = d
        return api_field_rule_workflow_update

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
