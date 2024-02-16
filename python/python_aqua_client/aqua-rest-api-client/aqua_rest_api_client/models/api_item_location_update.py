from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemLocationUpdate")


@attr.s(auto_attribs=True)
class ApiItemLocationUpdate:
    """
    Attributes:
        project_id (Union[Unset, None, int]): The id of the project
        folder_id (Union[Unset, None, int]): The id of the folder
    """

    project_id: Union[Unset, None, int] = UNSET
    folder_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        folder_id = self.folder_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = d.pop("ProjectId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        api_item_location_update = cls(
            project_id=project_id,
            folder_id=folder_id,
        )

        return api_item_location_update
