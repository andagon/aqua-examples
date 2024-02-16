from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_file_upload_info import ApiFileUploadInfo
    from ..models.api_project_create_source import ApiProjectCreateSource


T = TypeVar("T", bound="ApiProjectCreate")


@attr.s(auto_attribs=True)
class ApiProjectCreate:
    """Contains necessary information to create a new project.

    Attributes:
        name (Union[Unset, None, str]): The name of the project.
        source_project (Union[Unset, None, ApiProjectCreateSource]): Contains informations about the source project used
            to create a new project.
        uploaded_configuration (Union[Unset, None, ApiFileUploadInfo]): Contains metadata for an uploaded image.
    """

    name: Union[Unset, None, str] = UNSET
    source_project: Union[Unset, None, "ApiProjectCreateSource"] = UNSET
    uploaded_configuration: Union[Unset, None, "ApiFileUploadInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        source_project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.source_project, Unset):
            source_project = self.source_project.to_dict() if self.source_project else None

        uploaded_configuration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.uploaded_configuration, Unset):
            uploaded_configuration = self.uploaded_configuration.to_dict() if self.uploaded_configuration else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if source_project is not UNSET:
            field_dict["SourceProject"] = source_project
        if uploaded_configuration is not UNSET:
            field_dict["UploadedConfiguration"] = uploaded_configuration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_file_upload_info import ApiFileUploadInfo
        from ..models.api_project_create_source import ApiProjectCreateSource

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        _source_project = d.pop("SourceProject", UNSET)
        source_project: Union[Unset, None, ApiProjectCreateSource]
        if _source_project is None:
            source_project = None
        elif isinstance(_source_project, Unset):
            source_project = UNSET
        else:
            source_project = ApiProjectCreateSource.from_dict(_source_project)

        _uploaded_configuration = d.pop("UploadedConfiguration", UNSET)
        uploaded_configuration: Union[Unset, None, ApiFileUploadInfo]
        if _uploaded_configuration is None:
            uploaded_configuration = None
        elif isinstance(_uploaded_configuration, Unset):
            uploaded_configuration = UNSET
        else:
            uploaded_configuration = ApiFileUploadInfo.from_dict(_uploaded_configuration)

        api_project_create = cls(
            name=name,
            source_project=source_project,
            uploaded_configuration=uploaded_configuration,
        )

        return api_project_create
