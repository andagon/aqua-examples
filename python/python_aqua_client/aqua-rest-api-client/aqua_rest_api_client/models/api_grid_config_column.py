from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_grid_config_column_fixed_position import ApiGridConfigColumnFixedPosition
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiGridConfigColumn")


@attr.s(auto_attribs=True)
class ApiGridConfigColumn:
    """Information regarding a single column

    Attributes:
        field_id (Union[Unset, None, str]): The id of the field
        width (Union[Unset, int]): The width of the column
        fixed_position (Union[Unset, ApiGridConfigColumnFixedPosition]): The position to which a column is fixed in the
            grid
    """

    field_id: Union[Unset, None, str] = UNSET
    width: Union[Unset, int] = UNSET
    fixed_position: Union[Unset, ApiGridConfigColumnFixedPosition] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        width = self.width
        fixed_position: Union[Unset, int] = UNSET
        if not isinstance(self.fixed_position, Unset):
            fixed_position = self.fixed_position.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if width is not UNSET:
            field_dict["Width"] = width
        if fixed_position is not UNSET:
            field_dict["FixedPosition"] = fixed_position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId", UNSET)

        width = d.pop("Width", UNSET)

        _fixed_position = d.pop("FixedPosition", UNSET)
        fixed_position: Union[Unset, ApiGridConfigColumnFixedPosition]
        if isinstance(_fixed_position, Unset):
            fixed_position = UNSET
        else:
            fixed_position = ApiGridConfigColumnFixedPosition(_fixed_position)

        api_grid_config_column = cls(
            field_id=field_id,
            width=width,
            fixed_position=fixed_position,
        )

        return api_grid_config_column
