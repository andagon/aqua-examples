from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectFolderPatchMove")


@attr.s(auto_attribs=True)
class ApiProjectFolderPatchMove:
    """
    Attributes:
        operation_type (str):
        target_parent_folder_id (Union[Unset, int]):
    """

    operation_type: str
    target_parent_folder_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        target_parent_folder_id = self.target_parent_folder_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if target_parent_folder_id is not UNSET:
            field_dict["TargetParentFolderId"] = target_parent_folder_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        target_parent_folder_id = d.pop("TargetParentFolderId", UNSET)

        api_project_folder_patch_move = cls(
            operation_type=operation_type,
            target_parent_folder_id=target_parent_folder_id,
        )

        api_project_folder_patch_move.additional_properties = d
        return api_project_folder_patch_move

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
