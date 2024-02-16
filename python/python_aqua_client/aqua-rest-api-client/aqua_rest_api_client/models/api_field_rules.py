from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.api_item_type import ApiItemType

if TYPE_CHECKING:
    from ..models.api_field_rule import ApiFieldRule


T = TypeVar("T", bound="ApiFieldRules")


@attr.s(auto_attribs=True)
class ApiFieldRules:
    """Contains the field rules for a certain item type in a certain
    project.

        Attributes:
            item_type (ApiItemType): Identifies the type of item.
                This enum has the following values:
                  - `Defect`
                  - `ExternalJira`
                  - `ExternalOtrs`
                  - `Requirement`
                  - `Script`
                  - `TestCase`
                  - `TestExecution`
                  - `TestScenario`
            rules (List['ApiFieldRule']): The list of rules. Rules can be only one of the following types:
                  - DependentValues: rules of this type restrict the possible values
                    of a certain field based on the current value of another field.
                  - Workflow: rules of this type specify actions which are executed when
                    the value of a dictionary field is changed to a certain value.
                    These actions include setting a field readonly, changing
                    the value of a field, etc.
    """

    item_type: ApiItemType
    rules: List["ApiFieldRule"]

    def to_dict(self) -> Dict[str, Any]:
        item_type = self.item_type.value

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()

            rules.append(rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ItemType": item_type,
                "Rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_rule import ApiFieldRule

        d = src_dict.copy()
        item_type = ApiItemType(d.pop("ItemType"))

        rules = []
        _rules = d.pop("Rules")
        for rules_item_data in _rules:
            rules_item = ApiFieldRule.from_dict(rules_item_data)

            rules.append(rules_item)

        api_field_rules = cls(
            item_type=item_type,
            rules=rules,
        )

        return api_field_rules
