from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_field_rules_update_with_item_type import ApiFieldRulesUpdateWithItemType


T = TypeVar("T", bound="ApiProjectFieldRulesUpdate")


@attr.s(auto_attribs=True)
class ApiProjectFieldRulesUpdate:
    """Contains the modifications which should be applied to the field rules
    for all item types in a project.

        Attributes:
            rules (List['ApiFieldRulesUpdateWithItemType']): Contains the field rules to update per item type. If nothing
                is specified for a certain item type, its field rules are not
                modified.
    """

    rules: List["ApiFieldRulesUpdateWithItemType"]

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
        from ..models.api_field_rules_update_with_item_type import ApiFieldRulesUpdateWithItemType

        d = src_dict.copy()
        rules = []
        _rules = d.pop("Rules")
        for rules_item_data in _rules:
            rules_item = ApiFieldRulesUpdateWithItemType.from_dict(rules_item_data)

            rules.append(rules_item)

        api_project_field_rules_update = cls(
            rules=rules,
        )

        return api_project_field_rules_update
