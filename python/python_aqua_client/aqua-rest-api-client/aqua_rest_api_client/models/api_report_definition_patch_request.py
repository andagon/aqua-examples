from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiReportDefinitionPatchRequest")


@attr.s(auto_attribs=True)
class ApiReportDefinitionPatchRequest:
    """Represents the patch request for report definition.

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

        api_report_definition_patch_request = cls(
            patch_type=patch_type,
        )

        return api_report_definition_patch_request
