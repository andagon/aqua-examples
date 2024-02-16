from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..models.api_sync_item_status import ApiSyncItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_edit_layout import ApiEditLayout
    from ..models.api_editable_info import ApiEditableInfo
    from ..models.api_field_value_date_time import ApiFieldValueDateTime
    from ..models.api_field_with_value import ApiFieldWithValue
    from ..models.api_item_location import ApiItemLocation
    from ..models.api_item_permissions import ApiItemPermissions
    from ..models.api_item_version import ApiItemVersion


T = TypeVar("T", bound="ApiScript")


@attr.s(auto_attribs=True)
class ApiScript:
    """
    Attributes:
        id (Union[Unset, int]): The id of the item
        formatted_id (Union[Unset, None, str]): A nicely formatted version of the id which
            contains the item type identifier and the numerical
            id padded to six digits. E.g.: RQ004242.
            This id is only for presentation. You must use the
            numerical id for all requests.
        type (Union[Unset, ApiItemType]): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        name (Union[Unset, None, str]): The name of the item
        version (Union[Unset, None, ApiItemVersion]): Version information for an item.
        archived (Union[Unset, bool]): The archived flag of the item.
        location (Union[Unset, None, ApiItemLocation]): Specifies the location (project and folder) of an item
        last_modified (Union[Unset, None, ApiFieldValueDateTime]):
        editable_info (Union[Unset, None, ApiEditableInfo]): Contains information about editable status of an item.
        permissions (Union[Unset, None, ApiItemPermissions]): Represents permissions of an item. Intended to be
            subclassed
            by classes with more fine-grained permission set for given context.
        has_dependency (Union[Unset, bool]): True if item has any dependency.
        has_files (Union[Unset, bool]): True if item has any attachments.
        sync_status (Union[Unset, None, ApiSyncItemStatus]):
            This enum has the following values:
              - `Error` The item is synced and there was a problem in the sync, sync stopped
              - `Ok` The item is synced and sync status is ok
              - `Unsynced` The item is not part of any sync
              - `Warning` The item is synced and there was a problem in the sync, sync stopped
        details (Union[Unset, None, List['ApiFieldWithValue']]): Contains all the different fields specified for this
            item type
        edit_layout (Union[Unset, None, ApiEditLayout]):
    """

    id: Union[Unset, int] = UNSET
    formatted_id: Union[Unset, None, str] = UNSET
    type: Union[Unset, ApiItemType] = UNSET
    name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, "ApiItemVersion"] = UNSET
    archived: Union[Unset, bool] = UNSET
    location: Union[Unset, None, "ApiItemLocation"] = UNSET
    last_modified: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    editable_info: Union[Unset, None, "ApiEditableInfo"] = UNSET
    permissions: Union[Unset, None, "ApiItemPermissions"] = UNSET
    has_dependency: Union[Unset, bool] = UNSET
    has_files: Union[Unset, bool] = UNSET
    sync_status: Union[Unset, None, ApiSyncItemStatus] = UNSET
    details: Union[Unset, None, List["ApiFieldWithValue"]] = UNSET
    edit_layout: Union[Unset, None, "ApiEditLayout"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        formatted_id = self.formatted_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        name = self.name
        version: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict() if self.version else None

        archived = self.archived
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        last_modified: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.to_dict() if self.last_modified else None

        editable_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.editable_info, Unset):
            editable_info = self.editable_info.to_dict() if self.editable_info else None

        permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict() if self.permissions else None

        has_dependency = self.has_dependency
        has_files = self.has_files
        sync_status: Union[Unset, None, str] = UNSET
        if not isinstance(self.sync_status, Unset):
            sync_status = self.sync_status.value if self.sync_status else None

        details: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            if self.details is None:
                details = None
            else:
                details = []
                for details_item_data in self.details:
                    details_item = details_item_data.to_dict()

                    details.append(details_item)

        edit_layout: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_layout, Unset):
            edit_layout = self.edit_layout.to_dict() if self.edit_layout else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if formatted_id is not UNSET:
            field_dict["FormattedId"] = formatted_id
        if type is not UNSET:
            field_dict["Type"] = type
        if name is not UNSET:
            field_dict["Name"] = name
        if version is not UNSET:
            field_dict["Version"] = version
        if archived is not UNSET:
            field_dict["Archived"] = archived
        if location is not UNSET:
            field_dict["Location"] = location
        if last_modified is not UNSET:
            field_dict["LastModified"] = last_modified
        if editable_info is not UNSET:
            field_dict["EditableInfo"] = editable_info
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions
        if has_dependency is not UNSET:
            field_dict["HasDependency"] = has_dependency
        if has_files is not UNSET:
            field_dict["HasFiles"] = has_files
        if sync_status is not UNSET:
            field_dict["SyncStatus"] = sync_status
        if details is not UNSET:
            field_dict["Details"] = details
        if edit_layout is not UNSET:
            field_dict["EditLayout"] = edit_layout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_edit_layout import ApiEditLayout
        from ..models.api_editable_info import ApiEditableInfo
        from ..models.api_field_value_date_time import ApiFieldValueDateTime
        from ..models.api_field_with_value import ApiFieldWithValue
        from ..models.api_item_location import ApiItemLocation
        from ..models.api_item_permissions import ApiItemPermissions
        from ..models.api_item_version import ApiItemVersion

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        formatted_id = d.pop("FormattedId", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiItemType(_type)

        name = d.pop("Name", UNSET)

        _version = d.pop("Version", UNSET)
        version: Union[Unset, None, ApiItemVersion]
        if _version is None:
            version = None
        elif isinstance(_version, Unset):
            version = UNSET
        else:
            version = ApiItemVersion.from_dict(_version)

        archived = d.pop("Archived", UNSET)

        _location = d.pop("Location", UNSET)
        location: Union[Unset, None, ApiItemLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = ApiItemLocation.from_dict(_location)

        _last_modified = d.pop("LastModified", UNSET)
        last_modified: Union[Unset, None, ApiFieldValueDateTime]
        if _last_modified is None:
            last_modified = None
        elif isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = ApiFieldValueDateTime.from_dict(_last_modified)

        _editable_info = d.pop("EditableInfo", UNSET)
        editable_info: Union[Unset, None, ApiEditableInfo]
        if _editable_info is None:
            editable_info = None
        elif isinstance(_editable_info, Unset):
            editable_info = UNSET
        else:
            editable_info = ApiEditableInfo.from_dict(_editable_info)

        _permissions = d.pop("Permissions", UNSET)
        permissions: Union[Unset, None, ApiItemPermissions]
        if _permissions is None:
            permissions = None
        elif isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ApiItemPermissions.from_dict(_permissions)

        has_dependency = d.pop("HasDependency", UNSET)

        has_files = d.pop("HasFiles", UNSET)

        _sync_status = d.pop("SyncStatus", UNSET)
        sync_status: Union[Unset, None, ApiSyncItemStatus]
        if _sync_status is None:
            sync_status = None
        elif isinstance(_sync_status, Unset):
            sync_status = UNSET
        else:
            sync_status = ApiSyncItemStatus(_sync_status)

        details = []
        _details = d.pop("Details", UNSET)
        for details_item_data in _details or []:
            details_item = ApiFieldWithValue.from_dict(details_item_data)

            details.append(details_item)

        _edit_layout = d.pop("EditLayout", UNSET)
        edit_layout: Union[Unset, None, ApiEditLayout]
        if _edit_layout is None:
            edit_layout = None
        elif isinstance(_edit_layout, Unset):
            edit_layout = UNSET
        else:
            edit_layout = ApiEditLayout.from_dict(_edit_layout)

        api_script = cls(
            id=id,
            formatted_id=formatted_id,
            type=type,
            name=name,
            version=version,
            archived=archived,
            location=location,
            last_modified=last_modified,
            editable_info=editable_info,
            permissions=permissions,
            has_dependency=has_dependency,
            has_files=has_files,
            sync_status=sync_status,
            details=details,
            edit_layout=edit_layout,
        )

        api_script.additional_properties = d
        return api_script

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
