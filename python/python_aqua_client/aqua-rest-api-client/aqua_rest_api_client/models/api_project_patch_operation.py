from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiProjectPatchOperation")


@attr.s(auto_attribs=True)
class ApiProjectPatchOperation:
    """Represents data required to execute project-modify operation.
    There are multiple project modify operations supported - see ApiProjectPatchTypes.
    Depending on the type the actual properties can differ. See subclasses for details.

        Attributes:
            patch_operation (str):
    """

    patch_operation: str

    def to_dict(self) -> Dict[str, Any]:
        patch_operation = self.patch_operation

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "PatchOperation": patch_operation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_operation = d.pop("PatchOperation")

        api_project_patch_operation = cls(
            patch_operation=patch_operation,
        )

        return api_project_patch_operation
