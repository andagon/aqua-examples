from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_content import HttpContent
    from ..models.http_method import HttpMethod
    from ..models.http_request_headers import HttpRequestHeaders
    from ..models.http_request_message_properties import HttpRequestMessageProperties
    from ..models.version import Version


T = TypeVar("T", bound="HttpRequestMessage")


@attr.s(auto_attribs=True)
class HttpRequestMessage:
    """
    Attributes:
        version (Union[Unset, None, Version]):
        content (Union[Unset, None, HttpContent]):
        method (Union[Unset, None, HttpMethod]):
        request_uri (Union[Unset, None, str]):
        headers (Union[Unset, None, HttpRequestHeaders]):
        properties (Union[Unset, None, HttpRequestMessageProperties]):
    """

    version: Union[Unset, None, "Version"] = UNSET
    content: Union[Unset, None, "HttpContent"] = UNSET
    method: Union[Unset, None, "HttpMethod"] = UNSET
    request_uri: Union[Unset, None, str] = UNSET
    headers: Union[Unset, None, "HttpRequestHeaders"] = UNSET
    properties: Union[Unset, None, "HttpRequestMessageProperties"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        version: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict() if self.version else None

        content: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict() if self.content else None

        method: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.to_dict() if self.method else None

        request_uri = self.request_uri
        headers: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict() if self.headers else None

        properties: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict() if self.properties else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version
        if content is not UNSET:
            field_dict["Content"] = content
        if method is not UNSET:
            field_dict["Method"] = method
        if request_uri is not UNSET:
            field_dict["RequestUri"] = request_uri
        if headers is not UNSET:
            field_dict["Headers"] = headers
        if properties is not UNSET:
            field_dict["Properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.http_content import HttpContent
        from ..models.http_method import HttpMethod
        from ..models.http_request_headers import HttpRequestHeaders
        from ..models.http_request_message_properties import HttpRequestMessageProperties
        from ..models.version import Version

        d = src_dict.copy()
        _version = d.pop("Version", UNSET)
        version: Union[Unset, None, Version]
        if _version is None:
            version = None
        elif isinstance(_version, Unset):
            version = UNSET
        else:
            version = Version.from_dict(_version)

        _content = d.pop("Content", UNSET)
        content: Union[Unset, None, HttpContent]
        if _content is None:
            content = None
        elif isinstance(_content, Unset):
            content = UNSET
        else:
            content = HttpContent.from_dict(_content)

        _method = d.pop("Method", UNSET)
        method: Union[Unset, None, HttpMethod]
        if _method is None:
            method = None
        elif isinstance(_method, Unset):
            method = UNSET
        else:
            method = HttpMethod.from_dict(_method)

        request_uri = d.pop("RequestUri", UNSET)

        _headers = d.pop("Headers", UNSET)
        headers: Union[Unset, None, HttpRequestHeaders]
        if _headers is None:
            headers = None
        elif isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HttpRequestHeaders.from_dict(_headers)

        _properties = d.pop("Properties", UNSET)
        properties: Union[Unset, None, HttpRequestMessageProperties]
        if _properties is None:
            properties = None
        elif isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = HttpRequestMessageProperties.from_dict(_properties)

        http_request_message = cls(
            version=version,
            content=content,
            method=method,
            request_uri=request_uri,
            headers=headers,
            properties=properties,
        )

        return http_request_message
