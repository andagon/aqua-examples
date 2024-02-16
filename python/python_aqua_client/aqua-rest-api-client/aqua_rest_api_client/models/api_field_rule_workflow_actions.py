from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value import ApiFieldValue


T = TypeVar("T", bound="ApiFieldRuleWorkflowActions")


@attr.s(auto_attribs=True)
class ApiFieldRuleWorkflowActions:
    """Contains the actions which should be performed for one specific field.

    Attributes:
        field_id (str): This action is applied to the field with this id.
        readonly (bool): Indicates whether the field should be readonly.
        required (bool): Indicates whether the field should be required.
        visible (bool): Indicates whether the field should be visible.
        highlight (bool): Indicates whether the field should be highlighted.
        change_value (bool): Indicates whether the value of the field should be changed.
        value (Union[Unset, None, ApiFieldValue]):
    """

    field_id: str
    readonly: bool
    required: bool
    visible: bool
    highlight: bool
    change_value: bool
    value: Union[Unset, None, "ApiFieldValue"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        readonly = self.readonly
        required = self.required
        visible = self.visible
        highlight = self.highlight
        change_value = self.change_value
        value: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict() if self.value else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "FieldId": field_id,
                "Readonly": readonly,
                "Required": required,
                "Visible": visible,
                "Highlight": highlight,
                "ChangeValue": change_value,
            }
        )
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value import ApiFieldValue

        d = src_dict.copy()
        field_id = d.pop("FieldId")

        readonly = d.pop("Readonly")

        required = d.pop("Required")

        visible = d.pop("Visible")

        highlight = d.pop("Highlight")

        change_value = d.pop("ChangeValue")

        _value = d.pop("Value", UNSET)
        value: Union[Unset, None, ApiFieldValue]
        if _value is None:
            value = None
        elif isinstance(_value, Unset):
            value = UNSET
        else:
            value = ApiFieldValue.from_dict(_value)

        api_field_rule_workflow_actions = cls(
            field_id=field_id,
            readonly=readonly,
            required=required,
            visible=visible,
            highlight=highlight,
            change_value=change_value,
            value=value,
        )

        return api_field_rule_workflow_actions
