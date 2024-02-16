from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDashboardNGReorderWidgets")


@attr.s(auto_attribs=True)
class ApiDashboardNGReorderWidgets:
    """
    Attributes:
        widget_id (Union[Unset, int]): The id of the widget.
        new_position (Union[Unset, int]): The new position of the widget.
    """

    widget_id: Union[Unset, int] = UNSET
    new_position: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        widget_id = self.widget_id
        new_position = self.new_position

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if widget_id is not UNSET:
            field_dict["WidgetId"] = widget_id
        if new_position is not UNSET:
            field_dict["NewPosition"] = new_position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        widget_id = d.pop("WidgetId", UNSET)

        new_position = d.pop("NewPosition", UNSET)

        api_dashboard_ng_reorder_widgets = cls(
            widget_id=widget_id,
            new_position=new_position,
        )

        return api_dashboard_ng_reorder_widgets
