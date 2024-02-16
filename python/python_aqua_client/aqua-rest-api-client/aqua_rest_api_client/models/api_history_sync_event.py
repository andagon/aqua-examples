from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_history_sync_event_type import ApiHistorySyncEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistorySyncEvent")


@attr.s(auto_attribs=True)
class ApiHistorySyncEvent:
    """Contains information about the sync event which has been logged
    in the item's history. Connectors which synchronize items in aqua with
    third-party systems log their errors and the resolving of the errors
    in the history to make them visible to the user.

        Attributes:
            event_type (Union[Unset, ApiHistorySyncEventType]): Indicates the type of sync event.
                This enum has the following values:
                  - `Error` The sync failed with an error.
                  - `ErrorResolved` The sync error has been resolved.
            sync_module_id (Union[Unset, None, int]): The id of the sync in which the error occurred. This can be null
                for some legacy syncs.
            sync_module_type (Union[Unset, None, str]): The type of the sync in which the error occurred.
            sync_name (Union[Unset, None, str]): The name of the sync in which the sync error occurred.
            is_push_error (Union[Unset, bool]): Indicates whether the sync error occurred during a push or pull.
                When true, the error occurred during a push. Otherwise, it occurred
                during a pull.
            is_auto_merge_error (Union[Unset, bool]): Indicates whether the sync error occurred during an automatic
                merge operation. When true, the error occurred during an automatic
                merge. Otherwise, it occurred during a normal sync operation.
            error_message (Union[Unset, None, str]): The actual error message provided by the sync for the sync error.
    """

    event_type: Union[Unset, ApiHistorySyncEventType] = UNSET
    sync_module_id: Union[Unset, None, int] = UNSET
    sync_module_type: Union[Unset, None, str] = UNSET
    sync_name: Union[Unset, None, str] = UNSET
    is_push_error: Union[Unset, bool] = UNSET
    is_auto_merge_error: Union[Unset, bool] = UNSET
    error_message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        sync_module_id = self.sync_module_id
        sync_module_type = self.sync_module_type
        sync_name = self.sync_name
        is_push_error = self.is_push_error
        is_auto_merge_error = self.is_auto_merge_error
        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["EventType"] = event_type
        if sync_module_id is not UNSET:
            field_dict["SyncModuleId"] = sync_module_id
        if sync_module_type is not UNSET:
            field_dict["SyncModuleType"] = sync_module_type
        if sync_name is not UNSET:
            field_dict["SyncName"] = sync_name
        if is_push_error is not UNSET:
            field_dict["IsPushError"] = is_push_error
        if is_auto_merge_error is not UNSET:
            field_dict["IsAutoMergeError"] = is_auto_merge_error
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _event_type = d.pop("EventType", UNSET)
        event_type: Union[Unset, ApiHistorySyncEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = ApiHistorySyncEventType(_event_type)

        sync_module_id = d.pop("SyncModuleId", UNSET)

        sync_module_type = d.pop("SyncModuleType", UNSET)

        sync_name = d.pop("SyncName", UNSET)

        is_push_error = d.pop("IsPushError", UNSET)

        is_auto_merge_error = d.pop("IsAutoMergeError", UNSET)

        error_message = d.pop("ErrorMessage", UNSET)

        api_history_sync_event = cls(
            event_type=event_type,
            sync_module_id=sync_module_id,
            sync_module_type=sync_module_type,
            sync_name=sync_name,
            is_push_error=is_push_error,
            is_auto_merge_error=is_auto_merge_error,
            error_message=error_message,
        )

        return api_history_sync_event
