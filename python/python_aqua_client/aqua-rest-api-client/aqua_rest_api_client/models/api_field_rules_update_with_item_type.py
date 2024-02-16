from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.api_item_type import ApiItemType

if TYPE_CHECKING:
    from ..models.api_field_rule_update import ApiFieldRuleUpdate


T = TypeVar("T", bound="ApiFieldRulesUpdateWithItemType")


@attr.s(auto_attribs=True)
class ApiFieldRulesUpdateWithItemType:
    """
    Attributes:
        rules (List['ApiFieldRuleUpdate']): The list of field rules which should be set. The existing rules
            will be replaced. Rules can be only one of the following types:
              - DependentValues: rules of this type restrict the possible values
                of a certain field based on the current value of another field.
              - Workflow: rules of this type specify actions which are executed when
                the value of a dictionary field is changed to a certain value.
                These actions include setting a field readonly, changing
                the value of a field, etc.
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
    """

    rules: List["ApiFieldRuleUpdate"]
    item_type: ApiItemType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()

            rules.append(rules_item)

        item_type = self.item_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Rules": rules,
                "ItemType": item_type,
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

        item_type = ApiItemType(d.pop("ItemType"))

        api_field_rules_update_with_item_type = cls(
            rules=rules,
            item_type=item_type,
        )

        api_field_rules_update_with_item_type.additional_properties = d
        return api_field_rules_update_with_item_type

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
