from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectFolderFavouritePatchRename")


@attr.s(auto_attribs=True)
class ApiProjectFolderFavouritePatchRename:
    """
    Attributes:
        patch_operation (str):
        label (Union[Unset, None, str]): Custom label of the favorite.
    """

    patch_operation: str
    label: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_operation = self.patch_operation
        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PatchOperation": patch_operation,
            }
        )
        if label is not UNSET:
            field_dict["Label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_operation = d.pop("PatchOperation")

        label = d.pop("Label", UNSET)

        api_project_folder_favourite_patch_rename = cls(
            patch_operation=patch_operation,
            label=label,
        )

        api_project_folder_favourite_patch_rename.additional_properties = d
        return api_project_folder_favourite_patch_rename

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
