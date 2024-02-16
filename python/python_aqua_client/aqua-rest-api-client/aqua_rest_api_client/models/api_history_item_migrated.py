from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistoryItemMigrated")


@attr.s(auto_attribs=True)
class ApiHistoryItemMigrated:
    """Information on the migration of the item from a third-party system.

    Attributes:
        info (Union[Unset, None, str]): Some information provided by the migration tool. Most likely
            the name of the third-party system from which the item was migrated
            and or its original id.
        history_download_url (Union[Unset, None, str]): A URL where a file with the history of the item in the third-
            party
            system can be downloaded.
    """

    info: Union[Unset, None, str] = UNSET
    history_download_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        info = self.info
        history_download_url = self.history_download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if info is not UNSET:
            field_dict["Info"] = info
        if history_download_url is not UNSET:
            field_dict["HistoryDownloadUrl"] = history_download_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        info = d.pop("Info", UNSET)

        history_download_url = d.pop("HistoryDownloadUrl", UNSET)

        api_history_item_migrated = cls(
            info=info,
            history_download_url=history_download_url,
        )

        return api_history_item_migrated
