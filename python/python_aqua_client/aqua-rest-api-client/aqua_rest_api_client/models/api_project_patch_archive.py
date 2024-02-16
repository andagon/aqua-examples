from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectPatchArchive")


@attr.s(auto_attribs=True)
class ApiProjectPatchArchive:
    """
    Attributes:
        patch_operation (str):
        archived (Union[Unset, bool]): Specifies whether given project should be set archive (true) or non-archived
            (false)
    """

    patch_operation: str
    archived: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_operation = self.patch_operation
        archived = self.archived

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PatchOperation": patch_operation,
            }
        )
        if archived is not UNSET:
            field_dict["Archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_operation = d.pop("PatchOperation")

        archived = d.pop("Archived", UNSET)

        api_project_patch_archive = cls(
            patch_operation=patch_operation,
            archived=archived,
        )

        api_project_patch_archive.additional_properties = d
        return api_project_patch_archive

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
