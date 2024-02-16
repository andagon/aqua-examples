from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_history_field_change_type import ApiHistoryFieldChangeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistoryFieldChanged")


@attr.s(auto_attribs=True)
class ApiHistoryFieldChanged:
    """A certain field of an item has changed

    Attributes:
        field_id (Union[Unset, None, str]): The id of the changed field
        field_title (Union[Unset, None, str]): The title of the changed field
        change_type (Union[Unset, ApiHistoryFieldChangeType]): Identifies the type of change to a certain field
            This enum has the following values:
              - `Added` The field was changed from empty to a certain value
              - `Changed` The field was changed from one value to another
              - `ChangedNoDiff` The field was changed but the value before and
            after the change have not been recorded
              - `Removed` The field was changed from a value to empty
        old_value (Union[Unset, Any]): The old value before the change as human readable object.
            If the flag IsRichText is true the value is of type ApiRichText otherwise of type string.
            ApiRichText contains following information:
            - string Html: information rendered as HTML.
            - bool IncompatibleRichTextFeatures: Indicates that rich text features are used which are not supported by the
            REST API.
            - string PlainText: information as plaintext.
        new_value (Union[Unset, Any]): The new value after the change as human readable object.
            If the flag IsRichText is true the value is of type ApiRichText otherwise of type string.
            ApiRichText contains following information:
            - string Html: information rendered as HTML.
            - bool IncompatibleRichTextFeatures: Indicates that rich text features are used which are not supported by the
            REST API.
            - string PlainText: information as plaintext.
        is_rich_text (Union[Unset, bool]): If true indicates that the values are of type ApiRichText, otherwise of type
            string.
    """

    field_id: Union[Unset, None, str] = UNSET
    field_title: Union[Unset, None, str] = UNSET
    change_type: Union[Unset, ApiHistoryFieldChangeType] = UNSET
    old_value: Union[Unset, Any] = UNSET
    new_value: Union[Unset, Any] = UNSET
    is_rich_text: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        field_title = self.field_title
        change_type: Union[Unset, str] = UNSET
        if not isinstance(self.change_type, Unset):
            change_type = self.change_type.value

        old_value = self.old_value
        new_value = self.new_value
        is_rich_text = self.is_rich_text

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if field_title is not UNSET:
            field_dict["FieldTitle"] = field_title
        if change_type is not UNSET:
            field_dict["ChangeType"] = change_type
        if old_value is not UNSET:
            field_dict["OldValue"] = old_value
        if new_value is not UNSET:
            field_dict["NewValue"] = new_value
        if is_rich_text is not UNSET:
            field_dict["IsRichText"] = is_rich_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId", UNSET)

        field_title = d.pop("FieldTitle", UNSET)

        _change_type = d.pop("ChangeType", UNSET)
        change_type: Union[Unset, ApiHistoryFieldChangeType]
        if isinstance(_change_type, Unset):
            change_type = UNSET
        else:
            change_type = ApiHistoryFieldChangeType(_change_type)

        old_value = d.pop("OldValue", UNSET)

        new_value = d.pop("NewValue", UNSET)

        is_rich_text = d.pop("IsRichText", UNSET)

        api_history_field_changed = cls(
            field_id=field_id,
            field_title=field_title,
            change_type=change_type,
            old_value=old_value,
            new_value=new_value,
            is_rich_text=is_rich_text,
        )

        return api_history_field_changed
