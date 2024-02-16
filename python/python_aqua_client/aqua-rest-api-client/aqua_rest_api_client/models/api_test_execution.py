from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_test_execution_status import ApiTestExecutionStatus
from ..models.api_test_execution_type import ApiTestExecutionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachment_info import ApiAttachmentInfo
    from ..models.api_edit_layout import ApiEditLayout
    from ..models.api_editable_info import ApiEditableInfo
    from ..models.api_field_value_date_time import ApiFieldValueDateTime
    from ..models.api_field_value_time_span import ApiFieldValueTimeSpan
    from ..models.api_field_value_user import ApiFieldValueUser
    from ..models.api_field_with_value import ApiFieldWithValue
    from ..models.api_item import ApiItem
    from ..models.api_item_location import ApiItemLocation
    from ..models.api_label_attached import ApiLabelAttached
    from ..models.api_test_execution_data_attribute import ApiTestExecutionDataAttribute
    from ..models.api_test_execution_log import ApiTestExecutionLog
    from ..models.api_test_execution_permission import ApiTestExecutionPermission
    from ..models.api_test_execution_test_scenario_info import ApiTestExecutionTestScenarioInfo
    from ..models.api_test_step_execution import ApiTestStepExecution


T = TypeVar("T", bound="ApiTestExecution")


@attr.s(auto_attribs=True)
class ApiTestExecution:
    """
    Attributes:
        id (Union[Unset, int]): Id of the execution.
        formatted_id (Union[Unset, None, str]): The formatted id of the execution.
        guid (Union[Unset, None, str]): Guid of the execution.
        test_execution_type (Union[Unset, ApiTestExecutionType]): Identifies the type of an execution.
            This enum has the following values:
              - `Automated` Represents automated execution.
              - `Manual` Represents manual execution.
        test_case_id (Union[Unset, int]): Id of the test case the execution is related to.
        test_case_name (Union[Unset, None, str]): Name of the test case the execution is related to.
        test_case_formatted_id (Union[Unset, None, str]): Formatted name of the test case the execution is related to.
        last_editor (Union[Unset, None, ApiFieldValueUser]):
        tester (Union[Unset, None, ApiFieldValueUser]):
        execution_date (Union[Unset, None, ApiFieldValueDateTime]):
        last_modified (Union[Unset, None, ApiFieldValueDateTime]):
        execution_duration (Union[Unset, None, ApiFieldValueTimeSpan]):
        status (Union[Unset, ApiTestExecutionStatus]): Identifies the status of an execution.
            This enum has the following values:
              - `Aborted` Execution has been aborted.
              - `Blocked` At least one executed step was blocked, and there were no failures (only considered for manual
            tests)
              - `Failed` At least one executed step marked as failed.
              - `Incomplete` Some steps executed, but at least one step was not executed (and no failures or blocked yet).
              - `InProgress` Execution is in progress.
              - `NotApplicable` All steps were not applicable to the execution
              - `NotRun` No steps executed yet.
              - `Pass` All steps executed and passed.
              - `Queued` The step is queued for automated execution.
              - `Waiting` An execution was started and a step is waiting for pickup by agent
        value_set_name (Union[Unset, None, str]): Name of the value set used (or none)
        version (Union[Unset, int]): Version
        tested_version (Union[Unset, None, str]): Tested version
        irrelevant_flagged_by (Union[Unset, None, ApiFieldValueUser]):
        irrelevant_flagged_at (Union[Unset, None, ApiFieldValueDateTime]):
        irrelevant_reason (Union[Unset, None, str]): Reason why execution has been marked as irrelevant (if was)
        irrelevant (Union[Unset, bool]): True if execution has been marked as irrelevent.
        agent_to_use (Union[Unset, None, str]): Agents selected for this execution. Can be a pool (especially if
            execution consists of mixuture of different steps)
        is_finalized (Union[Unset, bool]): True if execution is finalized.
        has_attachment (Union[Unset, bool]): True if execution has any attachments.
        has_defect (Union[Unset, bool]): True if execution has any defetcs related.
        test_scenario_info (Union[Unset, None, ApiTestExecutionTestScenarioInfo]): Contains information specific for the
            execution
            in scope of a test scenario.
        attached_labels (Union[Unset, None, List['ApiLabelAttached']]): Contains labels attached to this execution
        custom_fields (Union[Unset, None, List['ApiFieldWithValue']]): Contains the custom fields of this execution
        history_test_case (Union[Unset, None, ApiItem]):
        steps (Union[Unset, None, List['ApiTestStepExecution']]): Contains execution steps.
        attached_files (Union[Unset, None, List['ApiAttachmentInfo']]): List of files attached to this execution.
        edit_layout (Union[Unset, None, ApiEditLayout]):
        location (Union[Unset, None, ApiItemLocation]): Specifies the location (project and folder) of an item
        execution_logs (Union[Unset, None, List['ApiTestExecutionLog']]): Contains execution logs (only for automated
            executions)
        execution_data_attributes (Union[Unset, None, List['ApiTestExecutionDataAttribute']]): Contains execution data
            attributes (only for automated executions)
        permissions (Union[Unset, None, ApiTestExecutionPermission]): Represents permissions of an test execution.
            Intended to be subclassed
            by classes with more fine-grained permission set for given context.
        require_actual_result (Union[Unset, bool]): If true, then 'Actual Results' field is mandatory when manually
            executing.
        edit_status (Union[Unset, None, ApiEditableInfo]): Contains information about editable status of an item.
    """

    id: Union[Unset, int] = UNSET
    formatted_id: Union[Unset, None, str] = UNSET
    guid: Union[Unset, None, str] = UNSET
    test_execution_type: Union[Unset, ApiTestExecutionType] = UNSET
    test_case_id: Union[Unset, int] = UNSET
    test_case_name: Union[Unset, None, str] = UNSET
    test_case_formatted_id: Union[Unset, None, str] = UNSET
    last_editor: Union[Unset, None, "ApiFieldValueUser"] = UNSET
    tester: Union[Unset, None, "ApiFieldValueUser"] = UNSET
    execution_date: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    last_modified: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    execution_duration: Union[Unset, None, "ApiFieldValueTimeSpan"] = UNSET
    status: Union[Unset, ApiTestExecutionStatus] = UNSET
    value_set_name: Union[Unset, None, str] = UNSET
    version: Union[Unset, int] = UNSET
    tested_version: Union[Unset, None, str] = UNSET
    irrelevant_flagged_by: Union[Unset, None, "ApiFieldValueUser"] = UNSET
    irrelevant_flagged_at: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    irrelevant_reason: Union[Unset, None, str] = UNSET
    irrelevant: Union[Unset, bool] = UNSET
    agent_to_use: Union[Unset, None, str] = UNSET
    is_finalized: Union[Unset, bool] = UNSET
    has_attachment: Union[Unset, bool] = UNSET
    has_defect: Union[Unset, bool] = UNSET
    test_scenario_info: Union[Unset, None, "ApiTestExecutionTestScenarioInfo"] = UNSET
    attached_labels: Union[Unset, None, List["ApiLabelAttached"]] = UNSET
    custom_fields: Union[Unset, None, List["ApiFieldWithValue"]] = UNSET
    history_test_case: Union[Unset, None, "ApiItem"] = UNSET
    steps: Union[Unset, None, List["ApiTestStepExecution"]] = UNSET
    attached_files: Union[Unset, None, List["ApiAttachmentInfo"]] = UNSET
    edit_layout: Union[Unset, None, "ApiEditLayout"] = UNSET
    location: Union[Unset, None, "ApiItemLocation"] = UNSET
    execution_logs: Union[Unset, None, List["ApiTestExecutionLog"]] = UNSET
    execution_data_attributes: Union[Unset, None, List["ApiTestExecutionDataAttribute"]] = UNSET
    permissions: Union[Unset, None, "ApiTestExecutionPermission"] = UNSET
    require_actual_result: Union[Unset, bool] = UNSET
    edit_status: Union[Unset, None, "ApiEditableInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        formatted_id = self.formatted_id
        guid = self.guid
        test_execution_type: Union[Unset, str] = UNSET
        if not isinstance(self.test_execution_type, Unset):
            test_execution_type = self.test_execution_type.value

        test_case_id = self.test_case_id
        test_case_name = self.test_case_name
        test_case_formatted_id = self.test_case_formatted_id
        last_editor: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_editor, Unset):
            last_editor = self.last_editor.to_dict() if self.last_editor else None

        tester: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.tester, Unset):
            tester = self.tester.to_dict() if self.tester else None

        execution_date: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_date, Unset):
            execution_date = self.execution_date.to_dict() if self.execution_date else None

        last_modified: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.to_dict() if self.last_modified else None

        execution_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_duration, Unset):
            execution_duration = self.execution_duration.to_dict() if self.execution_duration else None

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        value_set_name = self.value_set_name
        version = self.version
        tested_version = self.tested_version
        irrelevant_flagged_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.irrelevant_flagged_by, Unset):
            irrelevant_flagged_by = self.irrelevant_flagged_by.to_dict() if self.irrelevant_flagged_by else None

        irrelevant_flagged_at: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.irrelevant_flagged_at, Unset):
            irrelevant_flagged_at = self.irrelevant_flagged_at.to_dict() if self.irrelevant_flagged_at else None

        irrelevant_reason = self.irrelevant_reason
        irrelevant = self.irrelevant
        agent_to_use = self.agent_to_use
        is_finalized = self.is_finalized
        has_attachment = self.has_attachment
        has_defect = self.has_defect
        test_scenario_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.test_scenario_info, Unset):
            test_scenario_info = self.test_scenario_info.to_dict() if self.test_scenario_info else None

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

        history_test_case: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.history_test_case, Unset):
            history_test_case = self.history_test_case.to_dict() if self.history_test_case else None

        steps: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            if self.steps is None:
                steps = None
            else:
                steps = []
                for steps_item_data in self.steps:
                    steps_item = steps_item_data.to_dict()

                    steps.append(steps_item)

        attached_files: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attached_files, Unset):
            if self.attached_files is None:
                attached_files = None
            else:
                attached_files = []
                for attached_files_item_data in self.attached_files:
                    attached_files_item = attached_files_item_data.to_dict()

                    attached_files.append(attached_files_item)

        edit_layout: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_layout, Unset):
            edit_layout = self.edit_layout.to_dict() if self.edit_layout else None

        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        execution_logs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.execution_logs, Unset):
            if self.execution_logs is None:
                execution_logs = None
            else:
                execution_logs = []
                for execution_logs_item_data in self.execution_logs:
                    execution_logs_item = execution_logs_item_data.to_dict()

                    execution_logs.append(execution_logs_item)

        execution_data_attributes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.execution_data_attributes, Unset):
            if self.execution_data_attributes is None:
                execution_data_attributes = None
            else:
                execution_data_attributes = []
                for execution_data_attributes_item_data in self.execution_data_attributes:
                    execution_data_attributes_item = execution_data_attributes_item_data.to_dict()

                    execution_data_attributes.append(execution_data_attributes_item)

        permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict() if self.permissions else None

        require_actual_result = self.require_actual_result
        edit_status: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_status, Unset):
            edit_status = self.edit_status.to_dict() if self.edit_status else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if formatted_id is not UNSET:
            field_dict["FormattedId"] = formatted_id
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if test_execution_type is not UNSET:
            field_dict["TestExecutionType"] = test_execution_type
        if test_case_id is not UNSET:
            field_dict["TestCaseId"] = test_case_id
        if test_case_name is not UNSET:
            field_dict["TestCaseName"] = test_case_name
        if test_case_formatted_id is not UNSET:
            field_dict["TestCaseFormattedId"] = test_case_formatted_id
        if last_editor is not UNSET:
            field_dict["LastEditor"] = last_editor
        if tester is not UNSET:
            field_dict["Tester"] = tester
        if execution_date is not UNSET:
            field_dict["ExecutionDate"] = execution_date
        if last_modified is not UNSET:
            field_dict["LastModified"] = last_modified
        if execution_duration is not UNSET:
            field_dict["ExecutionDuration"] = execution_duration
        if status is not UNSET:
            field_dict["Status"] = status
        if value_set_name is not UNSET:
            field_dict["ValueSetName"] = value_set_name
        if version is not UNSET:
            field_dict["Version"] = version
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if irrelevant_flagged_by is not UNSET:
            field_dict["IrrelevantFlaggedBy"] = irrelevant_flagged_by
        if irrelevant_flagged_at is not UNSET:
            field_dict["IrrelevantFlaggedAt"] = irrelevant_flagged_at
        if irrelevant_reason is not UNSET:
            field_dict["IrrelevantReason"] = irrelevant_reason
        if irrelevant is not UNSET:
            field_dict["Irrelevant"] = irrelevant
        if agent_to_use is not UNSET:
            field_dict["AgentToUse"] = agent_to_use
        if is_finalized is not UNSET:
            field_dict["IsFinalized"] = is_finalized
        if has_attachment is not UNSET:
            field_dict["HasAttachment"] = has_attachment
        if has_defect is not UNSET:
            field_dict["HasDefect"] = has_defect
        if test_scenario_info is not UNSET:
            field_dict["TestScenarioInfo"] = test_scenario_info
        if attached_labels is not UNSET:
            field_dict["AttachedLabels"] = attached_labels
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields
        if history_test_case is not UNSET:
            field_dict["HistoryTestCase"] = history_test_case
        if steps is not UNSET:
            field_dict["Steps"] = steps
        if attached_files is not UNSET:
            field_dict["AttachedFiles"] = attached_files
        if edit_layout is not UNSET:
            field_dict["EditLayout"] = edit_layout
        if location is not UNSET:
            field_dict["Location"] = location
        if execution_logs is not UNSET:
            field_dict["ExecutionLogs"] = execution_logs
        if execution_data_attributes is not UNSET:
            field_dict["ExecutionDataAttributes"] = execution_data_attributes
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions
        if require_actual_result is not UNSET:
            field_dict["RequireActualResult"] = require_actual_result
        if edit_status is not UNSET:
            field_dict["EditStatus"] = edit_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachment_info import ApiAttachmentInfo
        from ..models.api_edit_layout import ApiEditLayout
        from ..models.api_editable_info import ApiEditableInfo
        from ..models.api_field_value_date_time import ApiFieldValueDateTime
        from ..models.api_field_value_time_span import ApiFieldValueTimeSpan
        from ..models.api_field_value_user import ApiFieldValueUser
        from ..models.api_field_with_value import ApiFieldWithValue
        from ..models.api_item import ApiItem
        from ..models.api_item_location import ApiItemLocation
        from ..models.api_label_attached import ApiLabelAttached
        from ..models.api_test_execution_data_attribute import ApiTestExecutionDataAttribute
        from ..models.api_test_execution_log import ApiTestExecutionLog
        from ..models.api_test_execution_permission import ApiTestExecutionPermission
        from ..models.api_test_execution_test_scenario_info import ApiTestExecutionTestScenarioInfo
        from ..models.api_test_step_execution import ApiTestStepExecution

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        formatted_id = d.pop("FormattedId", UNSET)

        guid = d.pop("Guid", UNSET)

        _test_execution_type = d.pop("TestExecutionType", UNSET)
        test_execution_type: Union[Unset, ApiTestExecutionType]
        if isinstance(_test_execution_type, Unset):
            test_execution_type = UNSET
        else:
            test_execution_type = ApiTestExecutionType(_test_execution_type)

        test_case_id = d.pop("TestCaseId", UNSET)

        test_case_name = d.pop("TestCaseName", UNSET)

        test_case_formatted_id = d.pop("TestCaseFormattedId", UNSET)

        _last_editor = d.pop("LastEditor", UNSET)
        last_editor: Union[Unset, None, ApiFieldValueUser]
        if _last_editor is None:
            last_editor = None
        elif isinstance(_last_editor, Unset):
            last_editor = UNSET
        else:
            last_editor = ApiFieldValueUser.from_dict(_last_editor)

        _tester = d.pop("Tester", UNSET)
        tester: Union[Unset, None, ApiFieldValueUser]
        if _tester is None:
            tester = None
        elif isinstance(_tester, Unset):
            tester = UNSET
        else:
            tester = ApiFieldValueUser.from_dict(_tester)

        _execution_date = d.pop("ExecutionDate", UNSET)
        execution_date: Union[Unset, None, ApiFieldValueDateTime]
        if _execution_date is None:
            execution_date = None
        elif isinstance(_execution_date, Unset):
            execution_date = UNSET
        else:
            execution_date = ApiFieldValueDateTime.from_dict(_execution_date)

        _last_modified = d.pop("LastModified", UNSET)
        last_modified: Union[Unset, None, ApiFieldValueDateTime]
        if _last_modified is None:
            last_modified = None
        elif isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = ApiFieldValueDateTime.from_dict(_last_modified)

        _execution_duration = d.pop("ExecutionDuration", UNSET)
        execution_duration: Union[Unset, None, ApiFieldValueTimeSpan]
        if _execution_duration is None:
            execution_duration = None
        elif isinstance(_execution_duration, Unset):
            execution_duration = UNSET
        else:
            execution_duration = ApiFieldValueTimeSpan.from_dict(_execution_duration)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiTestExecutionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiTestExecutionStatus(_status)

        value_set_name = d.pop("ValueSetName", UNSET)

        version = d.pop("Version", UNSET)

        tested_version = d.pop("TestedVersion", UNSET)

        _irrelevant_flagged_by = d.pop("IrrelevantFlaggedBy", UNSET)
        irrelevant_flagged_by: Union[Unset, None, ApiFieldValueUser]
        if _irrelevant_flagged_by is None:
            irrelevant_flagged_by = None
        elif isinstance(_irrelevant_flagged_by, Unset):
            irrelevant_flagged_by = UNSET
        else:
            irrelevant_flagged_by = ApiFieldValueUser.from_dict(_irrelevant_flagged_by)

        _irrelevant_flagged_at = d.pop("IrrelevantFlaggedAt", UNSET)
        irrelevant_flagged_at: Union[Unset, None, ApiFieldValueDateTime]
        if _irrelevant_flagged_at is None:
            irrelevant_flagged_at = None
        elif isinstance(_irrelevant_flagged_at, Unset):
            irrelevant_flagged_at = UNSET
        else:
            irrelevant_flagged_at = ApiFieldValueDateTime.from_dict(_irrelevant_flagged_at)

        irrelevant_reason = d.pop("IrrelevantReason", UNSET)

        irrelevant = d.pop("Irrelevant", UNSET)

        agent_to_use = d.pop("AgentToUse", UNSET)

        is_finalized = d.pop("IsFinalized", UNSET)

        has_attachment = d.pop("HasAttachment", UNSET)

        has_defect = d.pop("HasDefect", UNSET)

        _test_scenario_info = d.pop("TestScenarioInfo", UNSET)
        test_scenario_info: Union[Unset, None, ApiTestExecutionTestScenarioInfo]
        if _test_scenario_info is None:
            test_scenario_info = None
        elif isinstance(_test_scenario_info, Unset):
            test_scenario_info = UNSET
        else:
            test_scenario_info = ApiTestExecutionTestScenarioInfo.from_dict(_test_scenario_info)

        attached_labels = []
        _attached_labels = d.pop("AttachedLabels", UNSET)
        for attached_labels_item_data in _attached_labels or []:
            attached_labels_item = ApiLabelAttached.from_dict(attached_labels_item_data)

            attached_labels.append(attached_labels_item)

        custom_fields = []
        _custom_fields = d.pop("CustomFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = ApiFieldWithValue.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        _history_test_case = d.pop("HistoryTestCase", UNSET)
        history_test_case: Union[Unset, None, ApiItem]
        if _history_test_case is None:
            history_test_case = None
        elif isinstance(_history_test_case, Unset):
            history_test_case = UNSET
        else:
            history_test_case = ApiItem.from_dict(_history_test_case)

        steps = []
        _steps = d.pop("Steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = ApiTestStepExecution.from_dict(steps_item_data)

            steps.append(steps_item)

        attached_files = []
        _attached_files = d.pop("AttachedFiles", UNSET)
        for attached_files_item_data in _attached_files or []:
            attached_files_item = ApiAttachmentInfo.from_dict(attached_files_item_data)

            attached_files.append(attached_files_item)

        _edit_layout = d.pop("EditLayout", UNSET)
        edit_layout: Union[Unset, None, ApiEditLayout]
        if _edit_layout is None:
            edit_layout = None
        elif isinstance(_edit_layout, Unset):
            edit_layout = UNSET
        else:
            edit_layout = ApiEditLayout.from_dict(_edit_layout)

        _location = d.pop("Location", UNSET)
        location: Union[Unset, None, ApiItemLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = ApiItemLocation.from_dict(_location)

        execution_logs = []
        _execution_logs = d.pop("ExecutionLogs", UNSET)
        for execution_logs_item_data in _execution_logs or []:
            execution_logs_item = ApiTestExecutionLog.from_dict(execution_logs_item_data)

            execution_logs.append(execution_logs_item)

        execution_data_attributes = []
        _execution_data_attributes = d.pop("ExecutionDataAttributes", UNSET)
        for execution_data_attributes_item_data in _execution_data_attributes or []:
            execution_data_attributes_item = ApiTestExecutionDataAttribute.from_dict(
                execution_data_attributes_item_data
            )

            execution_data_attributes.append(execution_data_attributes_item)

        _permissions = d.pop("Permissions", UNSET)
        permissions: Union[Unset, None, ApiTestExecutionPermission]
        if _permissions is None:
            permissions = None
        elif isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ApiTestExecutionPermission.from_dict(_permissions)

        require_actual_result = d.pop("RequireActualResult", UNSET)

        _edit_status = d.pop("EditStatus", UNSET)
        edit_status: Union[Unset, None, ApiEditableInfo]
        if _edit_status is None:
            edit_status = None
        elif isinstance(_edit_status, Unset):
            edit_status = UNSET
        else:
            edit_status = ApiEditableInfo.from_dict(_edit_status)

        api_test_execution = cls(
            id=id,
            formatted_id=formatted_id,
            guid=guid,
            test_execution_type=test_execution_type,
            test_case_id=test_case_id,
            test_case_name=test_case_name,
            test_case_formatted_id=test_case_formatted_id,
            last_editor=last_editor,
            tester=tester,
            execution_date=execution_date,
            last_modified=last_modified,
            execution_duration=execution_duration,
            status=status,
            value_set_name=value_set_name,
            version=version,
            tested_version=tested_version,
            irrelevant_flagged_by=irrelevant_flagged_by,
            irrelevant_flagged_at=irrelevant_flagged_at,
            irrelevant_reason=irrelevant_reason,
            irrelevant=irrelevant,
            agent_to_use=agent_to_use,
            is_finalized=is_finalized,
            has_attachment=has_attachment,
            has_defect=has_defect,
            test_scenario_info=test_scenario_info,
            attached_labels=attached_labels,
            custom_fields=custom_fields,
            history_test_case=history_test_case,
            steps=steps,
            attached_files=attached_files,
            edit_layout=edit_layout,
            location=location,
            execution_logs=execution_logs,
            execution_data_attributes=execution_data_attributes,
            permissions=permissions,
            require_actual_result=require_actual_result,
            edit_status=edit_status,
        )

        api_test_execution.additional_properties = d
        return api_test_execution

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
