from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBatchFieldUpdate")


@attr.s(auto_attribs=True)
class ApiBatchFieldUpdate:
    """Represents batch update of a single field to a given value.

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
    """

    update_type: str
    value: Union[Unset, Any] = UNSET
    update_only_if_empty: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        update_type = self.update_type
        value = self.value
        update_only_if_empty = self.update_only_if_empty

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "UpdateType": update_type,
            }
        )
        if value is not UNSET:
            field_dict["Value"] = value
        if update_only_if_empty is not UNSET:
            field_dict["UpdateOnlyIfEmpty"] = update_only_if_empty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        update_type = d.pop("UpdateType")

        value = d.pop("Value", UNSET)

        update_only_if_empty = d.pop("UpdateOnlyIfEmpty", UNSET)

        api_batch_field_update = cls(
            update_type=update_type,
            value=value,
            update_only_if_empty=update_only_if_empty,
        )

        return api_batch_field_update
