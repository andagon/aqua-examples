from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemListWidgetSorting")


@attr.s(auto_attribs=True)
class ApiItemListWidgetSorting:
    """Represent sorting in item list widget

    Attributes:
        field_title (Union[Unset, None, str]): Title of the field to sort by
        ascending (Union[Unset, bool]): Sorting direction - if true then ascending, descending otherwise.
    """

    field_title: Union[Unset, None, str] = UNSET
    ascending: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_title = self.field_title
        ascending = self.ascending

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_title is not UNSET:
            field_dict["FieldTitle"] = field_title
        if ascending is not UNSET:
            field_dict["Ascending"] = ascending

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_title = d.pop("FieldTitle", UNSET)

        ascending = d.pop("Ascending", UNSET)

        api_item_list_widget_sorting = cls(
            field_title=field_title,
            ascending=ascending,
        )

        return api_item_list_widget_sorting
