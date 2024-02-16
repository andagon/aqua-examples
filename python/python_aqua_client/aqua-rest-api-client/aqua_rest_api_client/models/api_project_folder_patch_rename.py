from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectFolderPatchRename")


@attr.s(auto_attribs=True)
class ApiProjectFolderPatchRename:
    """
    Attributes:
        operation_type (str):
        new_name (Union[Unset, None, str]): New name of the folder being updated.
    """

    operation_type: str
    new_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        new_name = self.new_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if new_name is not UNSET:
            field_dict["NewName"] = new_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        new_name = d.pop("NewName", UNSET)

        api_project_folder_patch_rename = cls(
            operation_type=operation_type,
            new_name=new_name,
        )

        api_project_folder_patch_rename.additional_properties = d
        return api_project_folder_patch_rename

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
