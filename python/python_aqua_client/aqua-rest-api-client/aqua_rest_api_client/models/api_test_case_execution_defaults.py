from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_agent_id_and_name import ApiAgentIdAndName
    from ..models.api_edit_layout import ApiEditLayout
    from ..models.api_field_with_value import ApiFieldWithValue
    from ..models.api_label_info import ApiLabelInfo


T = TypeVar("T", bound="ApiTestCaseExecutionDefaults")


@attr.s(auto_attribs=True)
class ApiTestCaseExecutionDefaults:
    """
    Attributes:
        value_set_guid (Union[Unset, None, str]): The value set guid.
        tested_version (Union[Unset, None, str]): The tested version.
        labels (Union[Unset, None, List['ApiLabelInfo']]): On creation of a test execution those labels are copied over
            as ApiLabelAttached.
            Version is not checked and can be null.
        id (Union[Unset, int]): the id of the test case execution default.
        test_case_id (Union[Unset, int]): The id of the test case.
        agent (Union[Unset, None, ApiAgentIdAndName]): Some minimal identifying information for an agent.
        custom_fields (Union[Unset, None, List['ApiFieldWithValue']]): The list of custom fields.
        edit_layout (Union[Unset, None, ApiEditLayout]):
    """

    value_set_guid: Union[Unset, None, str] = UNSET
    tested_version: Union[Unset, None, str] = UNSET
    labels: Union[Unset, None, List["ApiLabelInfo"]] = UNSET
    id: Union[Unset, int] = UNSET
    test_case_id: Union[Unset, int] = UNSET
    agent: Union[Unset, None, "ApiAgentIdAndName"] = UNSET
    custom_fields: Union[Unset, None, List["ApiFieldWithValue"]] = UNSET
    edit_layout: Union[Unset, None, "ApiEditLayout"] = UNSET
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

        id = self.id
        test_case_id = self.test_case_id
        agent: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.agent, Unset):
            agent = self.agent.to_dict() if self.agent else None

        custom_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            if self.custom_fields is None:
                custom_fields = None
            else:
                custom_fields = []
                for custom_fields_item_data in self.custom_fields:
                    custom_fields_item = custom_fields_item_data.to_dict()

                    custom_fields.append(custom_fields_item)

        edit_layout: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_layout, Unset):
            edit_layout = self.edit_layout.to_dict() if self.edit_layout else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_set_guid is not UNSET:
            field_dict["ValueSetGuid"] = value_set_guid
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if labels is not UNSET:
            field_dict["Labels"] = labels
        if id is not UNSET:
            field_dict["Id"] = id
        if test_case_id is not UNSET:
            field_dict["TestCaseId"] = test_case_id
        if agent is not UNSET:
            field_dict["Agent"] = agent
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields
        if edit_layout is not UNSET:
            field_dict["EditLayout"] = edit_layout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_agent_id_and_name import ApiAgentIdAndName
        from ..models.api_edit_layout import ApiEditLayout
        from ..models.api_field_with_value import ApiFieldWithValue
        from ..models.api_label_info import ApiLabelInfo

        d = src_dict.copy()
        value_set_guid = d.pop("ValueSetGuid", UNSET)

        tested_version = d.pop("TestedVersion", UNSET)

        labels = []
        _labels = d.pop("Labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = ApiLabelInfo.from_dict(labels_item_data)

            labels.append(labels_item)

        id = d.pop("Id", UNSET)

        test_case_id = d.pop("TestCaseId", UNSET)

        _agent = d.pop("Agent", UNSET)
        agent: Union[Unset, None, ApiAgentIdAndName]
        if _agent is None:
            agent = None
        elif isinstance(_agent, Unset):
            agent = UNSET
        else:
            agent = ApiAgentIdAndName.from_dict(_agent)

        custom_fields = []
        _custom_fields = d.pop("CustomFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = ApiFieldWithValue.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        _edit_layout = d.pop("EditLayout", UNSET)
        edit_layout: Union[Unset, None, ApiEditLayout]
        if _edit_layout is None:
            edit_layout = None
        elif isinstance(_edit_layout, Unset):
            edit_layout = UNSET
        else:
            edit_layout = ApiEditLayout.from_dict(_edit_layout)

        api_test_case_execution_defaults = cls(
            value_set_guid=value_set_guid,
            tested_version=tested_version,
            labels=labels,
            id=id,
            test_case_id=test_case_id,
            agent=agent,
            custom_fields=custom_fields,
            edit_layout=edit_layout,
        )

        api_test_case_execution_defaults.additional_properties = d
        return api_test_case_execution_defaults

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
