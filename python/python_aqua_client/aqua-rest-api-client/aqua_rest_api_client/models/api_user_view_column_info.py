from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserViewColumnInfo")


@attr.s(auto_attribs=True)
class ApiUserViewColumnInfo:
    """Represents the user view column information.

    Attributes:
        field_id (Union[Unset, None, str]): The name of the column.
        title (Union[Unset, None, str]): The label of the column.
        width (Union[Unset, int]): The width of the column.
    """

    field_id: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    width: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        title = self.title
        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if title is not UNSET:
            field_dict["Title"] = title
        if width is not UNSET:
            field_dict["Width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId", UNSET)

        title = d.pop("Title", UNSET)

        width = d.pop("Width", UNSET)

        api_user_view_column_info = cls(
            field_id=field_id,
            title=title,
            width=width,
        )

        return api_user_view_column_info
