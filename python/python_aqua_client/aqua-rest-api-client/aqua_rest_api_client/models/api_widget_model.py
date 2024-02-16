from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiWidgetModel")


@attr.s(auto_attribs=True)
class ApiWidgetModel:
    """Base class for all widget models.

    Attributes:
        widget_type (str):
    """

    widget_type: str

    def to_dict(self) -> Dict[str, Any]:
        widget_type = self.widget_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "WidgetType": widget_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        widget_type = d.pop("WidgetType")

        api_widget_model = cls(
            widget_type=widget_type,
        )

        return api_widget_model
