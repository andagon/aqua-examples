from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBatchFieldUpdateRegularField")


@attr.s(auto_attribs=True)
class ApiBatchFieldUpdateRegularField:
    """
    Attributes:
        update_type (str):
        value (Union[Unset, Any]): The value to which the field will be changed. The exact type of the
            value depends on the field of the type:
            - for regular fields (UpdateType=RegularField) it should be the same as defined in ApiFieldUpdate.Value
            - for differential update of multi-selection fields (UpdateType=MultiChoiceFieldDifferential) it should be an
            array of ints (ids)
            - for a new enclosure (UpdateType=NewEnclosure) it should be string containing plain text of the enclosure
            content.
        update_only_if_empty (Union[Unset, bool]): Performs update only if the field is currently empty.
        field_id (Union[Unset, None, str]): Id of the regular field to update.
    """

    update_type: str
    value: Union[Unset, Any] = UNSET
    update_only_if_empty: Union[Unset, bool] = UNSET
    field_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        update_type = self.update_type
        value = self.value
        update_only_if_empty = self.update_only_if_empty
        field_id = self.field_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "UpdateType": update_type,
            }
        )
        if value is not UNSET:
            field_dict["Value"] = value
        if update_only_if_empty is not UNSET:
            field_dict["UpdateOnlyIfEmpty"] = update_only_if_empty
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        update_type = d.pop("UpdateType")

        value = d.pop("Value", UNSET)

        update_only_if_empty = d.pop("UpdateOnlyIfEmpty", UNSET)

        field_id = d.pop("FieldId", UNSET)

        api_batch_field_update_regular_field = cls(
            update_type=update_type,
            value=value,
            update_only_if_empty=update_only_if_empty,
            field_id=field_id,
        )

        api_batch_field_update_regular_field.additional_properties = d
        return api_batch_field_update_regular_field

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
