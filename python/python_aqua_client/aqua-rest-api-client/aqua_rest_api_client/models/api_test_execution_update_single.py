from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachments import ApiAttachments
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_field_value_time_span import ApiFieldValueTimeSpan
    from ..models.api_label_attached import ApiLabelAttached
    from ..models.api_test_step_execution_update import ApiTestStepExecutionUpdate


T = TypeVar("T", bound="ApiTestExecutionUpdateSingle")


@attr.s(auto_attribs=True)
class ApiTestExecutionUpdateSingle:
    """A test execution to be updated.

    Attributes:
        attachments (Union[Unset, None, ApiAttachments]): Contains all changes to the attachments of an item.
        steps (Union[Unset, None, List['ApiTestStepExecutionUpdate']]): Contains the steps of this execution.
        tested_version (Union[Unset, None, str]): Tested version
        attached_labels (Union[Unset, None, List['ApiLabelAttached']]): Contains labels attached to this execution
        execution_duration (Union[Unset, None, ApiFieldValueTimeSpan]):
        custom_fields (Union[Unset, None, List['ApiFieldUpdate']]): The values which should be set for the custom fields
    """

    attachments: Union[Unset, None, "ApiAttachments"] = UNSET
    steps: Union[Unset, None, List["ApiTestStepExecutionUpdate"]] = UNSET
    tested_version: Union[Unset, None, str] = UNSET
    attached_labels: Union[Unset, None, List["ApiLabelAttached"]] = UNSET
    execution_duration: Union[Unset, None, "ApiFieldValueTimeSpan"] = UNSET
    custom_fields: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        attachments: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict() if self.attachments else None

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
        attached_labels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attached_labels, Unset):
            if self.attached_labels is None:
                attached_labels = None
            else:
                attached_labels = []
                for attached_labels_item_data in self.attached_labels:
                    attached_labels_item = attached_labels_item_data.to_dict()

                    attached_labels.append(attached_labels_item)

        execution_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_duration, Unset):
            execution_duration = self.execution_duration.to_dict() if self.execution_duration else None

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
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments
        if steps is not UNSET:
            field_dict["Steps"] = steps
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if attached_labels is not UNSET:
            field_dict["AttachedLabels"] = attached_labels
        if execution_duration is not UNSET:
            field_dict["ExecutionDuration"] = execution_duration
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachments import ApiAttachments
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_field_value_time_span import ApiFieldValueTimeSpan
        from ..models.api_label_attached import ApiLabelAttached
        from ..models.api_test_step_execution_update import ApiTestStepExecutionUpdate

        d = src_dict.copy()
        _attachments = d.pop("Attachments", UNSET)
        attachments: Union[Unset, None, ApiAttachments]
        if _attachments is None:
            attachments = None
        elif isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = ApiAttachments.from_dict(_attachments)

        steps = []
        _steps = d.pop("Steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = ApiTestStepExecutionUpdate.from_dict(steps_item_data)

            steps.append(steps_item)

        tested_version = d.pop("TestedVersion", UNSET)

        attached_labels = []
        _attached_labels = d.pop("AttachedLabels", UNSET)
        for attached_labels_item_data in _attached_labels or []:
            attached_labels_item = ApiLabelAttached.from_dict(attached_labels_item_data)

            attached_labels.append(attached_labels_item)

        _execution_duration = d.pop("ExecutionDuration", UNSET)
        execution_duration: Union[Unset, None, ApiFieldValueTimeSpan]
        if _execution_duration is None:
            execution_duration = None
        elif isinstance(_execution_duration, Unset):
            execution_duration = UNSET
        else:
            execution_duration = ApiFieldValueTimeSpan.from_dict(_execution_duration)

        custom_fields = []
        _custom_fields = d.pop("CustomFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = ApiFieldUpdate.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        api_test_execution_update_single = cls(
            attachments=attachments,
            steps=steps,
            tested_version=tested_version,
            attached_labels=attached_labels,
            execution_duration=execution_duration,
            custom_fields=custom_fields,
        )

        return api_test_execution_update_single
