from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHtmlContentWidgetDataSpecification")


@attr.s(auto_attribs=True)
class ApiHtmlContentWidgetDataSpecification:
    """The data specification for an HTML content widget

    Attributes:
        url (Union[Unset, None, str]): The URL of the HTML content which should be displayed
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

        api_html_content_widget_data_specification = cls(
            url=url,
        )

        return api_html_content_widget_data_specification
