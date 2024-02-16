from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEditLayoutEntryField")


@attr.s(auto_attribs=True)
class ApiEditLayoutEntryField:
    """
    Attributes:
        entry_type (str):
        field_id (Union[Unset, None, str]): Id of the field.
        col_span (Union[Unset, int]): The number of columns this field should span in the UI layout.
            A three-column layout is assumed.
        starts_new_line (Union[Unset, bool]): Indicates whether this field should be placed on a new line in
            the UI layout.
    """

    entry_type: str
    field_id: Union[Unset, None, str] = UNSET
    col_span: Union[Unset, int] = UNSET
    starts_new_line: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry_type = self.entry_type
        field_id = self.field_id
        col_span = self.col_span
        starts_new_line = self.starts_new_line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "EntryType": entry_type,
            }
        )
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if col_span is not UNSET:
            field_dict["ColSpan"] = col_span
        if starts_new_line is not UNSET:
            field_dict["StartsNewLine"] = starts_new_line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry_type = d.pop("EntryType")

        field_id = d.pop("FieldId", UNSET)

        col_span = d.pop("ColSpan", UNSET)

        starts_new_line = d.pop("StartsNewLine", UNSET)

        api_edit_layout_entry_field = cls(
            entry_type=entry_type,
            field_id=field_id,
            col_span=col_span,
            starts_new_line=starts_new_line,
        )

        api_edit_layout_entry_field.additional_properties = d
        return api_edit_layout_entry_field

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
