from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiProjectFolderPatchOperation")


@attr.s(auto_attribs=True)
class ApiProjectFolderPatchOperation:
    """Represents data required to execute folder-modify operation.
    There are multiple folder modify operations supported - see ApiProjectFolderPatchOperationType.
    Depending on the type the actual properties can differ. See subclasses for details.

        Attributes:
            operation_type (str):
    """

    operation_type: str

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        api_project_folder_patch_operation = cls(
            operation_type=operation_type,
        )

        return api_project_folder_patch_operation
