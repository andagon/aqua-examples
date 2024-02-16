from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportDefinitionPatchCopyCollectionOperation")


@attr.s(auto_attribs=True)
class ApiReportDefinitionPatchCopyCollectionOperation:
    """
    Attributes:
        patch_operation (str):
        report_definition_id (Union[Unset, int]): The id of the report definition.
        target_project_id (Union[Unset, int]): The id of the target project.
        new_name (Union[Unset, None, str]): The new name for the report definition, if empty the old name will be kept.
    """

    patch_operation: str
    report_definition_id: Union[Unset, int] = UNSET
    target_project_id: Union[Unset, int] = UNSET
    new_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_operation = self.patch_operation
        report_definition_id = self.report_definition_id
        target_project_id = self.target_project_id
        new_name = self.new_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PatchOperation": patch_operation,
            }
        )
        if report_definition_id is not UNSET:
            field_dict["ReportDefinitionId"] = report_definition_id
        if target_project_id is not UNSET:
            field_dict["TargetProjectId"] = target_project_id
        if new_name is not UNSET:
            field_dict["NewName"] = new_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_operation = d.pop("PatchOperation")

        report_definition_id = d.pop("ReportDefinitionId", UNSET)

        target_project_id = d.pop("TargetProjectId", UNSET)

        new_name = d.pop("NewName", UNSET)

        api_report_definition_patch_copy_collection_operation = cls(
            patch_operation=patch_operation,
            report_definition_id=report_definition_id,
            target_project_id=target_project_id,
            new_name=new_name,
        )

        api_report_definition_patch_copy_collection_operation.additional_properties = d
        return api_report_definition_patch_copy_collection_operation

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
