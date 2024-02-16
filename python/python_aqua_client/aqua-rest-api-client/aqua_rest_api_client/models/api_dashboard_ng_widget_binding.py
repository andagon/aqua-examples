from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_folder import ApiProjectFolder


T = TypeVar("T", bound="ApiDashboardNGWidgetBinding")


@attr.s(auto_attribs=True)
class ApiDashboardNGWidgetBinding:
    """Specifies the binding (project and folder) as well as recursive flag of a widget.

    Attributes:
        project_id (Union[Unset, int]): The id of the project.
            This field is required when saving.
        folder_id (Union[Unset, int]): The id of the folder or zero (root folder).
            This field is required when saving.
        recursive (Union[Unset, bool]): Specifies whether data should be loaded from the all subfolder or only from
            given folder.
            This field is required when saving.
        project_name (Union[Unset, None, str]): The name of the project.
            This field is ignored when saving.
        text (Union[Unset, None, str]): The human readable path as text. The path consists of the project name and
            the folder names separated by slashes.
            This field is ignored when saving.
            WARNING! This field can be null in case the folder has been deleted.
        path (Union[Unset, None, List['ApiProjectFolder']]): Provides a list of folders with the complete path. The
            order of items corresponds to the path. The project itself is not contained.
            This field is ignored when saving.
            WARNING! This field can be null in case the folder has been deleted.
    """

    project_id: Union[Unset, int] = UNSET
    folder_id: Union[Unset, int] = UNSET
    recursive: Union[Unset, bool] = UNSET
    project_name: Union[Unset, None, str] = UNSET
    text: Union[Unset, None, str] = UNSET
    path: Union[Unset, None, List["ApiProjectFolder"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        folder_id = self.folder_id
        recursive = self.recursive
        project_name = self.project_name
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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if recursive is not UNSET:
            field_dict["Recursive"] = recursive
        if project_name is not UNSET:
            field_dict["ProjectName"] = project_name
        if text is not UNSET:
            field_dict["Text"] = text
        if path is not UNSET:
            field_dict["Path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_folder import ApiProjectFolder

        d = src_dict.copy()
        project_id = d.pop("ProjectId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        recursive = d.pop("Recursive", UNSET)

        project_name = d.pop("ProjectName", UNSET)

        text = d.pop("Text", UNSET)

        path = []
        _path = d.pop("Path", UNSET)
        for path_item_data in _path or []:
            path_item = ApiProjectFolder.from_dict(path_item_data)

            path.append(path_item)

        api_dashboard_ng_widget_binding = cls(
            project_id=project_id,
            folder_id=folder_id,
            recursive=recursive,
            project_name=project_name,
            text=text,
            path=path,
        )

        return api_dashboard_ng_widget_binding
