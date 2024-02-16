from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSystemGetColorsResponse")


@attr.s(auto_attribs=True)
class ApiSystemGetColorsResponse:
    """Contains the response for get colors.

    Attributes:
        colors (Union[Unset, None, List[str]]): List of predefined colors.
    """

    colors: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        colors: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.colors, Unset):
            if self.colors is None:
                colors = None
            else:
                colors = self.colors

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if colors is not UNSET:
            field_dict["Colors"] = colors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        colors = cast(List[str], d.pop("Colors", UNSET))

        api_system_get_colors_response = cls(
            colors=colors,
        )

        return api_system_get_colors_response
