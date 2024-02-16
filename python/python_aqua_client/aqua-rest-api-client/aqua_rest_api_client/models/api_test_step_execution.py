import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_automation_technology import ApiAutomationTechnology
from ..models.api_test_step_execution_status import ApiTestStepExecutionStatus
from ..models.api_test_step_type import ApiTestStepType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value_user import ApiFieldValueUser
    from ..models.api_rich_text import ApiRichText
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiTestStepExecution")


@attr.s(auto_attribs=True)
class ApiTestStepExecution:
    """Represents single step of a test execution (manual or automated).

    Attributes:
        id (Union[Unset, int]): Id of this step execution
        status (Union[Unset, ApiTestStepExecutionStatus]): Identifies the status of a test step execution.
            This enum has the following values:
              - `Aborted` Step has been aborted.
              - `Blocked` Step has been blocked.
              - `Failed` Step has failed.
              - `InProgress` Is being executed by some agent.
              - `NotApplicable` Step is not applicable for the current test execution, not considered for overall execution
            status.
              - `NotRun` Step has not been run yet.
              - `Pass` Step has passed.
              - `Queued` Directly queued for execution, will be executed as soon as agent is able to process it.
        name (Union[Unset, None, str]): Name of executed step
        index (Union[Unset, int]): The index of this test step. The index does not need to be consecutive as partial
            execution is allowed.
        step_type (Union[Unset, ApiTestStepType]): Identifies the type of an execution.
            This enum has the following values:
              - `Condition` Represents 'condition'
              - `NestedTestCase` Only for internal use.
              - `Step` Represents 'step'
        description (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
        expected_results (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in
            several different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
        actual_results (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
        actual_results_last_updated_by (Union[Unset, None, ApiUserInfo]): The user information
        actual_results_last_updated (Union[Unset, datetime.datetime]): The time when the Actual Result was updated
        agents_used (Union[Unset, None, str]): Agent used to execute this step (if any).
            Note: in case of JMeter automation it can happen (but this is very uncommon though)
            that more than one agent executes the step. In this case this field contains comma separated list of agents.
        last_editor (Union[Unset, None, ApiFieldValueUser]):
        has_defect (Union[Unset, bool]): Indicates whether a defect exists which is related to this test step.
        automation_technology (Union[Unset, ApiAutomationTechnology]): Represents the different test automation
            technologies supported
            by aqua.
            This enum has the following values:
              - `Database` aqua's database automation technology allows to execute
            SQL instructions against various database management
            systems.
              - `Jenkins` Integration with the Jenkins CI and CD server. Allows to
            trigger jobs on the Jenkins server.
              - `JMeter` Integration of the load and performance test tool Apache
            JMeter.
              - `None` No test automation technology is used.
              - `PowerShell` aqua's Powershell integration allows to execute
            arbitrary Powershell scripts.
              - `QTP` HP QuickTest Professional integration
              - `Ranorex` Ranorex integration
              - `SoapUI` SoapUI integration
              - `UFT` MicroFocus Unified Functional Testing integration
              - `UnixShell` aqua's UnixShell integration allows to execute arbitrary
            unix shell scripts in various languages.
    """

    id: Union[Unset, int] = UNSET
    status: Union[Unset, ApiTestStepExecutionStatus] = UNSET
    name: Union[Unset, None, str] = UNSET
    index: Union[Unset, int] = UNSET
    step_type: Union[Unset, ApiTestStepType] = UNSET
    description: Union[Unset, None, "ApiRichText"] = UNSET
    expected_results: Union[Unset, None, "ApiRichText"] = UNSET
    actual_results: Union[Unset, None, "ApiRichText"] = UNSET
    actual_results_last_updated_by: Union[Unset, None, "ApiUserInfo"] = UNSET
    actual_results_last_updated: Union[Unset, datetime.datetime] = UNSET
    agents_used: Union[Unset, None, str] = UNSET
    last_editor: Union[Unset, None, "ApiFieldValueUser"] = UNSET
    has_defect: Union[Unset, bool] = UNSET
    automation_technology: Union[Unset, ApiAutomationTechnology] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name = self.name
        index = self.index
        step_type: Union[Unset, str] = UNSET
        if not isinstance(self.step_type, Unset):
            step_type = self.step_type.value

        description: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict() if self.description else None

        expected_results: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.expected_results, Unset):
            expected_results = self.expected_results.to_dict() if self.expected_results else None

        actual_results: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.actual_results, Unset):
            actual_results = self.actual_results.to_dict() if self.actual_results else None

        actual_results_last_updated_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.actual_results_last_updated_by, Unset):
            actual_results_last_updated_by = (
                self.actual_results_last_updated_by.to_dict() if self.actual_results_last_updated_by else None
            )

        actual_results_last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.actual_results_last_updated, Unset):
            actual_results_last_updated = self.actual_results_last_updated.isoformat()

        agents_used = self.agents_used
        last_editor: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_editor, Unset):
            last_editor = self.last_editor.to_dict() if self.last_editor else None

        has_defect = self.has_defect
        automation_technology: Union[Unset, str] = UNSET
        if not isinstance(self.automation_technology, Unset):
            automation_technology = self.automation_technology.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if status is not UNSET:
            field_dict["Status"] = status
        if name is not UNSET:
            field_dict["Name"] = name
        if index is not UNSET:
            field_dict["Index"] = index
        if step_type is not UNSET:
            field_dict["StepType"] = step_type
        if description is not UNSET:
            field_dict["Description"] = description
        if expected_results is not UNSET:
            field_dict["ExpectedResults"] = expected_results
        if actual_results is not UNSET:
            field_dict["ActualResults"] = actual_results
        if actual_results_last_updated_by is not UNSET:
            field_dict["ActualResultsLastUpdatedBy"] = actual_results_last_updated_by
        if actual_results_last_updated is not UNSET:
            field_dict["ActualResultsLastUpdated"] = actual_results_last_updated
        if agents_used is not UNSET:
            field_dict["AgentsUsed"] = agents_used
        if last_editor is not UNSET:
            field_dict["LastEditor"] = last_editor
        if has_defect is not UNSET:
            field_dict["HasDefect"] = has_defect
        if automation_technology is not UNSET:
            field_dict["AutomationTechnology"] = automation_technology

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_user import ApiFieldValueUser
        from ..models.api_rich_text import ApiRichText
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiTestStepExecutionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiTestStepExecutionStatus(_status)

        name = d.pop("Name", UNSET)

        index = d.pop("Index", UNSET)

        _step_type = d.pop("StepType", UNSET)
        step_type: Union[Unset, ApiTestStepType]
        if isinstance(_step_type, Unset):
            step_type = UNSET
        else:
            step_type = ApiTestStepType(_step_type)

        _description = d.pop("Description", UNSET)
        description: Union[Unset, None, ApiRichText]
        if _description is None:
            description = None
        elif isinstance(_description, Unset):
            description = UNSET
        else:
            description = ApiRichText.from_dict(_description)

        _expected_results = d.pop("ExpectedResults", UNSET)
        expected_results: Union[Unset, None, ApiRichText]
        if _expected_results is None:
            expected_results = None
        elif isinstance(_expected_results, Unset):
            expected_results = UNSET
        else:
            expected_results = ApiRichText.from_dict(_expected_results)

        _actual_results = d.pop("ActualResults", UNSET)
        actual_results: Union[Unset, None, ApiRichText]
        if _actual_results is None:
            actual_results = None
        elif isinstance(_actual_results, Unset):
            actual_results = UNSET
        else:
            actual_results = ApiRichText.from_dict(_actual_results)

        _actual_results_last_updated_by = d.pop("ActualResultsLastUpdatedBy", UNSET)
        actual_results_last_updated_by: Union[Unset, None, ApiUserInfo]
        if _actual_results_last_updated_by is None:
            actual_results_last_updated_by = None
        elif isinstance(_actual_results_last_updated_by, Unset):
            actual_results_last_updated_by = UNSET
        else:
            actual_results_last_updated_by = ApiUserInfo.from_dict(_actual_results_last_updated_by)

        _actual_results_last_updated = d.pop("ActualResultsLastUpdated", UNSET)
        actual_results_last_updated: Union[Unset, datetime.datetime]
        if isinstance(_actual_results_last_updated, Unset):
            actual_results_last_updated = UNSET
        else:
            actual_results_last_updated = isoparse(_actual_results_last_updated)

        agents_used = d.pop("AgentsUsed", UNSET)

        _last_editor = d.pop("LastEditor", UNSET)
        last_editor: Union[Unset, None, ApiFieldValueUser]
        if _last_editor is None:
            last_editor = None
        elif isinstance(_last_editor, Unset):
            last_editor = UNSET
        else:
            last_editor = ApiFieldValueUser.from_dict(_last_editor)

        has_defect = d.pop("HasDefect", UNSET)

        _automation_technology = d.pop("AutomationTechnology", UNSET)
        automation_technology: Union[Unset, ApiAutomationTechnology]
        if isinstance(_automation_technology, Unset):
            automation_technology = UNSET
        else:
            automation_technology = ApiAutomationTechnology(_automation_technology)

        api_test_step_execution = cls(
            id=id,
            status=status,
            name=name,
            index=index,
            step_type=step_type,
            description=description,
            expected_results=expected_results,
            actual_results=actual_results,
            actual_results_last_updated_by=actual_results_last_updated_by,
            actual_results_last_updated=actual_results_last_updated,
            agents_used=agents_used,
            last_editor=last_editor,
            has_defect=has_defect,
            automation_technology=automation_technology,
        )

        return api_test_step_execution
