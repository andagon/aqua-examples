from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_label_info import ApiLabelInfo


T = TypeVar("T", bound="ApiTestCaseExecutionDefaultsBase")


@attr.s(auto_attribs=True)
class ApiTestCaseExecutionDefaultsBase:
    """
    Attributes:
        value_set_guid (Union[Unset, None, str]): The value set guid.
        tested_version (Union[Unset, None, str]): The tested version.
        labels (Union[Unset, None, List['ApiLabelInfo']]): On creation of a test execution those labels are copied over
            as ApiLabelAttached.
            Version is not checked and can be null.
    """

    value_set_guid: Union[Unset, None, str] = UNSET
    tested_version: Union[Unset, None, str] = UNSET
    labels: Union[Unset, None, List["ApiLabelInfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value_set_guid = self.value_set_guid
        tested_version = self.tested_version
        labels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            if self.labels is None:
                labels = None
            else:
                labels = []
                for labels_item_data in self.labels:
                    labels_item = labels_item_data.to_dict()

                    labels.append(labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value_set_guid is not UNSET:
            field_dict["ValueSetGuid"] = value_set_guid
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if labels is not UNSET:
            field_dict["Labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_label_info import ApiLabelInfo

        d = src_dict.copy()
        value_set_guid = d.pop("ValueSetGuid", UNSET)

        tested_version = d.pop("TestedVersion", UNSET)

        labels = []
        _labels = d.pop("Labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = ApiLabelInfo.from_dict(labels_item_data)

            labels.append(labels_item)

        api_test_case_execution_defaults_base = cls(
            value_set_guid=value_set_guid,
            tested_version=tested_version,
            labels=labels,
        )

        return api_test_case_execution_defaults_base
