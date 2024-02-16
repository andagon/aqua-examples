from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_label_info import ApiLabelInfo


T = TypeVar("T", bound="ApiTestCaseExecutionDefaultsUpdate")


@attr.s(auto_attribs=True)
class ApiTestCaseExecutionDefaultsUpdate:
    """
    Attributes:
        value_set_guid (Union[Unset, None, str]): The value set guid.
        tested_version (Union[Unset, None, str]): The tested version.
        labels (Union[Unset, None, List['ApiLabelInfo']]): On creation of a test execution those labels are copied over
            as ApiLabelAttached.
            Version is not checked and can be null.
        agent_id (Union[Unset, None, int]): The agent id (or null, if saving executions for non-automated test case).
        custom_fields (Union[Unset, None, List['ApiFieldUpdate']]): The list of custom fields.
    """

    value_set_guid: Union[Unset, None, str] = UNSET
    tested_version: Union[Unset, None, str] = UNSET
    labels: Union[Unset, None, List["ApiLabelInfo"]] = UNSET
    agent_id: Union[Unset, None, int] = UNSET
    custom_fields: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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

        agent_id = self.agent_id
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
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_set_guid is not UNSET:
            field_dict["ValueSetGuid"] = value_set_guid
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if labels is not UNSET:
            field_dict["Labels"] = labels
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_label_info import ApiLabelInfo

        d = src_dict.copy()
        value_set_guid = d.pop("ValueSetGuid", UNSET)

        tested_version = d.pop("TestedVersion", UNSET)

        labels = []
        _labels = d.pop("Labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = ApiLabelInfo.from_dict(labels_item_data)

            labels.append(labels_item)

        agent_id = d.pop("AgentId", UNSET)

        custom_fields = []
        _custom_fields = d.pop("CustomFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = ApiFieldUpdate.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        api_test_case_execution_defaults_update = cls(
            value_set_guid=value_set_guid,
            tested_version=tested_version,
            labels=labels,
            agent_id=agent_id,
            custom_fields=custom_fields,
        )

        api_test_case_execution_defaults_update.additional_properties = d
        return api_test_case_execution_defaults_update

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
