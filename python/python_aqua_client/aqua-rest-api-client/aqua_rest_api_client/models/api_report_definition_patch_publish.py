from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiReportDefinitionPatchPublish")


@attr.s(auto_attribs=True)
class ApiReportDefinitionPatchPublish:
    """
    Attributes:
        patch_type (str):
    """

    patch_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_type = self.patch_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        api_report_definition_patch_publish = cls(
            patch_type=patch_type,
        )

        api_report_definition_patch_publish.additional_properties = d
        return api_report_definition_patch_publish

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
