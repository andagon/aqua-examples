import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_disposition_header_value import ContentDispositionHeaderValue
    from ..models.content_range_header_value import ContentRangeHeaderValue
    from ..models.media_type_header_value import MediaTypeHeaderValue


T = TypeVar("T", bound="HttpContentHeaders")


@attr.s(auto_attribs=True)
class HttpContentHeaders:
    """
    Attributes:
        allow (Union[Unset, None, List[str]]):
        content_disposition (Union[Unset, None, ContentDispositionHeaderValue]):
        content_encoding (Union[Unset, None, List[str]]):
        content_language (Union[Unset, None, List[str]]):
        content_length (Union[Unset, None, int]):
        content_location (Union[Unset, None, str]):
        content_md5 (Union[Unset, None, str]):
        content_range (Union[Unset, None, ContentRangeHeaderValue]):
        content_type (Union[Unset, None, MediaTypeHeaderValue]):
        expires (Union[Unset, None, datetime.datetime]):
        last_modified (Union[Unset, None, datetime.datetime]):
    """

    allow: Union[Unset, None, List[str]] = UNSET
    content_disposition: Union[Unset, None, "ContentDispositionHeaderValue"] = UNSET
    content_encoding: Union[Unset, None, List[str]] = UNSET
    content_language: Union[Unset, None, List[str]] = UNSET
    content_length: Union[Unset, None, int] = UNSET
    content_location: Union[Unset, None, str] = UNSET
    content_md5: Union[Unset, None, str] = UNSET
    content_range: Union[Unset, None, "ContentRangeHeaderValue"] = UNSET
    content_type: Union[Unset, None, "MediaTypeHeaderValue"] = UNSET
    expires: Union[Unset, None, datetime.datetime] = UNSET
    last_modified: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.allow, Unset):
            if self.allow is None:
                allow = None
            else:
                allow = self.allow

        content_disposition: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.content_disposition, Unset):
            content_disposition = self.content_disposition.to_dict() if self.content_disposition else None

        content_encoding: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.content_encoding, Unset):
            if self.content_encoding is None:
                content_encoding = None
            else:
                content_encoding = self.content_encoding

        content_language: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.content_language, Unset):
            if self.content_language is None:
                content_language = None
            else:
                content_language = self.content_language

        content_length = self.content_length
        content_location = self.content_location
        content_md5 = self.content_md5
        content_range: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.content_range, Unset):
            content_range = self.content_range.to_dict() if self.content_range else None

        content_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.to_dict() if self.content_type else None

        expires: Union[Unset, None, str] = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat() if self.expires else None

        last_modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat() if self.last_modified else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow is not UNSET:
            field_dict["Allow"] = allow
        if content_disposition is not UNSET:
            field_dict["ContentDisposition"] = content_disposition
        if content_encoding is not UNSET:
            field_dict["ContentEncoding"] = content_encoding
        if content_language is not UNSET:
            field_dict["ContentLanguage"] = content_language
        if content_length is not UNSET:
            field_dict["ContentLength"] = content_length
        if content_location is not UNSET:
            field_dict["ContentLocation"] = content_location
        if content_md5 is not UNSET:
            field_dict["ContentMD5"] = content_md5
        if content_range is not UNSET:
            field_dict["ContentRange"] = content_range
        if content_type is not UNSET:
            field_dict["ContentType"] = content_type
        if expires is not UNSET:
            field_dict["Expires"] = expires
        if last_modified is not UNSET:
            field_dict["LastModified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_disposition_header_value import ContentDispositionHeaderValue
        from ..models.content_range_header_value import ContentRangeHeaderValue
        from ..models.media_type_header_value import MediaTypeHeaderValue

        d = src_dict.copy()
        allow = cast(List[str], d.pop("Allow", UNSET))

        _content_disposition = d.pop("ContentDisposition", UNSET)
        content_disposition: Union[Unset, None, ContentDispositionHeaderValue]
        if _content_disposition is None:
            content_disposition = None
        elif isinstance(_content_disposition, Unset):
            content_disposition = UNSET
        else:
            content_disposition = ContentDispositionHeaderValue.from_dict(_content_disposition)

        content_encoding = cast(List[str], d.pop("ContentEncoding", UNSET))

        content_language = cast(List[str], d.pop("ContentLanguage", UNSET))

        content_length = d.pop("ContentLength", UNSET)

        content_location = d.pop("ContentLocation", UNSET)

        content_md5 = d.pop("ContentMD5", UNSET)

        _content_range = d.pop("ContentRange", UNSET)
        content_range: Union[Unset, None, ContentRangeHeaderValue]
        if _content_range is None:
            content_range = None
        elif isinstance(_content_range, Unset):
            content_range = UNSET
        else:
            content_range = ContentRangeHeaderValue.from_dict(_content_range)

        _content_type = d.pop("ContentType", UNSET)
        content_type: Union[Unset, None, MediaTypeHeaderValue]
        if _content_type is None:
            content_type = None
        elif isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = MediaTypeHeaderValue.from_dict(_content_type)

        _expires = d.pop("Expires", UNSET)
        expires: Union[Unset, None, datetime.datetime]
        if _expires is None:
            expires = None
        elif isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires)

        _last_modified = d.pop("LastModified", UNSET)
        last_modified: Union[Unset, None, datetime.datetime]
        if _last_modified is None:
            last_modified = None
        elif isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        http_content_headers = cls(
            allow=allow,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_language=content_language,
            content_length=content_length,
            content_location=content_location,
            content_md5=content_md5,
            content_range=content_range,
            content_type=content_type,
            expires=expires,
            last_modified=last_modified,
        )

        http_content_headers.additional_properties = d
        return http_content_headers

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
