from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserProjectFolderAssignmentPatchReplace")


@attr.s(auto_attribs=True)
class ApiUserProjectFolderAssignmentPatchReplace:
    """
    Attributes:
        operation_type (str):
        new_role_id (Union[Unset, int]): New role id.
    """

    operation_type: str
    new_role_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        new_role_id = self.new_role_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if new_role_id is not UNSET:
            field_dict["NewRoleId"] = new_role_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        new_role_id = d.pop("NewRoleId", UNSET)

        api_user_project_folder_assignment_patch_replace = cls(
            operation_type=operation_type,
            new_role_id=new_role_id,
        )

        api_user_project_folder_assignment_patch_replace.additional_properties = d
        return api_user_project_folder_assignment_patch_replace

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
