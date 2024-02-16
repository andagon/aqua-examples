import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_history_attachments import ApiHistoryAttachments
    from ..models.api_history_dependency_changed import ApiHistoryDependencyChanged
    from ..models.api_history_enclosure_changed import ApiHistoryEnclosureChanged
    from ..models.api_history_field_changed import ApiHistoryFieldChanged
    from ..models.api_history_item_created import ApiHistoryItemCreated
    from ..models.api_history_item_migrated import ApiHistoryItemMigrated
    from ..models.api_history_item_moved import ApiHistoryItemMoved
    from ..models.api_history_post_changed import ApiHistoryPostChanged
    from ..models.api_history_sync_event import ApiHistorySyncEvent
    from ..models.api_history_user_c_cs import ApiHistoryUserCCs
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiHistoryEntryDefect")


@attr.s(auto_attribs=True)
class ApiHistoryEntryDefect:
    """
    Attributes:
        id (Union[Unset, int]): The id of the history entry
        time_stamp (Union[Unset, datetime.datetime]): The date and time when the changes were performed
        editor (Union[Unset, None, ApiUserInfo]): The user information
        fields (Union[Unset, None, List['ApiHistoryFieldChanged']]): The list of changes to the fields
        created (Union[Unset, None, ApiHistoryItemCreated]): Information on the creation of the item.
        moved (Union[Unset, None, ApiHistoryItemMoved]):
        attachments (Union[Unset, None, ApiHistoryAttachments]): The list of changes to the attachments of an item.
        user_c_cs (Union[Unset, None, ApiHistoryUserCCs]): Contains the changes to the list of users which have
            subscribed
            to the item and are notified about any changes.
        dependency_changed (Union[Unset, None, ApiHistoryDependencyChanged]): Contains information on the dependency
            which changed.
        post_changed (Union[Unset, None, ApiHistoryPostChanged]): Contains the changes to a certain post.
        sync_event (Union[Unset, None, ApiHistorySyncEvent]): Contains information about the sync event which has been
            logged
            in the item's history. Connectors which synchronize items in aqua with
            third-party systems log their errors and the resolving of the errors
            in the history to make them visible to the user.
        migrated (Union[Unset, None, ApiHistoryItemMigrated]): Information on the migration of the item from a third-
            party system.
        enclosures (Union[Unset, None, List['ApiHistoryEnclosureChanged']]): A list with all changes to the enclosures
            of this defect.
    """

    id: Union[Unset, int] = UNSET
    time_stamp: Union[Unset, datetime.datetime] = UNSET
    editor: Union[Unset, None, "ApiUserInfo"] = UNSET
    fields: Union[Unset, None, List["ApiHistoryFieldChanged"]] = UNSET
    created: Union[Unset, None, "ApiHistoryItemCreated"] = UNSET
    moved: Union[Unset, None, "ApiHistoryItemMoved"] = UNSET
    attachments: Union[Unset, None, "ApiHistoryAttachments"] = UNSET
    user_c_cs: Union[Unset, None, "ApiHistoryUserCCs"] = UNSET
    dependency_changed: Union[Unset, None, "ApiHistoryDependencyChanged"] = UNSET
    post_changed: Union[Unset, None, "ApiHistoryPostChanged"] = UNSET
    sync_event: Union[Unset, None, "ApiHistorySyncEvent"] = UNSET
    migrated: Union[Unset, None, "ApiHistoryItemMigrated"] = UNSET
    enclosures: Union[Unset, None, List["ApiHistoryEnclosureChanged"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        time_stamp: Union[Unset, str] = UNSET
        if not isinstance(self.time_stamp, Unset):
            time_stamp = self.time_stamp.isoformat()

        editor: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.editor, Unset):
            editor = self.editor.to_dict() if self.editor else None

        fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            if self.fields is None:
                fields = None
            else:
                fields = []
                for fields_item_data in self.fields:
                    fields_item = fields_item_data.to_dict()

                    fields.append(fields_item)

        created: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict() if self.created else None

        moved: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.moved, Unset):
            moved = self.moved.to_dict() if self.moved else None

        attachments: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict() if self.attachments else None

        user_c_cs: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user_c_cs, Unset):
            user_c_cs = self.user_c_cs.to_dict() if self.user_c_cs else None

        dependency_changed: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.dependency_changed, Unset):
            dependency_changed = self.dependency_changed.to_dict() if self.dependency_changed else None

        post_changed: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.post_changed, Unset):
            post_changed = self.post_changed.to_dict() if self.post_changed else None

        sync_event: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sync_event, Unset):
            sync_event = self.sync_event.to_dict() if self.sync_event else None

        migrated: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.migrated, Unset):
            migrated = self.migrated.to_dict() if self.migrated else None

        enclosures: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.enclosures, Unset):
            if self.enclosures is None:
                enclosures = None
            else:
                enclosures = []
                for enclosures_item_data in self.enclosures:
                    enclosures_item = enclosures_item_data.to_dict()

                    enclosures.append(enclosures_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if time_stamp is not UNSET:
            field_dict["TimeStamp"] = time_stamp
        if editor is not UNSET:
            field_dict["Editor"] = editor
        if fields is not UNSET:
            field_dict["Fields"] = fields
        if created is not UNSET:
            field_dict["Created"] = created
        if moved is not UNSET:
            field_dict["Moved"] = moved
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments
        if user_c_cs is not UNSET:
            field_dict["UserCCs"] = user_c_cs
        if dependency_changed is not UNSET:
            field_dict["DependencyChanged"] = dependency_changed
        if post_changed is not UNSET:
            field_dict["PostChanged"] = post_changed
        if sync_event is not UNSET:
            field_dict["SyncEvent"] = sync_event
        if migrated is not UNSET:
            field_dict["Migrated"] = migrated
        if enclosures is not UNSET:
            field_dict["Enclosures"] = enclosures

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_history_attachments import ApiHistoryAttachments
        from ..models.api_history_dependency_changed import ApiHistoryDependencyChanged
        from ..models.api_history_enclosure_changed import ApiHistoryEnclosureChanged
        from ..models.api_history_field_changed import ApiHistoryFieldChanged
        from ..models.api_history_item_created import ApiHistoryItemCreated
        from ..models.api_history_item_migrated import ApiHistoryItemMigrated
        from ..models.api_history_item_moved import ApiHistoryItemMoved
        from ..models.api_history_post_changed import ApiHistoryPostChanged
        from ..models.api_history_sync_event import ApiHistorySyncEvent
        from ..models.api_history_user_c_cs import ApiHistoryUserCCs
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _time_stamp = d.pop("TimeStamp", UNSET)
        time_stamp: Union[Unset, datetime.datetime]
        if isinstance(_time_stamp, Unset):
            time_stamp = UNSET
        else:
            time_stamp = isoparse(_time_stamp)

        _editor = d.pop("Editor", UNSET)
        editor: Union[Unset, None, ApiUserInfo]
        if _editor is None:
            editor = None
        elif isinstance(_editor, Unset):
            editor = UNSET
        else:
            editor = ApiUserInfo.from_dict(_editor)

        fields = []
        _fields = d.pop("Fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ApiHistoryFieldChanged.from_dict(fields_item_data)

            fields.append(fields_item)

        _created = d.pop("Created", UNSET)
        created: Union[Unset, None, ApiHistoryItemCreated]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = ApiHistoryItemCreated.from_dict(_created)

        _moved = d.pop("Moved", UNSET)
        moved: Union[Unset, None, ApiHistoryItemMoved]
        if _moved is None:
            moved = None
        elif isinstance(_moved, Unset):
            moved = UNSET
        else:
            moved = ApiHistoryItemMoved.from_dict(_moved)

        _attachments = d.pop("Attachments", UNSET)
        attachments: Union[Unset, None, ApiHistoryAttachments]
        if _attachments is None:
            attachments = None
        elif isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = ApiHistoryAttachments.from_dict(_attachments)

        _user_c_cs = d.pop("UserCCs", UNSET)
        user_c_cs: Union[Unset, None, ApiHistoryUserCCs]
        if _user_c_cs is None:
            user_c_cs = None
        elif isinstance(_user_c_cs, Unset):
            user_c_cs = UNSET
        else:
            user_c_cs = ApiHistoryUserCCs.from_dict(_user_c_cs)

        _dependency_changed = d.pop("DependencyChanged", UNSET)
        dependency_changed: Union[Unset, None, ApiHistoryDependencyChanged]
        if _dependency_changed is None:
            dependency_changed = None
        elif isinstance(_dependency_changed, Unset):
            dependency_changed = UNSET
        else:
            dependency_changed = ApiHistoryDependencyChanged.from_dict(_dependency_changed)

        _post_changed = d.pop("PostChanged", UNSET)
        post_changed: Union[Unset, None, ApiHistoryPostChanged]
        if _post_changed is None:
            post_changed = None
        elif isinstance(_post_changed, Unset):
            post_changed = UNSET
        else:
            post_changed = ApiHistoryPostChanged.from_dict(_post_changed)

        _sync_event = d.pop("SyncEvent", UNSET)
        sync_event: Union[Unset, None, ApiHistorySyncEvent]
        if _sync_event is None:
            sync_event = None
        elif isinstance(_sync_event, Unset):
            sync_event = UNSET
        else:
            sync_event = ApiHistorySyncEvent.from_dict(_sync_event)

        _migrated = d.pop("Migrated", UNSET)
        migrated: Union[Unset, None, ApiHistoryItemMigrated]
        if _migrated is None:
            migrated = None
        elif isinstance(_migrated, Unset):
            migrated = UNSET
        else:
            migrated = ApiHistoryItemMigrated.from_dict(_migrated)

        enclosures = []
        _enclosures = d.pop("Enclosures", UNSET)
        for enclosures_item_data in _enclosures or []:
            enclosures_item = ApiHistoryEnclosureChanged.from_dict(enclosures_item_data)

            enclosures.append(enclosures_item)

        api_history_entry_defect = cls(
            id=id,
            time_stamp=time_stamp,
            editor=editor,
            fields=fields,
            created=created,
            moved=moved,
            attachments=attachments,
            user_c_cs=user_c_cs,
            dependency_changed=dependency_changed,
            post_changed=post_changed,
            sync_event=sync_event,
            migrated=migrated,
            enclosures=enclosures,
        )

        api_history_entry_defect.additional_properties = d
        return api_history_entry_defect

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
