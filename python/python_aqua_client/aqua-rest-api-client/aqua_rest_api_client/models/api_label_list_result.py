from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_label import ApiLabel


T = TypeVar("T", bound="ApiLabelListResult")


@attr.s(auto_attribs=True)
class ApiLabelListResult:
    """
    Attributes:
        items (Union[Unset, None, List['ApiLabel']]):
    """

    items: Union[Unset, None, List["ApiLabel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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
        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_label import ApiLabel

        d = src_dict.copy()
        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = ApiLabel.from_dict(items_item_data)

            items.append(items_item)

        api_label_list_result = cls(
            items=items,
        )

        return api_label_list_result
