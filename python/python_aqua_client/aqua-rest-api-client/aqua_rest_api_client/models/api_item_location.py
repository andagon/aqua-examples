from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_folder import ApiProjectFolder


T = TypeVar("T", bound="ApiItemLocation")


@attr.s(auto_attribs=True)
class ApiItemLocation:
    """Specifies the location (project and folder) of an item

    Attributes:
        project_id (Union[Unset, None, int]): The id of the project
        project_name (Union[Unset, None, str]): The name of the project
        folder_id (Union[Unset, None, int]): The id of the folder
        text (Union[Unset, None, str]): The human readable path as text. The path consists of the project name and
            the folder names separated by slashes
        path (Union[Unset, None, List['ApiProjectFolder']]): Provides a list of folders with the complete path. The
            order of items corresponds to the path. The project itself is not contained.
        is_project_archived (Union[Unset, bool]): Indicates whether the project is archived.
    """

    project_id: Union[Unset, None, int] = UNSET
    project_name: Union[Unset, None, str] = UNSET
    folder_id: Union[Unset, None, int] = UNSET
    text: Union[Unset, None, str] = UNSET
    path: Union[Unset, None, List["ApiProjectFolder"]] = UNSET
    is_project_archived: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        project_name = self.project_name
        folder_id = self.folder_id
        text = self.text
        path: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.path, Unset):
            if self.path is None:
                path = None
            else:
                path = []
                for path_item_data in self.path:
                    path_item = path_item_data.to_dict()

                    path.append(path_item)

        is_project_archived = self.is_project_archived

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if project_name is not UNSET:
            field_dict["ProjectName"] = project_name
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if text is not UNSET:
            field_dict["Text"] = text
        if path is not UNSET:
            field_dict["Path"] = path
        if is_project_archived is not UNSET:
            field_dict["IsProjectArchived"] = is_project_archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_folder import ApiProjectFolder

        d = src_dict.copy()
        project_id = d.pop("ProjectId", UNSET)

        project_name = d.pop("ProjectName", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        text = d.pop("Text", UNSET)

        path = []
        _path = d.pop("Path", UNSET)
        for path_item_data in _path or []:
            path_item = ApiProjectFolder.from_dict(path_item_data)

            path.append(path_item)

        is_project_archived = d.pop("IsProjectArchived", UNSET)

        api_item_location = cls(
            project_id=project_id,
            project_name=project_name,
            folder_id=folder_id,
            text=text,
            path=path,
            is_project_archived=is_project_archived,
        )

        return api_item_location
