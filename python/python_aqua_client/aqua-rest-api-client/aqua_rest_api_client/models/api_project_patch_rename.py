from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectPatchRename")


@attr.s(auto_attribs=True)
class ApiProjectPatchRename:
    """
    Attributes:
        patch_operation (str):
        new_name (Union[Unset, None, str]): New name of the project being updated.
    """

    patch_operation: str
    new_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_operation = self.patch_operation
        new_name = self.new_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PatchOperation": patch_operation,
            }
        )
        if new_name is not UNSET:
            field_dict["NewName"] = new_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_operation = d.pop("PatchOperation")

        new_name = d.pop("NewName", UNSET)

        api_project_patch_rename = cls(
            patch_operation=patch_operation,
            new_name=new_name,
        )

        api_project_patch_rename.additional_properties = d
        return api_project_patch_rename

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
