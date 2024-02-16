from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.object_type import ObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemExportRequest")


@attr.s(auto_attribs=True)
class ApiItemExportRequest:
    """Request for exporting files

    Attributes:
        object_types (Union[Unset, None, List[ObjectType]]): The objectTypes to export
            If an objecttype is specified, all items of that objecttype in the folder are exported,
            the respective id list for that objecttype is then ignored in this case.
        requirement_ids (Union[Unset, None, List[int]]): Ids of requirements to be exported
        defect_ids (Union[Unset, None, List[int]]): Ids of defect to be exported
        test_case_ids (Union[Unset, None, List[int]]): Ids of testcases to be exported
        test_scenario_ids (Union[Unset, None, List[int]]): Ids of testscenarios to be exported
        recursive (Union[Unset, bool]): Export everything from subfolders
        include_invisible_fields (Union[Unset, bool]): Export fields not visible on layout
        include_attachments (Union[Unset, bool]): Export the Attachments
        include_rtf_files (Union[Unset, bool]): Export the rtf to external files
    """

    object_types: Union[Unset, None, List[ObjectType]] = UNSET
    requirement_ids: Union[Unset, None, List[int]] = UNSET
    defect_ids: Union[Unset, None, List[int]] = UNSET
    test_case_ids: Union[Unset, None, List[int]] = UNSET
    test_scenario_ids: Union[Unset, None, List[int]] = UNSET
    recursive: Union[Unset, bool] = UNSET
    include_invisible_fields: Union[Unset, bool] = UNSET
    include_attachments: Union[Unset, bool] = UNSET
    include_rtf_files: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        object_types: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.object_types, Unset):
            if self.object_types is None:
                object_types = None
            else:
                object_types = []
                for object_types_item_data in self.object_types:
                    object_types_item = object_types_item_data.value

                    object_types.append(object_types_item)

        requirement_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.requirement_ids, Unset):
            if self.requirement_ids is None:
                requirement_ids = None
            else:
                requirement_ids = self.requirement_ids

        defect_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.defect_ids, Unset):
            if self.defect_ids is None:
                defect_ids = None
            else:
                defect_ids = self.defect_ids

        test_case_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.test_case_ids, Unset):
            if self.test_case_ids is None:
                test_case_ids = None
            else:
                test_case_ids = self.test_case_ids

        test_scenario_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.test_scenario_ids, Unset):
            if self.test_scenario_ids is None:
                test_scenario_ids = None
            else:
                test_scenario_ids = self.test_scenario_ids

        recursive = self.recursive
        include_invisible_fields = self.include_invisible_fields
        include_attachments = self.include_attachments
        include_rtf_files = self.include_rtf_files

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if object_types is not UNSET:
            field_dict["objectTypes"] = object_types
        if requirement_ids is not UNSET:
            field_dict["RequirementIds"] = requirement_ids
        if defect_ids is not UNSET:
            field_dict["DefectIds"] = defect_ids
        if test_case_ids is not UNSET:
            field_dict["TestCaseIds"] = test_case_ids
        if test_scenario_ids is not UNSET:
            field_dict["TestScenarioIds"] = test_scenario_ids
        if recursive is not UNSET:
            field_dict["recursive"] = recursive
        if include_invisible_fields is not UNSET:
            field_dict["includeInvisibleFields"] = include_invisible_fields
        if include_attachments is not UNSET:
            field_dict["includeAttachments"] = include_attachments
        if include_rtf_files is not UNSET:
            field_dict["includeRtfFiles"] = include_rtf_files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_types = []
        _object_types = d.pop("objectTypes", UNSET)
        for object_types_item_data in _object_types or []:
            object_types_item = ObjectType(object_types_item_data)

            object_types.append(object_types_item)

        requirement_ids = cast(List[int], d.pop("RequirementIds", UNSET))

        defect_ids = cast(List[int], d.pop("DefectIds", UNSET))

        test_case_ids = cast(List[int], d.pop("TestCaseIds", UNSET))

        test_scenario_ids = cast(List[int], d.pop("TestScenarioIds", UNSET))

        recursive = d.pop("recursive", UNSET)

        include_invisible_fields = d.pop("includeInvisibleFields", UNSET)

        include_attachments = d.pop("includeAttachments", UNSET)

        include_rtf_files = d.pop("includeRtfFiles", UNSET)

        api_item_export_request = cls(
            object_types=object_types,
            requirement_ids=requirement_ids,
            defect_ids=defect_ids,
            test_case_ids=test_case_ids,
            test_scenario_ids=test_scenario_ids,
            recursive=recursive,
            include_invisible_fields=include_invisible_fields,
            include_attachments=include_attachments,
            include_rtf_files=include_rtf_files,
        )

        return api_item_export_request
