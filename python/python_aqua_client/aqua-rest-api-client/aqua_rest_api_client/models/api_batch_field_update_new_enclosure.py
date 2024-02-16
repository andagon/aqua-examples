from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_enclosure_type import ApiEnclosureType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBatchFieldUpdateNewEnclosure")


@attr.s(auto_attribs=True)
class ApiBatchFieldUpdateNewEnclosure:
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
        enclosure_type (Union[Unset, ApiEnclosureType]): Identifies the type of enclosure.
            This enum has the following values:
              - `Description` The enclosure is a description of the defect.
              - `Note` The enclosure is a note.
              - `ReplicationProcedure` The enclosure is a replication procedure which explains how
            to reproduce the defect.
              - `Resolution` The enclosure explains how the defect has been resolved.
    """

    update_type: str
    value: Union[Unset, Any] = UNSET
    update_only_if_empty: Union[Unset, bool] = UNSET
    enclosure_type: Union[Unset, ApiEnclosureType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        update_type = self.update_type
        value = self.value
        update_only_if_empty = self.update_only_if_empty
        enclosure_type: Union[Unset, str] = UNSET
        if not isinstance(self.enclosure_type, Unset):
            enclosure_type = self.enclosure_type.value

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
        if enclosure_type is not UNSET:
            field_dict["EnclosureType"] = enclosure_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        update_type = d.pop("UpdateType")

        value = d.pop("Value", UNSET)

        update_only_if_empty = d.pop("UpdateOnlyIfEmpty", UNSET)

        _enclosure_type = d.pop("EnclosureType", UNSET)
        enclosure_type: Union[Unset, ApiEnclosureType]
        if isinstance(_enclosure_type, Unset):
            enclosure_type = UNSET
        else:
            enclosure_type = ApiEnclosureType(_enclosure_type)

        api_batch_field_update_new_enclosure = cls(
            update_type=update_type,
            value=value,
            update_only_if_empty=update_only_if_empty,
            enclosure_type=enclosure_type,
        )

        api_batch_field_update_new_enclosure.additional_properties = d
        return api_batch_field_update_new_enclosure

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
