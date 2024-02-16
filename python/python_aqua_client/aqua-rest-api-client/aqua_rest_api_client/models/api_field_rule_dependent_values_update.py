from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_field_value_restriction_update import ApiFieldValueRestrictionUpdate


T = TypeVar("T", bound="ApiFieldRuleDependentValuesUpdate")


@attr.s(auto_attribs=True)
class ApiFieldRuleDependentValuesUpdate:
    """
    Attributes:
        field_id (str): The id of the field to which the rule applies.
        rule_type (str):
        other_field_id (str): The id of the other field on which the field to which this rule applies depends.
        restrictions (List['ApiFieldValueRestrictionUpdate']): The list with the restrictions for the value of the
            field.
    """

    field_id: str
    rule_type: str
    other_field_id: str
    restrictions: List["ApiFieldValueRestrictionUpdate"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        rule_type = self.rule_type
        other_field_id = self.other_field_id
        restrictions = []
        for restrictions_item_data in self.restrictions:
            restrictions_item = restrictions_item_data.to_dict()

            restrictions.append(restrictions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldId": field_id,
                "RuleType": rule_type,
                "OtherFieldId": other_field_id,
                "Restrictions": restrictions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_restriction_update import ApiFieldValueRestrictionUpdate

        d = src_dict.copy()
        field_id = d.pop("FieldId")

        rule_type = d.pop("RuleType")

        other_field_id = d.pop("OtherFieldId")

        restrictions = []
        _restrictions = d.pop("Restrictions")
        for restrictions_item_data in _restrictions:
            restrictions_item = ApiFieldValueRestrictionUpdate.from_dict(restrictions_item_data)

            restrictions.append(restrictions_item)

        api_field_rule_dependent_values_update = cls(
            field_id=field_id,
            rule_type=rule_type,
            other_field_id=other_field_id,
            restrictions=restrictions,
        )

        api_field_rule_dependent_values_update.additional_properties = d
        return api_field_rule_dependent_values_update

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
