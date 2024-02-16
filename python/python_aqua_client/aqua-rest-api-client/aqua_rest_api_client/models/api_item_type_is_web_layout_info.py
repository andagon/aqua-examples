from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemTypeIsWebLayoutInfo")


@attr.s(auto_attribs=True)
class ApiItemTypeIsWebLayoutInfo:
    """Contains the meta-information of a base object template which is shown by the item type
    and the information where the layout was created.

        Attributes:
            item_type (Union[Unset, ApiItemType]): Identifies the type of item.
                This enum has the following values:
                  - `Defect`
                  - `ExternalJira`
                  - `ExternalOtrs`
                  - `Requirement`
                  - `Script`
                  - `TestCase`
                  - `TestExecution`
                  - `TestScenario`
            is_web_layout (Union[Unset, bool]): Indicates whether the layout was created in web client.
    """

    item_type: Union[Unset, ApiItemType] = UNSET
    is_web_layout: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        is_web_layout = self.is_web_layout

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if is_web_layout is not UNSET:
            field_dict["IsWebLayout"] = is_web_layout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        is_web_layout = d.pop("IsWebLayout", UNSET)

        api_item_type_is_web_layout_info = cls(
            item_type=item_type,
            is_web_layout=is_web_layout,
        )

        return api_item_type_is_web_layout_info
