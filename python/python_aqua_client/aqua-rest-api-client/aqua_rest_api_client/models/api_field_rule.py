from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiFieldRule")


@attr.s(auto_attribs=True)
class ApiFieldRule:
    """Represents a single rule for a field.

    Attributes:
        guid (str): The unique id of the field rule.
        field_id (str): The id of the field to which the rule applies.
        rule_type (str):
    """

    guid: str
    field_id: str
    rule_type: str

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        field_id = self.field_id
        rule_type = self.rule_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Guid": guid,
                "FieldId": field_id,
                "RuleType": rule_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("Guid")

        field_id = d.pop("FieldId")

        rule_type = d.pop("RuleType")

        api_field_rule = cls(
            guid=guid,
            field_id=field_id,
            rule_type=rule_type,
        )

        return api_field_rule
