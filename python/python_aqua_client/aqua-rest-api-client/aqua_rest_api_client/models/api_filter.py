from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFilter")


@attr.s(auto_attribs=True)
class ApiFilter:
    """Represents the filter.

    Attributes:
        expression (Union[Unset, Any]): The Expression of the filter.
        display_text (Union[Unset, None, str]): The human readable text of the expression.
    """

    expression: Union[Unset, Any] = UNSET
    display_text: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        expression = self.expression
        display_text = self.display_text

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if expression is not UNSET:
            field_dict["Expression"] = expression
        if display_text is not UNSET:
            field_dict["DisplayText"] = display_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expression = d.pop("Expression", UNSET)

        display_text = d.pop("DisplayText", UNSET)

        api_filter = cls(
            expression=expression,
            display_text=display_text,
        )

        return api_filter
