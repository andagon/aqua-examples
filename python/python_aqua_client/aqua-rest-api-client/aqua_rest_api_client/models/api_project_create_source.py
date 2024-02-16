from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectCreateSource")


@attr.s(auto_attribs=True)
class ApiProjectCreateSource:
    """Contains informations about the source project used to create a new project.

    Attributes:
        project_id (Union[Unset, int]): The id of the source project.
        copy_items (Union[Unset, bool]): If true the project configuration and items will be copied, otherwise only
            project configuration will be copied.
        share_configuration (Union[Unset, bool]): If true shares the configuration with the source project.
    """

    project_id: Union[Unset, int] = UNSET
    copy_items: Union[Unset, bool] = UNSET
    share_configuration: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        copy_items = self.copy_items
        share_configuration = self.share_configuration

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if copy_items is not UNSET:
            field_dict["CopyItems"] = copy_items
        if share_configuration is not UNSET:
            field_dict["ShareConfiguration"] = share_configuration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = d.pop("ProjectId", UNSET)

        copy_items = d.pop("CopyItems", UNSET)

        share_configuration = d.pop("ShareConfiguration", UNSET)

        api_project_create_source = cls(
            project_id=project_id,
            copy_items=copy_items,
            share_configuration=share_configuration,
        )

        return api_project_create_source
