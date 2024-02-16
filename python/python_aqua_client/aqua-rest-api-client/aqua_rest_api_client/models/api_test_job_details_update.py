from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_label_info import ApiLabelInfo


T = TypeVar("T", bound="ApiTestJobDetailsUpdate")


@attr.s(auto_attribs=True)
class ApiTestJobDetailsUpdate:
    """Contains the details of the test job which should be updated.

    Attributes:
        agent_to_use (Union[Unset, None, int]): Id of the agent which should be used. Can be null.
        value_set_guid (Union[Unset, None, str]): Guid of the value set guid which should be used.
            Can be null but only if the test case is not
            parameterized.
        tested_version (Union[Unset, None, str]): The tested version. Can be null.
        labels (Union[Unset, None, List['ApiLabelInfo']]): Contains labels attached to this test job.
            On creation of a test execution those labels are copied over as ApiLabelAttached.
            Version is not checked and can be null.
        custom_fields (Union[Unset, None, List['ApiFieldUpdate']]): Contains the updates which should be applied to the
            execution custom fields of this test job.
        tester_id (Union[Unset, None, int]): Contains the tester user id.
    """

    agent_to_use: Union[Unset, None, int] = UNSET
    value_set_guid: Union[Unset, None, str] = UNSET
    tested_version: Union[Unset, None, str] = UNSET
    labels: Union[Unset, None, List["ApiLabelInfo"]] = UNSET
    custom_fields: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET
    tester_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_to_use = self.agent_to_use
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

        custom_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            if self.custom_fields is None:
                custom_fields = None
            else:
                custom_fields = []
                for custom_fields_item_data in self.custom_fields:
                    custom_fields_item = custom_fields_item_data.to_dict()

                    custom_fields.append(custom_fields_item)

        tester_id = self.tester_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agent_to_use is not UNSET:
            field_dict["AgentToUse"] = agent_to_use
        if value_set_guid is not UNSET:
            field_dict["ValueSetGuid"] = value_set_guid
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if labels is not UNSET:
            field_dict["Labels"] = labels
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields
        if tester_id is not UNSET:
            field_dict["TesterId"] = tester_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_label_info import ApiLabelInfo

        d = src_dict.copy()
        agent_to_use = d.pop("AgentToUse", UNSET)

        value_set_guid = d.pop("ValueSetGuid", UNSET)

        tested_version = d.pop("TestedVersion", UNSET)

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

        tester_id = d.pop("TesterId", UNSET)

        api_test_job_details_update = cls(
            agent_to_use=agent_to_use,
            value_set_guid=value_set_guid,
            tested_version=tested_version,
            labels=labels,
            custom_fields=custom_fields,
            tester_id=tester_id,
        )

        return api_test_job_details_update
