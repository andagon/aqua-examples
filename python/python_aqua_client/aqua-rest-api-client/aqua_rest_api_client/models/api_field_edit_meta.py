from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_default_value import ApiFieldDefaultValue
    from ..models.api_field_range import ApiFieldRange
    from ..models.api_field_rule import ApiFieldRule


T = TypeVar("T", bound="ApiFieldEditMeta")


@attr.s(auto_attribs=True)
class ApiFieldEditMeta:
    """Contains the information for a specific field of an item including
    the field's value.

        Attributes:
            possible_values (Union[Unset, None, List[Any]]): The list of values which are allowed for this field. The list
                contains
                different types of values depending on the field type. Null means that
                all values which fit the field type are allowed.
                This list of values is based on the project template and on the workflow.
                These values might be restricted further by the Rules which are included
                in this editmeta as well.
            allow_other_values (Union[Unset, bool]): Indicates whether the field allows ohter values which are not included
                in the
                PossibleValues as long as they are fit the field type.
            required (Union[Unset, bool]): Indicates that the field is required which means that it must
                have a nonempty value.
            readonly (Union[Unset, bool]): Indicates that the field is readonly and cannot be modified
                by the user.
            default_value (Union[Unset, None, ApiFieldDefaultValue]): Contains the default value for certain field.
            rules (Union[Unset, None, List['ApiFieldRule']]): A list with additional rules which apply to this field. The
                client is responsible
                for evaluating these rules as necessary when fields change. These rules might
                further restrict the list of possible values.
            range_ (Union[Unset, None, ApiFieldRange]):
            field_mask (Union[Unset, None, str]): Contains formatting information for a specific field.
            visible (Union[Unset, bool]): Indicates whether the item should be visible in a UI. The visibility
                of the field might depend on the item's status when a workflow is active.
                In this case, the field will still have valid index.
            highlight (Union[Unset, bool]): Indicates that the field should be highlighted in the UI.
    """

    possible_values: Union[Unset, None, List[Any]] = UNSET
    allow_other_values: Union[Unset, bool] = UNSET
    required: Union[Unset, bool] = UNSET
    readonly: Union[Unset, bool] = UNSET
    default_value: Union[Unset, None, "ApiFieldDefaultValue"] = UNSET
    rules: Union[Unset, None, List["ApiFieldRule"]] = UNSET
    range_: Union[Unset, None, "ApiFieldRange"] = UNSET
    field_mask: Union[Unset, None, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    highlight: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        possible_values: Union[Unset, None, List[Any]] = UNSET
        if not isinstance(self.possible_values, Unset):
            if self.possible_values is None:
                possible_values = None
            else:
                possible_values = self.possible_values

        allow_other_values = self.allow_other_values
        required = self.required
        readonly = self.readonly
        default_value: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict() if self.default_value else None

        rules: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            if self.rules is None:
                rules = None
            else:
                rules = []
                for rules_item_data in self.rules:
                    rules_item = rules_item_data.to_dict()

                    rules.append(rules_item)

        range_: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict() if self.range_ else None

        field_mask = self.field_mask
        visible = self.visible
        highlight = self.highlight

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if possible_values is not UNSET:
            field_dict["PossibleValues"] = possible_values
        if allow_other_values is not UNSET:
            field_dict["AllowOtherValues"] = allow_other_values
        if required is not UNSET:
            field_dict["Required"] = required
        if readonly is not UNSET:
            field_dict["Readonly"] = readonly
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if rules is not UNSET:
            field_dict["Rules"] = rules
        if range_ is not UNSET:
            field_dict["Range"] = range_
        if field_mask is not UNSET:
            field_dict["FieldMask"] = field_mask
        if visible is not UNSET:
            field_dict["Visible"] = visible
        if highlight is not UNSET:
            field_dict["Highlight"] = highlight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_default_value import ApiFieldDefaultValue
        from ..models.api_field_range import ApiFieldRange
        from ..models.api_field_rule import ApiFieldRule

        d = src_dict.copy()
        possible_values = cast(List[Any], d.pop("PossibleValues", UNSET))

        allow_other_values = d.pop("AllowOtherValues", UNSET)

        required = d.pop("Required", UNSET)

        readonly = d.pop("Readonly", UNSET)

        _default_value = d.pop("DefaultValue", UNSET)
        default_value: Union[Unset, None, ApiFieldDefaultValue]
        if _default_value is None:
            default_value = None
        elif isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = ApiFieldDefaultValue.from_dict(_default_value)

        rules = []
        _rules = d.pop("Rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = ApiFieldRule.from_dict(rules_item_data)

            rules.append(rules_item)

        _range_ = d.pop("Range", UNSET)
        range_: Union[Unset, None, ApiFieldRange]
        if _range_ is None:
            range_ = None
        elif isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = ApiFieldRange.from_dict(_range_)

        field_mask = d.pop("FieldMask", UNSET)

        visible = d.pop("Visible", UNSET)

        highlight = d.pop("Highlight", UNSET)

        api_field_edit_meta = cls(
            possible_values=possible_values,
            allow_other_values=allow_other_values,
            required=required,
            readonly=readonly,
            default_value=default_value,
            rules=rules,
            range_=range_,
            field_mask=field_mask,
            visible=visible,
            highlight=highlight,
        )

        return api_field_edit_meta
