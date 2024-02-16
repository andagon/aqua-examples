from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_html_content_widget_data_specification import ApiHtmlContentWidgetDataSpecification


T = TypeVar("T", bound="ApiHtmlContentWidgetModel")


@attr.s(auto_attribs=True)
class ApiHtmlContentWidgetModel:
    """
    Attributes:
        widget_type (str):
        html_content_widget_data_specification (Union[Unset, None, ApiHtmlContentWidgetDataSpecification]): The data
            specification for an HTML content widget
    """

    widget_type: str
    html_content_widget_data_specification: Union[Unset, None, "ApiHtmlContentWidgetDataSpecification"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        widget_type = self.widget_type
        html_content_widget_data_specification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.html_content_widget_data_specification, Unset):
            html_content_widget_data_specification = (
                self.html_content_widget_data_specification.to_dict()
                if self.html_content_widget_data_specification
                else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "WidgetType": widget_type,
            }
        )
        if html_content_widget_data_specification is not UNSET:
            field_dict["HtmlContentWidgetDataSpecification"] = html_content_widget_data_specification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_html_content_widget_data_specification import ApiHtmlContentWidgetDataSpecification

        d = src_dict.copy()
        widget_type = d.pop("WidgetType")

        _html_content_widget_data_specification = d.pop("HtmlContentWidgetDataSpecification", UNSET)
        html_content_widget_data_specification: Union[Unset, None, ApiHtmlContentWidgetDataSpecification]
        if _html_content_widget_data_specification is None:
            html_content_widget_data_specification = None
        elif isinstance(_html_content_widget_data_specification, Unset):
            html_content_widget_data_specification = UNSET
        else:
            html_content_widget_data_specification = ApiHtmlContentWidgetDataSpecification.from_dict(
                _html_content_widget_data_specification
            )

        api_html_content_widget_model = cls(
            widget_type=widget_type,
            html_content_widget_data_specification=html_content_widget_data_specification,
        )

        api_html_content_widget_model.additional_properties = d
        return api_html_content_widget_model

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
