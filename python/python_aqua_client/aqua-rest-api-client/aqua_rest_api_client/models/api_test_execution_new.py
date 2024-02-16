from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachment_new import ApiAttachmentNew
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_field_value_time_span import ApiFieldValueTimeSpan
    from ..models.api_label_attached import ApiLabelAttached
    from ..models.api_test_execution_new_test_scenario_info import ApiTestExecutionNewTestScenarioInfo
    from ..models.api_test_step_execution_new import ApiTestStepExecutionNew


T = TypeVar("T", bound="ApiTestExecutionNew")


@attr.s(auto_attribs=True)
class ApiTestExecutionNew:
    """A new test execution to be saved.

    Attributes:
        guid (Union[Unset, None, str]): A GUID which uniquely identifies the test
            execution.The GUID can be null. If a GUID
            is provided, it will be kept.
        test_case_id (Union[Unset, int]): The id of the test case to which this execution belongs.
        test_case_name (Union[Unset, None, str]): The name of the executed test case when the execution
            has been started. The name can be defined freely.
        finalize (Union[Unset, bool]): Indicates whether the execution should be finalized. Finalized executions
            cannot be modified any further.
        value_set_name (Union[Unset, None, str]): The name of the value set which was chosen for this
            execution. The value set name can be chosen freely
            here and is not validated against the value sets defined
            in the test case.
        test_scenario_info (Union[Unset, None, ApiTestExecutionNewTestScenarioInfo]): Contains information specific for
            the execution
            in scope of a test scenario.
        steps (Union[Unset, None, List['ApiTestStepExecutionNew']]): Contains the steps of this execution.
        tested_version (Union[Unset, None, str]): The tested version.
        execution_duration (Union[Unset, None, ApiFieldValueTimeSpan]):
        attached_labels (Union[Unset, None, List['ApiLabelAttached']]): Contains labels attached to this execution
        custom_fields (Union[Unset, None, List['ApiFieldUpdate']]): The values which should be set for the custom fields
        attachments (Union[Unset, None, List['ApiAttachmentNew']]): Contains the attachments.
    """

    guid: Union[Unset, None, str] = UNSET
    test_case_id: Union[Unset, int] = UNSET
    test_case_name: Union[Unset, None, str] = UNSET
    finalize: Union[Unset, bool] = UNSET
    value_set_name: Union[Unset, None, str] = UNSET
    test_scenario_info: Union[Unset, None, "ApiTestExecutionNewTestScenarioInfo"] = UNSET
    steps: Union[Unset, None, List["ApiTestStepExecutionNew"]] = UNSET
    tested_version: Union[Unset, None, str] = UNSET
    execution_duration: Union[Unset, None, "ApiFieldValueTimeSpan"] = UNSET
    attached_labels: Union[Unset, None, List["ApiLabelAttached"]] = UNSET
    custom_fields: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET
    attachments: Union[Unset, None, List["ApiAttachmentNew"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        test_case_id = self.test_case_id
        test_case_name = self.test_case_name
        finalize = self.finalize
        value_set_name = self.value_set_name
        test_scenario_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.test_scenario_info, Unset):
            test_scenario_info = self.test_scenario_info.to_dict() if self.test_scenario_info else None

        steps: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            if self.steps is None:
                steps = None
            else:
                steps = []
                for steps_item_data in self.steps:
                    steps_item = steps_item_data.to_dict()

                    steps.append(steps_item)

        tested_version = self.tested_version
        execution_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_duration, Unset):
            execution_duration = self.execution_duration.to_dict() if self.execution_duration else None

        attached_labels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attached_labels, Unset):
            if self.attached_labels is None:
                attached_labels = None
            else:
                attached_labels = []
                for attached_labels_item_data in self.attached_labels:
                    attached_labels_item = attached_labels_item_data.to_dict()

                    attached_labels.append(attached_labels_item)

        custom_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            if self.custom_fields is None:
                custom_fields = None
            else:
                custom_fields = []
                for custom_fields_item_data in self.custom_fields:
                    custom_fields_item = custom_fields_item_data.to_dict()

                    custom_fields.append(custom_fields_item)

        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if test_case_id is not UNSET:
            field_dict["TestCaseId"] = test_case_id
        if test_case_name is not UNSET:
            field_dict["TestCaseName"] = test_case_name
        if finalize is not UNSET:
            field_dict["Finalize"] = finalize
        if value_set_name is not UNSET:
            field_dict["ValueSetName"] = value_set_name
        if test_scenario_info is not UNSET:
            field_dict["TestScenarioInfo"] = test_scenario_info
        if steps is not UNSET:
            field_dict["Steps"] = steps
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if execution_duration is not UNSET:
            field_dict["ExecutionDuration"] = execution_duration
        if attached_labels is not UNSET:
            field_dict["AttachedLabels"] = attached_labels
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachment_new import ApiAttachmentNew
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_field_value_time_span import ApiFieldValueTimeSpan
        from ..models.api_label_attached import ApiLabelAttached
        from ..models.api_test_execution_new_test_scenario_info import ApiTestExecutionNewTestScenarioInfo
        from ..models.api_test_step_execution_new import ApiTestStepExecutionNew

        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        test_case_id = d.pop("TestCaseId", UNSET)

        test_case_name = d.pop("TestCaseName", UNSET)

        finalize = d.pop("Finalize", UNSET)

        value_set_name = d.pop("ValueSetName", UNSET)

        _test_scenario_info = d.pop("TestScenarioInfo", UNSET)
        test_scenario_info: Union[Unset, None, ApiTestExecutionNewTestScenarioInfo]
        if _test_scenario_info is None:
            test_scenario_info = None
        elif isinstance(_test_scenario_info, Unset):
            test_scenario_info = UNSET
        else:
            test_scenario_info = ApiTestExecutionNewTestScenarioInfo.from_dict(_test_scenario_info)

        steps = []
        _steps = d.pop("Steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = ApiTestStepExecutionNew.from_dict(steps_item_data)

            steps.append(steps_item)

        tested_version = d.pop("TestedVersion", UNSET)

        _execution_duration = d.pop("ExecutionDuration", UNSET)
        execution_duration: Union[Unset, None, ApiFieldValueTimeSpan]
        if _execution_duration is None:
            execution_duration = None
        elif isinstance(_execution_duration, Unset):
            execution_duration = UNSET
        else:
            execution_duration = ApiFieldValueTimeSpan.from_dict(_execution_duration)

        attached_labels = []
        _attached_labels = d.pop("AttachedLabels", UNSET)
        for attached_labels_item_data in _attached_labels or []:
            attached_labels_item = ApiLabelAttached.from_dict(attached_labels_item_data)

            attached_labels.append(attached_labels_item)

        custom_fields = []
        _custom_fields = d.pop("CustomFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = ApiFieldUpdate.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        attachments = []
        _attachments = d.pop("Attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = ApiAttachmentNew.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        api_test_execution_new = cls(
            guid=guid,
            test_case_id=test_case_id,
            test_case_name=test_case_name,
            finalize=finalize,
            value_set_name=value_set_name,
            test_scenario_info=test_scenario_info,
            steps=steps,
            tested_version=tested_version,
            execution_duration=execution_duration,
            attached_labels=attached_labels,
            custom_fields=custom_fields,
            attachments=attachments,
        )

        return api_test_execution_new
