from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_label_attached import ApiLabelAttached


T = TypeVar("T", bound="ApiAutomatedTestCaseExecution")


@attr.s(auto_attribs=True)
class ApiAutomatedTestCaseExecution:
    """
    Attributes:
        value_set_key (Union[Unset, None, str]): Contains the id of the value set key.
        tested_version (Union[Unset, None, str]): Contains the information about the test version.
        agent_id (Union[Unset, int]): Contains the id of the agent.
        labels (Union[Unset, None, List['ApiLabelAttached']]): Contains labels that will be used for the test jobs
            created by this preview.
            On creation of a test execution those labels are copied over as ApiLabelAttached.
            Version is not checked and can be null.
        custom_fields (Union[Unset, None, List['ApiFieldUpdate']]): The values which should be set for the custom
            fields.
    """

    value_set_key: Union[Unset, None, str] = UNSET
    tested_version: Union[Unset, None, str] = UNSET
    agent_id: Union[Unset, int] = UNSET
    labels: Union[Unset, None, List["ApiLabelAttached"]] = UNSET
    custom_fields: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value_set_key = self.value_set_key
        tested_version = self.tested_version
        agent_id = self.agent_id
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
        if value_set_key is not UNSET:
            field_dict["ValueSetKey"] = value_set_key
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if labels is not UNSET:
            field_dict["Labels"] = labels
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_label_attached import ApiLabelAttached

        d = src_dict.copy()
        value_set_key = d.pop("ValueSetKey", UNSET)

        tested_version = d.pop("TestedVersion", UNSET)

        agent_id = d.pop("AgentId", UNSET)

        labels = []
        _labels = d.pop("Labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = ApiLabelAttached.from_dict(labels_item_data)

            labels.append(labels_item)

        custom_fields = []
        _custom_fields = d.pop("CustomFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = ApiFieldUpdate.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        api_automated_test_case_execution = cls(
            value_set_key=value_set_key,
            tested_version=tested_version,
            agent_id=agent_id,
            labels=labels,
            custom_fields=custom_fields,
        )

        return api_automated_test_case_execution
