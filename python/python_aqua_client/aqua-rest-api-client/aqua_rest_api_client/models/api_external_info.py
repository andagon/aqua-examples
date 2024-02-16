from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value_date_time import ApiFieldValueDateTime


T = TypeVar("T", bound="ApiExternalInfo")


@attr.s(auto_attribs=True)
class ApiExternalInfo:
    """ONLT FOR INTERNAL USE

    Contains basic information about a item as requested
    from external system (e.g. JIRA plugin) using search by related external item id (e.g. JIRA Id).
    Please note that in case when current user has no access to view the item, only the Id field
    is properly filled.

        Attributes:
            id (Union[Unset, int]): The id of the item.
            project_id (Union[Unset, int]): The id of the project where test case is located.
                If 0 then item is not accessible for current user.
            folder_id (Union[Unset, int]): The id of the folder where item is located (or 0 if in root folder).
            name (Union[Unset, None, str]): The name of the item.
            date_created (Union[Unset, None, ApiFieldValueDateTime]):
            last_modified (Union[Unset, None, ApiFieldValueDateTime]):
            last_execution_date (Union[Unset, None, ApiFieldValueDateTime]):
    """

    id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    folder_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    date_created: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    last_modified: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    last_execution_date: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        project_id = self.project_id
        folder_id = self.folder_id
        name = self.name
        date_created: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.to_dict() if self.date_created else None

        last_modified: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.to_dict() if self.last_modified else None

        last_execution_date: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_execution_date, Unset):
            last_execution_date = self.last_execution_date.to_dict() if self.last_execution_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if name is not UNSET:
            field_dict["Name"] = name
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if last_modified is not UNSET:
            field_dict["LastModified"] = last_modified
        if last_execution_date is not UNSET:
            field_dict["LastExecutionDate"] = last_execution_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_date_time import ApiFieldValueDateTime

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        name = d.pop("Name", UNSET)

        _date_created = d.pop("DateCreated", UNSET)
        date_created: Union[Unset, None, ApiFieldValueDateTime]
        if _date_created is None:
            date_created = None
        elif isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = ApiFieldValueDateTime.from_dict(_date_created)

        _last_modified = d.pop("LastModified", UNSET)
        last_modified: Union[Unset, None, ApiFieldValueDateTime]
        if _last_modified is None:
            last_modified = None
        elif isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = ApiFieldValueDateTime.from_dict(_last_modified)

        _last_execution_date = d.pop("LastExecutionDate", UNSET)
        last_execution_date: Union[Unset, None, ApiFieldValueDateTime]
        if _last_execution_date is None:
            last_execution_date = None
        elif isinstance(_last_execution_date, Unset):
            last_execution_date = UNSET
        else:
            last_execution_date = ApiFieldValueDateTime.from_dict(_last_execution_date)

        api_external_info = cls(
            id=id,
            project_id=project_id,
            folder_id=folder_id,
            name=name,
            date_created=date_created,
            last_modified=last_modified,
            last_execution_date=last_execution_date,
        )

        return api_external_info
