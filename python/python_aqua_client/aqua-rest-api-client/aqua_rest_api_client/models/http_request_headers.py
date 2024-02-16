import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication_header_value import AuthenticationHeaderValue
    from ..models.cache_control_header_value import CacheControlHeaderValue
    from ..models.entity_tag_header_value import EntityTagHeaderValue
    from ..models.media_type_with_quality_header_value import MediaTypeWithQualityHeaderValue
    from ..models.name_value_header_value import NameValueHeaderValue
    from ..models.name_value_with_parameters_header_value import NameValueWithParametersHeaderValue
    from ..models.product_header_value import ProductHeaderValue
    from ..models.product_info_header_value import ProductInfoHeaderValue
    from ..models.range_condition_header_value import RangeConditionHeaderValue
    from ..models.range_header_value import RangeHeaderValue
    from ..models.string_with_quality_header_value import StringWithQualityHeaderValue
    from ..models.transfer_coding_header_value import TransferCodingHeaderValue
    from ..models.transfer_coding_with_quality_header_value import TransferCodingWithQualityHeaderValue
    from ..models.via_header_value import ViaHeaderValue
    from ..models.warning_header_value import WarningHeaderValue


T = TypeVar("T", bound="HttpRequestHeaders")


@attr.s(auto_attribs=True)
class HttpRequestHeaders:
    """
    Attributes:
        accept (Union[Unset, None, List['MediaTypeWithQualityHeaderValue']]):
        accept_charset (Union[Unset, None, List['StringWithQualityHeaderValue']]):
        accept_encoding (Union[Unset, None, List['StringWithQualityHeaderValue']]):
        accept_language (Union[Unset, None, List['StringWithQualityHeaderValue']]):
        authorization (Union[Unset, None, AuthenticationHeaderValue]):
        expect (Union[Unset, None, List['NameValueWithParametersHeaderValue']]):
        expect_continue (Union[Unset, None, bool]):
        from_ (Union[Unset, None, str]):
        host (Union[Unset, None, str]):
        if_match (Union[Unset, None, List['EntityTagHeaderValue']]):
        if_modified_since (Union[Unset, None, datetime.datetime]):
        if_none_match (Union[Unset, None, List['EntityTagHeaderValue']]):
        if_range (Union[Unset, None, RangeConditionHeaderValue]):
        if_unmodified_since (Union[Unset, None, datetime.datetime]):
        max_forwards (Union[Unset, None, int]):
        proxy_authorization (Union[Unset, None, AuthenticationHeaderValue]):
        range_ (Union[Unset, None, RangeHeaderValue]):
        referrer (Union[Unset, None, str]):
        te (Union[Unset, None, List['TransferCodingWithQualityHeaderValue']]):
        user_agent (Union[Unset, None, List['ProductInfoHeaderValue']]):
        cache_control (Union[Unset, None, CacheControlHeaderValue]):
        connection (Union[Unset, None, List[str]]):
        connection_close (Union[Unset, None, bool]):
        date (Union[Unset, None, datetime.datetime]):
        pragma (Union[Unset, None, List['NameValueHeaderValue']]):
        trailer (Union[Unset, None, List[str]]):
        transfer_encoding (Union[Unset, None, List['TransferCodingHeaderValue']]):
        transfer_encoding_chunked (Union[Unset, None, bool]):
        upgrade (Union[Unset, None, List['ProductHeaderValue']]):
        via (Union[Unset, None, List['ViaHeaderValue']]):
        warning (Union[Unset, None, List['WarningHeaderValue']]):
    """

    accept: Union[Unset, None, List["MediaTypeWithQualityHeaderValue"]] = UNSET
    accept_charset: Union[Unset, None, List["StringWithQualityHeaderValue"]] = UNSET
    accept_encoding: Union[Unset, None, List["StringWithQualityHeaderValue"]] = UNSET
    accept_language: Union[Unset, None, List["StringWithQualityHeaderValue"]] = UNSET
    authorization: Union[Unset, None, "AuthenticationHeaderValue"] = UNSET
    expect: Union[Unset, None, List["NameValueWithParametersHeaderValue"]] = UNSET
    expect_continue: Union[Unset, None, bool] = UNSET
    from_: Union[Unset, None, str] = UNSET
    host: Union[Unset, None, str] = UNSET
    if_match: Union[Unset, None, List["EntityTagHeaderValue"]] = UNSET
    if_modified_since: Union[Unset, None, datetime.datetime] = UNSET
    if_none_match: Union[Unset, None, List["EntityTagHeaderValue"]] = UNSET
    if_range: Union[Unset, None, "RangeConditionHeaderValue"] = UNSET
    if_unmodified_since: Union[Unset, None, datetime.datetime] = UNSET
    max_forwards: Union[Unset, None, int] = UNSET
    proxy_authorization: Union[Unset, None, "AuthenticationHeaderValue"] = UNSET
    range_: Union[Unset, None, "RangeHeaderValue"] = UNSET
    referrer: Union[Unset, None, str] = UNSET
    te: Union[Unset, None, List["TransferCodingWithQualityHeaderValue"]] = UNSET
    user_agent: Union[Unset, None, List["ProductInfoHeaderValue"]] = UNSET
    cache_control: Union[Unset, None, "CacheControlHeaderValue"] = UNSET
    connection: Union[Unset, None, List[str]] = UNSET
    connection_close: Union[Unset, None, bool] = UNSET
    date: Union[Unset, None, datetime.datetime] = UNSET
    pragma: Union[Unset, None, List["NameValueHeaderValue"]] = UNSET
    trailer: Union[Unset, None, List[str]] = UNSET
    transfer_encoding: Union[Unset, None, List["TransferCodingHeaderValue"]] = UNSET
    transfer_encoding_chunked: Union[Unset, None, bool] = UNSET
    upgrade: Union[Unset, None, List["ProductHeaderValue"]] = UNSET
    via: Union[Unset, None, List["ViaHeaderValue"]] = UNSET
    warning: Union[Unset, None, List["WarningHeaderValue"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accept: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accept, Unset):
            if self.accept is None:
                accept = None
            else:
                accept = []
                for accept_item_data in self.accept:
                    accept_item = accept_item_data.to_dict()

                    accept.append(accept_item)

        accept_charset: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accept_charset, Unset):
            if self.accept_charset is None:
                accept_charset = None
            else:
                accept_charset = []
                for accept_charset_item_data in self.accept_charset:
                    accept_charset_item = accept_charset_item_data.to_dict()

                    accept_charset.append(accept_charset_item)

        accept_encoding: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accept_encoding, Unset):
            if self.accept_encoding is None:
                accept_encoding = None
            else:
                accept_encoding = []
                for accept_encoding_item_data in self.accept_encoding:
                    accept_encoding_item = accept_encoding_item_data.to_dict()

                    accept_encoding.append(accept_encoding_item)

        accept_language: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accept_language, Unset):
            if self.accept_language is None:
                accept_language = None
            else:
                accept_language = []
                for accept_language_item_data in self.accept_language:
                    accept_language_item = accept_language_item_data.to_dict()

                    accept_language.append(accept_language_item)

        authorization: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.authorization, Unset):
            authorization = self.authorization.to_dict() if self.authorization else None

        expect: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.expect, Unset):
            if self.expect is None:
                expect = None
            else:
                expect = []
                for expect_item_data in self.expect:
                    expect_item = expect_item_data.to_dict()

                    expect.append(expect_item)

        expect_continue = self.expect_continue
        from_ = self.from_
        host = self.host
        if_match: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.if_match, Unset):
            if self.if_match is None:
                if_match = None
            else:
                if_match = []
                for if_match_item_data in self.if_match:
                    if_match_item = if_match_item_data.to_dict()

                    if_match.append(if_match_item)

        if_modified_since: Union[Unset, None, str] = UNSET
        if not isinstance(self.if_modified_since, Unset):
            if_modified_since = self.if_modified_since.isoformat() if self.if_modified_since else None

        if_none_match: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.if_none_match, Unset):
            if self.if_none_match is None:
                if_none_match = None
            else:
                if_none_match = []
                for if_none_match_item_data in self.if_none_match:
                    if_none_match_item = if_none_match_item_data.to_dict()

                    if_none_match.append(if_none_match_item)

        if_range: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.if_range, Unset):
            if_range = self.if_range.to_dict() if self.if_range else None

        if_unmodified_since: Union[Unset, None, str] = UNSET
        if not isinstance(self.if_unmodified_since, Unset):
            if_unmodified_since = self.if_unmodified_since.isoformat() if self.if_unmodified_since else None

        max_forwards = self.max_forwards
        proxy_authorization: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.proxy_authorization, Unset):
            proxy_authorization = self.proxy_authorization.to_dict() if self.proxy_authorization else None

        range_: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict() if self.range_ else None

        referrer = self.referrer
        te: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.te, Unset):
            if self.te is None:
                te = None
            else:
                te = []
                for te_item_data in self.te:
                    te_item = te_item_data.to_dict()

                    te.append(te_item)

        user_agent: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_agent, Unset):
            if self.user_agent is None:
                user_agent = None
            else:
                user_agent = []
                for user_agent_item_data in self.user_agent:
                    user_agent_item = user_agent_item_data.to_dict()

                    user_agent.append(user_agent_item)

        cache_control: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.cache_control, Unset):
            cache_control = self.cache_control.to_dict() if self.cache_control else None

        connection: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.connection, Unset):
            if self.connection is None:
                connection = None
            else:
                connection = self.connection

        connection_close = self.connection_close
        date: Union[Unset, None, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat() if self.date else None

        pragma: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pragma, Unset):
            if self.pragma is None:
                pragma = None
            else:
                pragma = []
                for pragma_item_data in self.pragma:
                    pragma_item = pragma_item_data.to_dict()

                    pragma.append(pragma_item)

        trailer: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.trailer, Unset):
            if self.trailer is None:
                trailer = None
            else:
                trailer = self.trailer

        transfer_encoding: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transfer_encoding, Unset):
            if self.transfer_encoding is None:
                transfer_encoding = None
            else:
                transfer_encoding = []
                for transfer_encoding_item_data in self.transfer_encoding:
                    transfer_encoding_item = transfer_encoding_item_data.to_dict()

                    transfer_encoding.append(transfer_encoding_item)

        transfer_encoding_chunked = self.transfer_encoding_chunked
        upgrade: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.upgrade, Unset):
            if self.upgrade is None:
                upgrade = None
            else:
                upgrade = []
                for upgrade_item_data in self.upgrade:
                    upgrade_item = upgrade_item_data.to_dict()

                    upgrade.append(upgrade_item)

        via: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.via, Unset):
            if self.via is None:
                via = None
            else:
                via = []
                for via_item_data in self.via:
                    via_item = via_item_data.to_dict()

                    via.append(via_item)

        warning: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warning, Unset):
            if self.warning is None:
                warning = None
            else:
                warning = []
                for warning_item_data in self.warning:
                    warning_item = warning_item_data.to_dict()

                    warning.append(warning_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept is not UNSET:
            field_dict["Accept"] = accept
        if accept_charset is not UNSET:
            field_dict["AcceptCharset"] = accept_charset
        if accept_encoding is not UNSET:
            field_dict["AcceptEncoding"] = accept_encoding
        if accept_language is not UNSET:
            field_dict["AcceptLanguage"] = accept_language
        if authorization is not UNSET:
            field_dict["Authorization"] = authorization
        if expect is not UNSET:
            field_dict["Expect"] = expect
        if expect_continue is not UNSET:
            field_dict["ExpectContinue"] = expect_continue
        if from_ is not UNSET:
            field_dict["From"] = from_
        if host is not UNSET:
            field_dict["Host"] = host
        if if_match is not UNSET:
            field_dict["IfMatch"] = if_match
        if if_modified_since is not UNSET:
            field_dict["IfModifiedSince"] = if_modified_since
        if if_none_match is not UNSET:
            field_dict["IfNoneMatch"] = if_none_match
        if if_range is not UNSET:
            field_dict["IfRange"] = if_range
        if if_unmodified_since is not UNSET:
            field_dict["IfUnmodifiedSince"] = if_unmodified_since
        if max_forwards is not UNSET:
            field_dict["MaxForwards"] = max_forwards
        if proxy_authorization is not UNSET:
            field_dict["ProxyAuthorization"] = proxy_authorization
        if range_ is not UNSET:
            field_dict["Range"] = range_
        if referrer is not UNSET:
            field_dict["Referrer"] = referrer
        if te is not UNSET:
            field_dict["TE"] = te
        if user_agent is not UNSET:
            field_dict["UserAgent"] = user_agent
        if cache_control is not UNSET:
            field_dict["CacheControl"] = cache_control
        if connection is not UNSET:
            field_dict["Connection"] = connection
        if connection_close is not UNSET:
            field_dict["ConnectionClose"] = connection_close
        if date is not UNSET:
            field_dict["Date"] = date
        if pragma is not UNSET:
            field_dict["Pragma"] = pragma
        if trailer is not UNSET:
            field_dict["Trailer"] = trailer
        if transfer_encoding is not UNSET:
            field_dict["TransferEncoding"] = transfer_encoding
        if transfer_encoding_chunked is not UNSET:
            field_dict["TransferEncodingChunked"] = transfer_encoding_chunked
        if upgrade is not UNSET:
            field_dict["Upgrade"] = upgrade
        if via is not UNSET:
            field_dict["Via"] = via
        if warning is not UNSET:
            field_dict["Warning"] = warning

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authentication_header_value import AuthenticationHeaderValue
        from ..models.cache_control_header_value import CacheControlHeaderValue
        from ..models.entity_tag_header_value import EntityTagHeaderValue
        from ..models.media_type_with_quality_header_value import MediaTypeWithQualityHeaderValue
        from ..models.name_value_header_value import NameValueHeaderValue
        from ..models.name_value_with_parameters_header_value import NameValueWithParametersHeaderValue
        from ..models.product_header_value import ProductHeaderValue
        from ..models.product_info_header_value import ProductInfoHeaderValue
        from ..models.range_condition_header_value import RangeConditionHeaderValue
        from ..models.range_header_value import RangeHeaderValue
        from ..models.string_with_quality_header_value import StringWithQualityHeaderValue
        from ..models.transfer_coding_header_value import TransferCodingHeaderValue
        from ..models.transfer_coding_with_quality_header_value import TransferCodingWithQualityHeaderValue
        from ..models.via_header_value import ViaHeaderValue
        from ..models.warning_header_value import WarningHeaderValue

        d = src_dict.copy()
        accept = []
        _accept = d.pop("Accept", UNSET)
        for accept_item_data in _accept or []:
            accept_item = MediaTypeWithQualityHeaderValue.from_dict(accept_item_data)

            accept.append(accept_item)

        accept_charset = []
        _accept_charset = d.pop("AcceptCharset", UNSET)
        for accept_charset_item_data in _accept_charset or []:
            accept_charset_item = StringWithQualityHeaderValue.from_dict(accept_charset_item_data)

            accept_charset.append(accept_charset_item)

        accept_encoding = []
        _accept_encoding = d.pop("AcceptEncoding", UNSET)
        for accept_encoding_item_data in _accept_encoding or []:
            accept_encoding_item = StringWithQualityHeaderValue.from_dict(accept_encoding_item_data)

            accept_encoding.append(accept_encoding_item)

        accept_language = []
        _accept_language = d.pop("AcceptLanguage", UNSET)
        for accept_language_item_data in _accept_language or []:
            accept_language_item = StringWithQualityHeaderValue.from_dict(accept_language_item_data)

            accept_language.append(accept_language_item)

        _authorization = d.pop("Authorization", UNSET)
        authorization: Union[Unset, None, AuthenticationHeaderValue]
        if _authorization is None:
            authorization = None
        elif isinstance(_authorization, Unset):
            authorization = UNSET
        else:
            authorization = AuthenticationHeaderValue.from_dict(_authorization)

        expect = []
        _expect = d.pop("Expect", UNSET)
        for expect_item_data in _expect or []:
            expect_item = NameValueWithParametersHeaderValue.from_dict(expect_item_data)

            expect.append(expect_item)

        expect_continue = d.pop("ExpectContinue", UNSET)

        from_ = d.pop("From", UNSET)

        host = d.pop("Host", UNSET)

        if_match = []
        _if_match = d.pop("IfMatch", UNSET)
        for if_match_item_data in _if_match or []:
            if_match_item = EntityTagHeaderValue.from_dict(if_match_item_data)

            if_match.append(if_match_item)

        _if_modified_since = d.pop("IfModifiedSince", UNSET)
        if_modified_since: Union[Unset, None, datetime.datetime]
        if _if_modified_since is None:
            if_modified_since = None
        elif isinstance(_if_modified_since, Unset):
            if_modified_since = UNSET
        else:
            if_modified_since = isoparse(_if_modified_since)

        if_none_match = []
        _if_none_match = d.pop("IfNoneMatch", UNSET)
        for if_none_match_item_data in _if_none_match or []:
            if_none_match_item = EntityTagHeaderValue.from_dict(if_none_match_item_data)

            if_none_match.append(if_none_match_item)

        _if_range = d.pop("IfRange", UNSET)
        if_range: Union[Unset, None, RangeConditionHeaderValue]
        if _if_range is None:
            if_range = None
        elif isinstance(_if_range, Unset):
            if_range = UNSET
        else:
            if_range = RangeConditionHeaderValue.from_dict(_if_range)

        _if_unmodified_since = d.pop("IfUnmodifiedSince", UNSET)
        if_unmodified_since: Union[Unset, None, datetime.datetime]
        if _if_unmodified_since is None:
            if_unmodified_since = None
        elif isinstance(_if_unmodified_since, Unset):
            if_unmodified_since = UNSET
        else:
            if_unmodified_since = isoparse(_if_unmodified_since)

        max_forwards = d.pop("MaxForwards", UNSET)

        _proxy_authorization = d.pop("ProxyAuthorization", UNSET)
        proxy_authorization: Union[Unset, None, AuthenticationHeaderValue]
        if _proxy_authorization is None:
            proxy_authorization = None
        elif isinstance(_proxy_authorization, Unset):
            proxy_authorization = UNSET
        else:
            proxy_authorization = AuthenticationHeaderValue.from_dict(_proxy_authorization)

        _range_ = d.pop("Range", UNSET)
        range_: Union[Unset, None, RangeHeaderValue]
        if _range_ is None:
            range_ = None
        elif isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = RangeHeaderValue.from_dict(_range_)

        referrer = d.pop("Referrer", UNSET)

        te = []
        _te = d.pop("TE", UNSET)
        for te_item_data in _te or []:
            te_item = TransferCodingWithQualityHeaderValue.from_dict(te_item_data)

            te.append(te_item)

        user_agent = []
        _user_agent = d.pop("UserAgent", UNSET)
        for user_agent_item_data in _user_agent or []:
            user_agent_item = ProductInfoHeaderValue.from_dict(user_agent_item_data)

            user_agent.append(user_agent_item)

        _cache_control = d.pop("CacheControl", UNSET)
        cache_control: Union[Unset, None, CacheControlHeaderValue]
        if _cache_control is None:
            cache_control = None
        elif isinstance(_cache_control, Unset):
            cache_control = UNSET
        else:
            cache_control = CacheControlHeaderValue.from_dict(_cache_control)

        connection = cast(List[str], d.pop("Connection", UNSET))

        connection_close = d.pop("ConnectionClose", UNSET)

        _date = d.pop("Date", UNSET)
        date: Union[Unset, None, datetime.datetime]
        if _date is None:
            date = None
        elif isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        pragma = []
        _pragma = d.pop("Pragma", UNSET)
        for pragma_item_data in _pragma or []:
            pragma_item = NameValueHeaderValue.from_dict(pragma_item_data)

            pragma.append(pragma_item)

        trailer = cast(List[str], d.pop("Trailer", UNSET))

        transfer_encoding = []
        _transfer_encoding = d.pop("TransferEncoding", UNSET)
        for transfer_encoding_item_data in _transfer_encoding or []:
            transfer_encoding_item = TransferCodingHeaderValue.from_dict(transfer_encoding_item_data)

            transfer_encoding.append(transfer_encoding_item)

        transfer_encoding_chunked = d.pop("TransferEncodingChunked", UNSET)

        upgrade = []
        _upgrade = d.pop("Upgrade", UNSET)
        for upgrade_item_data in _upgrade or []:
            upgrade_item = ProductHeaderValue.from_dict(upgrade_item_data)

            upgrade.append(upgrade_item)

        via = []
        _via = d.pop("Via", UNSET)
        for via_item_data in _via or []:
            via_item = ViaHeaderValue.from_dict(via_item_data)

            via.append(via_item)

        warning = []
        _warning = d.pop("Warning", UNSET)
        for warning_item_data in _warning or []:
            warning_item = WarningHeaderValue.from_dict(warning_item_data)

            warning.append(warning_item)

        http_request_headers = cls(
            accept=accept,
            accept_charset=accept_charset,
            accept_encoding=accept_encoding,
            accept_language=accept_language,
            authorization=authorization,
            expect=expect,
            expect_continue=expect_continue,
            from_=from_,
            host=host,
            if_match=if_match,
            if_modified_since=if_modified_since,
            if_none_match=if_none_match,
            if_range=if_range,
            if_unmodified_since=if_unmodified_since,
            max_forwards=max_forwards,
            proxy_authorization=proxy_authorization,
            range_=range_,
            referrer=referrer,
            te=te,
            user_agent=user_agent,
            cache_control=cache_control,
            connection=connection,
            connection_close=connection_close,
            date=date,
            pragma=pragma,
            trailer=trailer,
            transfer_encoding=transfer_encoding,
            transfer_encoding_chunked=transfer_encoding_chunked,
            upgrade=upgrade,
            via=via,
            warning=warning,
        )

        http_request_headers.additional_properties = d
        return http_request_headers

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
