from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HttpMethod")


@attr.s(auto_attribs=True)
class HttpMethod:
    """
    Attributes:
        method (Union[Unset, None, str]):
    """

    method: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        method = self.method

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if method is not UNSET:
            field_dict["Method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method = d.pop("Method", UNSET)

        http_method = cls(
            method=method,
        )

        return http_method
