from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_label_info import ApiLabelInfo


T = TypeVar("T", bound="ApiTestCaseExecutionPreviewRequest")


@attr.s(auto_attribs=True)
class ApiTestCaseExecutionPreviewRequest:
    """Represents the test case execution preview request.

    Attributes:
        tested_version (Union[Unset, None, str]): Tested version, is only used if test job tested version is not set.
        value_set_guid (Union[Unset, None, str]): The guid of the value set.
        labels (Union[Unset, None, List['ApiLabelInfo']]): Contains labels that will be used for the test jobs created
            by this preview.
            On creation of a test execution those labels are copied over as ApiLabelAttached.
            Version is not checked and can be null.
        custom_fields (Union[Unset, None, List['ApiFieldUpdate']]): Contains the custom fields of this execution
    """

    tested_version: Union[Unset, None, str] = UNSET
    value_set_guid: Union[Unset, None, str] = UNSET
    labels: Union[Unset, None, List["ApiLabelInfo"]] = UNSET
    custom_fields: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tested_version = self.tested_version
        value_set_guid = self.value_set_guid
        labels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            if self.labels is None:
                labels = None
            else:
                labels = []
                for labels_item_data in self.labels:
                    labels_item = labels_item_data.to_dict()

                    labels.append(labels_item)

        custom_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            if self.custom_fields is None:
                custom_fields = None
            else:
                custom_fields = []
                for custom_fields_item_data in self.custom_fields:
                    custom_fields_item = custom_fields_item_data.to_dict()

                    custom_fields.append(custom_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if value_set_guid is not UNSET:
            field_dict["ValueSetGuid"] = value_set_guid
        if labels is not UNSET:
            field_dict["Labels"] = labels
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_label_info import ApiLabelInfo

        d = src_dict.copy()
        tested_version = d.pop("TestedVersion", UNSET)

        value_set_guid = d.pop("ValueSetGuid", UNSET)

        labels = []
        _labels = d.pop("Labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = ApiLabelInfo.from_dict(labels_item_data)

            labels.append(labels_item)

        custom_fields = []
        _custom_fields = d.pop("CustomFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = ApiFieldUpdate.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        api_test_case_execution_preview_request = cls(
            tested_version=tested_version,
            value_set_guid=value_set_guid,
            labels=labels,
            custom_fields=custom_fields,
        )

        return api_test_case_execution_preview_request
