from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationHeaderValue")


@attr.s(auto_attribs=True)
class AuthenticationHeaderValue:
    """
    Attributes:
        scheme (Union[Unset, None, str]):
        parameter (Union[Unset, None, str]):
    """

    scheme: Union[Unset, None, str] = UNSET
    parameter: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        scheme = self.scheme
        parameter = self.parameter

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if scheme is not UNSET:
            field_dict["Scheme"] = scheme
        if parameter is not UNSET:
            field_dict["Parameter"] = parameter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scheme = d.pop("Scheme", UNSET)

        parameter = d.pop("Parameter", UNSET)

        authentication_header_value = cls(
            scheme=scheme,
            parameter=parameter,
        )

        return authentication_header_value
