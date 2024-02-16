from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_info import ApiItemInfo


T = TypeVar("T", bound="ApiItemListWidgetData")


@attr.s(auto_attribs=True)
class ApiItemListWidgetData:
    """
    Attributes:
        data_type (str):
        count (Union[Unset, None, int]): The total number of items which match the filter in the
            widget defintion.
        items (Union[Unset, None, List['ApiItemInfo']]): The actual items. Only a subset of the matching items is
            included in the response depending on the pagination settings
            in the widget's data specification.
    """

    data_type: str
    count: Union[Unset, None, int] = UNSET
    items: Union[Unset, None, List["ApiItemInfo"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_type = self.data_type
        count = self.count
        items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            if self.items is None:
                items = None
            else:
                items = []
                for items_item_data in self.items:
                    items_item = items_item_data.to_dict()

                    items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DataType": data_type,
            }
        )
        if count is not UNSET:
            field_dict["Count"] = count
        if items is not UNSET:
            field_dict["Items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_info import ApiItemInfo

        d = src_dict.copy()
        data_type = d.pop("DataType")

        count = d.pop("Count", UNSET)

        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = ApiItemInfo.from_dict(items_item_data)

            items.append(items_item)

        api_item_list_widget_data = cls(
            data_type=data_type,
            count=count,
            items=items,
        )

        api_item_list_widget_data.additional_properties = d
        return api_item_list_widget_data

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
