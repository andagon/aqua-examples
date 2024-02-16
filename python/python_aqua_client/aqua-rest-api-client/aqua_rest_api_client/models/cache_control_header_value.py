from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_value_header_value import NameValueHeaderValue


T = TypeVar("T", bound="CacheControlHeaderValue")


@attr.s(auto_attribs=True)
class CacheControlHeaderValue:
    """
    Attributes:
        no_cache (Union[Unset, bool]):
        no_cache_headers (Union[Unset, None, List[str]]):
        no_store (Union[Unset, bool]):
        max_age (Union[Unset, None, str]):
        shared_max_age (Union[Unset, None, str]):
        max_stale (Union[Unset, bool]):
        max_stale_limit (Union[Unset, None, str]):
        min_fresh (Union[Unset, None, str]):
        no_transform (Union[Unset, bool]):
        only_if_cached (Union[Unset, bool]):
        public (Union[Unset, bool]):
        private (Union[Unset, bool]):
        private_headers (Union[Unset, None, List[str]]):
        must_revalidate (Union[Unset, bool]):
        proxy_revalidate (Union[Unset, bool]):
        extensions (Union[Unset, None, List['NameValueHeaderValue']]):
    """

    no_cache: Union[Unset, bool] = UNSET
    no_cache_headers: Union[Unset, None, List[str]] = UNSET
    no_store: Union[Unset, bool] = UNSET
    max_age: Union[Unset, None, str] = UNSET
    shared_max_age: Union[Unset, None, str] = UNSET
    max_stale: Union[Unset, bool] = UNSET
    max_stale_limit: Union[Unset, None, str] = UNSET
    min_fresh: Union[Unset, None, str] = UNSET
    no_transform: Union[Unset, bool] = UNSET
    only_if_cached: Union[Unset, bool] = UNSET
    public: Union[Unset, bool] = UNSET
    private: Union[Unset, bool] = UNSET
    private_headers: Union[Unset, None, List[str]] = UNSET
    must_revalidate: Union[Unset, bool] = UNSET
    proxy_revalidate: Union[Unset, bool] = UNSET
    extensions: Union[Unset, None, List["NameValueHeaderValue"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        no_cache = self.no_cache
        no_cache_headers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.no_cache_headers, Unset):
            if self.no_cache_headers is None:
                no_cache_headers = None
            else:
                no_cache_headers = self.no_cache_headers

        no_store = self.no_store
        max_age = self.max_age
        shared_max_age = self.shared_max_age
        max_stale = self.max_stale
        max_stale_limit = self.max_stale_limit
        min_fresh = self.min_fresh
        no_transform = self.no_transform
        only_if_cached = self.only_if_cached
        public = self.public
        private = self.private
        private_headers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.private_headers, Unset):
            if self.private_headers is None:
                private_headers = None
            else:
                private_headers = self.private_headers

        must_revalidate = self.must_revalidate
        proxy_revalidate = self.proxy_revalidate
        extensions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extensions, Unset):
            if self.extensions is None:
                extensions = None
            else:
                extensions = []
                for extensions_item_data in self.extensions:
                    extensions_item = extensions_item_data.to_dict()

                    extensions.append(extensions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if no_cache is not UNSET:
            field_dict["NoCache"] = no_cache
        if no_cache_headers is not UNSET:
            field_dict["NoCacheHeaders"] = no_cache_headers
        if no_store is not UNSET:
            field_dict["NoStore"] = no_store
        if max_age is not UNSET:
            field_dict["MaxAge"] = max_age
        if shared_max_age is not UNSET:
            field_dict["SharedMaxAge"] = shared_max_age
        if max_stale is not UNSET:
            field_dict["MaxStale"] = max_stale
        if max_stale_limit is not UNSET:
            field_dict["MaxStaleLimit"] = max_stale_limit
        if min_fresh is not UNSET:
            field_dict["MinFresh"] = min_fresh
        if no_transform is not UNSET:
            field_dict["NoTransform"] = no_transform
        if only_if_cached is not UNSET:
            field_dict["OnlyIfCached"] = only_if_cached
        if public is not UNSET:
            field_dict["Public"] = public
        if private is not UNSET:
            field_dict["Private"] = private
        if private_headers is not UNSET:
            field_dict["PrivateHeaders"] = private_headers
        if must_revalidate is not UNSET:
            field_dict["MustRevalidate"] = must_revalidate
        if proxy_revalidate is not UNSET:
            field_dict["ProxyRevalidate"] = proxy_revalidate
        if extensions is not UNSET:
            field_dict["Extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.name_value_header_value import NameValueHeaderValue

        d = src_dict.copy()
        no_cache = d.pop("NoCache", UNSET)

        no_cache_headers = cast(List[str], d.pop("NoCacheHeaders", UNSET))

        no_store = d.pop("NoStore", UNSET)

        max_age = d.pop("MaxAge", UNSET)

        shared_max_age = d.pop("SharedMaxAge", UNSET)

        max_stale = d.pop("MaxStale", UNSET)

        max_stale_limit = d.pop("MaxStaleLimit", UNSET)

        min_fresh = d.pop("MinFresh", UNSET)

        no_transform = d.pop("NoTransform", UNSET)

        only_if_cached = d.pop("OnlyIfCached", UNSET)

        public = d.pop("Public", UNSET)

        private = d.pop("Private", UNSET)

        private_headers = cast(List[str], d.pop("PrivateHeaders", UNSET))

        must_revalidate = d.pop("MustRevalidate", UNSET)

        proxy_revalidate = d.pop("ProxyRevalidate", UNSET)

        extensions = []
        _extensions = d.pop("Extensions", UNSET)
        for extensions_item_data in _extensions or []:
            extensions_item = NameValueHeaderValue.from_dict(extensions_item_data)

            extensions.append(extensions_item)

        cache_control_header_value = cls(
            no_cache=no_cache,
            no_cache_headers=no_cache_headers,
            no_store=no_store,
            max_age=max_age,
            shared_max_age=shared_max_age,
            max_stale=max_stale,
            max_stale_limit=max_stale_limit,
            min_fresh=min_fresh,
            no_transform=no_transform,
            only_if_cached=only_if_cached,
            public=public,
            private=private,
            private_headers=private_headers,
            must_revalidate=must_revalidate,
            proxy_revalidate=proxy_revalidate,
            extensions=extensions,
        )

        return cache_control_header_value
