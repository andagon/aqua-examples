from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiReportDefinitionPatchCollectionResponse")


@attr.s(auto_attribs=True)
class ApiReportDefinitionPatchCollectionResponse:
    """Represent the response for the report definition patch collection operation."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        api_report_definition_patch_collection_response = cls()

        return api_report_definition_patch_collection_response
