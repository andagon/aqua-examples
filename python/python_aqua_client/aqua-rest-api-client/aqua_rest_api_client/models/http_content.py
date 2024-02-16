from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_content_headers import HttpContentHeaders


T = TypeVar("T", bound="HttpContent")


@attr.s(auto_attribs=True)
class HttpContent:
    """
    Attributes:
        headers (Union[Unset, None, HttpContentHeaders]):
    """

    headers: Union[Unset, None, "HttpContentHeaders"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        headers: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict() if self.headers else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if headers is not UNSET:
            field_dict["Headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.http_content_headers import HttpContentHeaders

        d = src_dict.copy()
        _headers = d.pop("Headers", UNSET)
        headers: Union[Unset, None, HttpContentHeaders]
        if _headers is None:
            headers = None
        elif isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HttpContentHeaders.from_dict(_headers)

        http_content = cls(
            headers=headers,
        )

        return http_content
