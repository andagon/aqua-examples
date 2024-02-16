from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field import ApiField
    from ..models.api_field_value import ApiFieldValue


T = TypeVar("T", bound="ApiBatchAllowedValuesResponseEntry")


@attr.s(auto_attribs=True)
class ApiBatchAllowedValuesResponseEntry:
    """Contains the values which are allowed for a batch update
    of the specified field (in the specified items).

        Attributes:
            field (Union[Unset, None, ApiField]): Contains meta information for a specific field of an item.
            allowed_values (Union[Unset, None, List['ApiFieldValue']]): The list with the values which are allowed for the
                specified field
                in all of the specified items.
                If the limit was specified in the request then this collection contains
                only up to given number fo values. The overall count can be always
                found in AllowedValuesTotalCount.
            allowed_values_total_count (Union[Unset, int]): Overall number of allowed values.
            allow_other_values (Union[Unset, bool]): Indicates whether the other values, which are not included in the
                AllowedValues, are allowed as long as they fit the field type.
    """

    field: Union[Unset, None, "ApiField"] = UNSET
    allowed_values: Union[Unset, None, List["ApiFieldValue"]] = UNSET
    allowed_values_total_count: Union[Unset, int] = UNSET
    allow_other_values: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict() if self.field else None

        allowed_values: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.allowed_values, Unset):
            if self.allowed_values is None:
                allowed_values = None
            else:
                allowed_values = []
                for allowed_values_item_data in self.allowed_values:
                    allowed_values_item = allowed_values_item_data.to_dict()

                    allowed_values.append(allowed_values_item)

        allowed_values_total_count = self.allowed_values_total_count
        allow_other_values = self.allow_other_values

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field is not UNSET:
            field_dict["Field"] = field
        if allowed_values is not UNSET:
            field_dict["AllowedValues"] = allowed_values
        if allowed_values_total_count is not UNSET:
            field_dict["AllowedValuesTotalCount"] = allowed_values_total_count
        if allow_other_values is not UNSET:
            field_dict["AllowOtherValues"] = allow_other_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field import ApiField
        from ..models.api_field_value import ApiFieldValue

        d = src_dict.copy()
        _field = d.pop("Field", UNSET)
        field: Union[Unset, None, ApiField]
        if _field is None:
            field = None
        elif isinstance(_field, Unset):
            field = UNSET
        else:
            field = ApiField.from_dict(_field)

        allowed_values = []
        _allowed_values = d.pop("AllowedValues", UNSET)
        for allowed_values_item_data in _allowed_values or []:
            allowed_values_item = ApiFieldValue.from_dict(allowed_values_item_data)

            allowed_values.append(allowed_values_item)

        allowed_values_total_count = d.pop("AllowedValuesTotalCount", UNSET)

        allow_other_values = d.pop("AllowOtherValues", UNSET)

        api_batch_allowed_values_response_entry = cls(
            field=field,
            allowed_values=allowed_values,
            allowed_values_total_count=allowed_values_total_count,
            allow_other_values=allow_other_values,
        )

        return api_batch_allowed_values_response_entry
