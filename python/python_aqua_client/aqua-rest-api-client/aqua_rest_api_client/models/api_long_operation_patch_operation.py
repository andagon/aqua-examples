from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiLongOperationPatchOperation")


@attr.s(auto_attribs=True)
class ApiLongOperationPatchOperation:
    """Represents patch operation that modifies 'long operation'.

    Attributes:
        operation (str):
    """

    operation: str

    def to_dict(self) -> Dict[str, Any]:
        operation = self.operation

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Operation": operation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation = d.pop("Operation")

        api_long_operation_patch_operation = cls(
            operation=operation,
        )

        return api_long_operation_patch_operation
