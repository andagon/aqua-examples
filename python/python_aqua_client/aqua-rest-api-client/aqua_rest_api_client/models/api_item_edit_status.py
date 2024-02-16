from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_editable_info import ApiEditableInfo
    from ..models.api_item_version import ApiItemVersion


T = TypeVar("T", bound="ApiItemEditStatus")


@attr.s(auto_attribs=True)
class ApiItemEditStatus:
    """Edit status information for an item.

    Attributes:
        item_version (Union[Unset, None, ApiItemVersion]): Version information for an item.
        editable_info (Union[Unset, None, ApiEditableInfo]): Contains information about editable status of an item.
    """

    item_version: Union[Unset, None, "ApiItemVersion"] = UNSET
    editable_info: Union[Unset, None, "ApiEditableInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_version: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.item_version, Unset):
            item_version = self.item_version.to_dict() if self.item_version else None

        editable_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.editable_info, Unset):
            editable_info = self.editable_info.to_dict() if self.editable_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_version is not UNSET:
            field_dict["ItemVersion"] = item_version
        if editable_info is not UNSET:
            field_dict["EditableInfo"] = editable_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_editable_info import ApiEditableInfo
        from ..models.api_item_version import ApiItemVersion

        d = src_dict.copy()
        _item_version = d.pop("ItemVersion", UNSET)
        item_version: Union[Unset, None, ApiItemVersion]
        if _item_version is None:
            item_version = None
        elif isinstance(_item_version, Unset):
            item_version = UNSET
        else:
            item_version = ApiItemVersion.from_dict(_item_version)

        _editable_info = d.pop("EditableInfo", UNSET)
        editable_info: Union[Unset, None, ApiEditableInfo]
        if _editable_info is None:
            editable_info = None
        elif isinstance(_editable_info, Unset):
            editable_info = UNSET
        else:
            editable_info = ApiEditableInfo.from_dict(_editable_info)

        api_item_edit_status = cls(
            item_version=item_version,
            editable_info=editable_info,
        )

        return api_item_edit_status
