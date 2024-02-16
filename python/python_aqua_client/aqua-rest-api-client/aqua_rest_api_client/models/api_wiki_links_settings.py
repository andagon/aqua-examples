from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_wiki_links_settings_base_urls import ApiWikiLinksSettingsBaseUrls


T = TypeVar("T", bound="ApiWikiLinksSettings")


@attr.s(auto_attribs=True)
class ApiWikiLinksSettings:
    """Contains the necessary settings to create links to the aqua wiki.

    Attributes:
        base_urls (Union[Unset, None, ApiWikiLinksSettingsBaseUrls]): Contains the base URL of the wiki for the
            different
            locales (e.g. en or de).
    """

    base_urls: Union[Unset, None, "ApiWikiLinksSettingsBaseUrls"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        base_urls: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.base_urls, Unset):
            base_urls = self.base_urls.to_dict() if self.base_urls else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if base_urls is not UNSET:
            field_dict["BaseUrls"] = base_urls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_wiki_links_settings_base_urls import ApiWikiLinksSettingsBaseUrls

        d = src_dict.copy()
        _base_urls = d.pop("BaseUrls", UNSET)
        base_urls: Union[Unset, None, ApiWikiLinksSettingsBaseUrls]
        if _base_urls is None:
            base_urls = None
        elif isinstance(_base_urls, Unset):
            base_urls = UNSET
        else:
            base_urls = ApiWikiLinksSettingsBaseUrls.from_dict(_base_urls)

        api_wiki_links_settings = cls(
            base_urls=base_urls,
        )

        return api_wiki_links_settings
