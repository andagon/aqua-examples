from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserViewColumnUpdate")


@attr.s(auto_attribs=True)
class ApiUserViewColumnUpdate:
    """
    Attributes:
        field_id (Union[Unset, None, str]): The id of the field for which the column is
            defined.
        width (Union[Unset, int]): The width of the column. The minimal width is 25px, if the set value is lower, the
            minimum width is automatically applied.
    """

    field_id: Union[Unset, None, str] = UNSET
    width: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if width is not UNSET:
            field_dict["Width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId", UNSET)

        width = d.pop("Width", UNSET)

        api_user_view_column_update = cls(
            field_id=field_id,
            width=width,
        )

        return api_user_view_column_update
