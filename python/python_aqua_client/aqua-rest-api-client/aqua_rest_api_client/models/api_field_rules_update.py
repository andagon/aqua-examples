from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_field_rule_update import ApiFieldRuleUpdate


T = TypeVar("T", bound="ApiFieldRulesUpdate")


@attr.s(auto_attribs=True)
class ApiFieldRulesUpdate:
    """Contains the modifications which should be applied to the field rules
    for a certain item type.

        Attributes:
            rules (List['ApiFieldRuleUpdate']): The list of field rules which should be set. The existing rules
                will be replaced. Rules can be only one of the following types:
                  - DependentValues: rules of this type restrict the possible values
                    of a certain field based on the current value of another field.
                  - Workflow: rules of this type specify actions which are executed when
                    the value of a dictionary field is changed to a certain value.
                    These actions include setting a field readonly, changing
                    the value of a field, etc.
    """

    rules: List["ApiFieldRuleUpdate"]

    def to_dict(self) -> Dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()

            rules.append(rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_rule_update import ApiFieldRuleUpdate

        d = src_dict.copy()
        rules = []
        _rules = d.pop("Rules")
        for rules_item_data in _rules:
            rules_item = ApiFieldRuleUpdate.from_dict(rules_item_data)

            rules.append(rules_item)

        api_field_rules_update = cls(
            rules=rules,
        )

        return api_field_rules_update
