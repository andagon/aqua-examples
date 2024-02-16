from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value_date_time import ApiFieldValueDateTime
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiOperationLog")


@attr.s(auto_attribs=True)
class ApiOperationLog:
    """
    Attributes:
        id (Union[Unset, int]): The id of this log entry.
        operation_user (Union[Unset, None, ApiUserInfo]): The user information
        operation_date_utc (Union[Unset, None, ApiFieldValueDateTime]):
        project_id (Union[Unset, None, int]): The id of the project
        project_name (Union[Unset, None, str]): The name of the project
        folder_id (Union[Unset, None, int]): The id of the folder
        folder_path (Union[Unset, None, str]): The human readable path as text. The path consists of the project name
            and
            the folder names separated by slashes
        category (Union[Unset, None, str]): Log category path (levels separated by dots).
        entity_type (Union[Unset, None, str]): Related entity type. Depends on category, but usually it is e.g. object
            type (Defect, Requirement, ...), Sprint, ProjectPlan etc.
        entity_id (Union[Unset, None, int]): Related entity id.
        further_info (Union[Unset, None, str]): Additional descriptino of the change (human-readable, in english)
        entity_user (Union[Unset, None, ApiUserInfo]): The user information
    """

    id: Union[Unset, int] = UNSET
    operation_user: Union[Unset, None, "ApiUserInfo"] = UNSET
    operation_date_utc: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    project_id: Union[Unset, None, int] = UNSET
    project_name: Union[Unset, None, str] = UNSET
    folder_id: Union[Unset, None, int] = UNSET
    folder_path: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, str] = UNSET
    entity_type: Union[Unset, None, str] = UNSET
    entity_id: Union[Unset, None, int] = UNSET
    further_info: Union[Unset, None, str] = UNSET
    entity_user: Union[Unset, None, "ApiUserInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        operation_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.operation_user, Unset):
            operation_user = self.operation_user.to_dict() if self.operation_user else None

        operation_date_utc: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.operation_date_utc, Unset):
            operation_date_utc = self.operation_date_utc.to_dict() if self.operation_date_utc else None

        project_id = self.project_id
        project_name = self.project_name
        folder_id = self.folder_id
        folder_path = self.folder_path
        category = self.category
        entity_type = self.entity_type
        entity_id = self.entity_id
        further_info = self.further_info
        entity_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_user, Unset):
            entity_user = self.entity_user.to_dict() if self.entity_user else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if operation_user is not UNSET:
            field_dict["OperationUser"] = operation_user
        if operation_date_utc is not UNSET:
            field_dict["OperationDateUTC"] = operation_date_utc
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if project_name is not UNSET:
            field_dict["ProjectName"] = project_name
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if folder_path is not UNSET:
            field_dict["FolderPath"] = folder_path
        if category is not UNSET:
            field_dict["Category"] = category
        if entity_type is not UNSET:
            field_dict["EntityType"] = entity_type
        if entity_id is not UNSET:
            field_dict["EntityId"] = entity_id
        if further_info is not UNSET:
            field_dict["FurtherInfo"] = further_info
        if entity_user is not UNSET:
            field_dict["EntityUser"] = entity_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_date_time import ApiFieldValueDateTime
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _operation_user = d.pop("OperationUser", UNSET)
        operation_user: Union[Unset, None, ApiUserInfo]
        if _operation_user is None:
            operation_user = None
        elif isinstance(_operation_user, Unset):
            operation_user = UNSET
        else:
            operation_user = ApiUserInfo.from_dict(_operation_user)

        _operation_date_utc = d.pop("OperationDateUTC", UNSET)
        operation_date_utc: Union[Unset, None, ApiFieldValueDateTime]
        if _operation_date_utc is None:
            operation_date_utc = None
        elif isinstance(_operation_date_utc, Unset):
            operation_date_utc = UNSET
        else:
            operation_date_utc = ApiFieldValueDateTime.from_dict(_operation_date_utc)

        project_id = d.pop("ProjectId", UNSET)

        project_name = d.pop("ProjectName", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        folder_path = d.pop("FolderPath", UNSET)

        category = d.pop("Category", UNSET)

        entity_type = d.pop("EntityType", UNSET)

        entity_id = d.pop("EntityId", UNSET)

        further_info = d.pop("FurtherInfo", UNSET)

        _entity_user = d.pop("EntityUser", UNSET)
        entity_user: Union[Unset, None, ApiUserInfo]
        if _entity_user is None:
            entity_user = None
        elif isinstance(_entity_user, Unset):
            entity_user = UNSET
        else:
            entity_user = ApiUserInfo.from_dict(_entity_user)

        api_operation_log = cls(
            id=id,
            operation_user=operation_user,
            operation_date_utc=operation_date_utc,
            project_id=project_id,
            project_name=project_name,
            folder_id=folder_id,
            folder_path=folder_path,
            category=category,
            entity_type=entity_type,
            entity_id=entity_id,
            further_info=further_info,
            entity_user=entity_user,
        )

        return api_operation_log
