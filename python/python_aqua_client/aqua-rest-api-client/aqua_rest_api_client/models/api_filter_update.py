from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFilterUpdate")


@attr.s(auto_attribs=True)
class ApiFilterUpdate:
    """Contains the new filter expression.

    Attributes:
        expression (Union[Unset, None, List[Any]]): The filter expression as JSON structure.
    """

    expression: Union[Unset, None, List[Any]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        expression: Union[Unset, None, List[Any]] = UNSET
        if not isinstance(self.expression, Unset):
            if self.expression is None:
                expression = None
            else:
                expression = self.expression

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if expression is not UNSET:
            field_dict["Expression"] = expression

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expression = cast(List[Any], d.pop("Expression", UNSET))

        api_filter_update = cls(
            expression=expression,
        )

        return api_filter_update
