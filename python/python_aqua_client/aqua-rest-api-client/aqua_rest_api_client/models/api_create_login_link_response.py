from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCreateLoginLinkResponse")


@attr.s(auto_attribs=True)
class ApiCreateLoginLinkResponse:
    """The response containing a URL that is only valid for
    a short period of time (default 10 minutes)

        Attributes:
            url (Union[Unset, None, str]): The URL containing the token that can be used to
                connect to aqua for a limited time
    """

    url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if url is not UNSET:
            field_dict["Url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("Url", UNSET)

        api_create_login_link_response = cls(
            url=url,
        )

        return api_create_login_link_response
