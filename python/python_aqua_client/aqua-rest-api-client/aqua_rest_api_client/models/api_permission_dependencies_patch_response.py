from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiPermissionDependenciesPatchResponse")


@attr.s(auto_attribs=True)
class ApiPermissionDependenciesPatchResponse:
    """Represent a response to validate permission dependencies.
    Actual subclasses are used, depending on OperationType.

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

        api_permission_dependencies_patch_response = cls(
            operation_type=operation_type,
        )

        return api_permission_dependencies_patch_response
