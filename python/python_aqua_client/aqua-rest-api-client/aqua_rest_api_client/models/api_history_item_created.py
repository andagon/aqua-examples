from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_history_creation_mode import ApiHistoryCreationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_info import ApiItemInfo


T = TypeVar("T", bound="ApiHistoryItemCreated")


@attr.s(auto_attribs=True)
class ApiHistoryItemCreated:
    """Information on the creation of the item.

    Attributes:
        creation_mode (Union[Unset, ApiHistoryCreationMode]): Identifies how the item was created
            This enum has the following values:
              - `CopyOfItem` The item was created as a copy of an existing item
              - `EmptyItem` The item was created as an empty item
              - `NewVersionOfItem` The item was created as a new version of an existing item
        source (Union[Unset, None, ApiItemInfo]):
    """

    creation_mode: Union[Unset, ApiHistoryCreationMode] = UNSET
    source: Union[Unset, None, "ApiItemInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        creation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.creation_mode, Unset):
            creation_mode = self.creation_mode.value

        source: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict() if self.source else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if creation_mode is not UNSET:
            field_dict["CreationMode"] = creation_mode
        if source is not UNSET:
            field_dict["Source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_info import ApiItemInfo

        d = src_dict.copy()
        _creation_mode = d.pop("CreationMode", UNSET)
        creation_mode: Union[Unset, ApiHistoryCreationMode]
        if isinstance(_creation_mode, Unset):
            creation_mode = UNSET
        else:
            creation_mode = ApiHistoryCreationMode(_creation_mode)

        _source = d.pop("Source", UNSET)
        source: Union[Unset, None, ApiItemInfo]
        if _source is None:
            source = None
        elif isinstance(_source, Unset):
            source = UNSET
        else:
            source = ApiItemInfo.from_dict(_source)

        api_history_item_created = cls(
            creation_mode=creation_mode,
            source=source,
        )

        return api_history_item_created
