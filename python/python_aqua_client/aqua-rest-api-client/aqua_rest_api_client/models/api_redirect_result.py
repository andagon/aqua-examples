from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiRedirectResult")


@attr.s(auto_attribs=True)
class ApiRedirectResult:
    """This result is returned as part of a redirection response.
    Most clients should automatically follow the redirect and
    will never see this response.

        Attributes:
            message (str): A human-readable info message
            url (str): The URL to which the request is redirected.
    """

    message: str
    url: str

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Message": message,
                "Url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("Message")

        url = d.pop("Url")

        api_redirect_result = cls(
            message=message,
            url=url,
        )

        return api_redirect_result
