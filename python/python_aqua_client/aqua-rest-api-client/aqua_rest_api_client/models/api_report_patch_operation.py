from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiReportPatchOperation")


@attr.s(auto_attribs=True)
class ApiReportPatchOperation:
    """Represent the report definition patch request.

    Attributes:
        patch_type (str):
    """

    patch_type: str

    def to_dict(self) -> Dict[str, Any]:
        patch_type = self.patch_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "PatchType": patch_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_type = d.pop("PatchType")

        api_report_patch_operation = cls(
            patch_type=patch_type,
        )

        return api_report_patch_operation
