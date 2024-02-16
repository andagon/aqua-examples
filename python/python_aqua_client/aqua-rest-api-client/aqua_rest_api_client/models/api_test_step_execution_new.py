import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_test_step_execution_step_type import ApiTestStepExecutionStepType
from ..models.api_test_step_execution_update_status import ApiTestStepExecutionUpdateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_rich_text import ApiRichText
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiTestStepExecutionNew")


@attr.s(auto_attribs=True)
class ApiTestStepExecutionNew:
    """A new test step execution to be saved.

    Attributes:
        index (Union[Unset, int]): The one-based index of this test step in the list
            of test steps.
        name (Union[Unset, None, str]): The name of this test step.
        step_type (Union[Unset, ApiTestStepExecutionStepType]): The possible step types for a test step execution.
            NestedTestCase is intentionally not included as test
            execution are flat. Test steps of a nested test case
            are merged into the flat test execution.
            This enum has the following values:
              - `Condition` The step represents a condition.
              - `Step` The step is a normal test step.
        status (Union[Unset, ApiTestStepExecutionUpdateStatus]): The list of statuses a test step execution can be set
            to
            when updating it.
            This enum has the following values:
              - `Blocked` The execution of the step is blocked.
              - `Failed` The execution of the step has failed.

              - `NotApplicable` Step is not applicable for the current test execution, not considered for overall execution
            status.
              - `NotRun` The step has not been executed yet.
              - `Pass` The step has been executed successfully.
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
    """

    index: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    step_type: Union[Unset, ApiTestStepExecutionStepType] = UNSET
    status: Union[Unset, ApiTestStepExecutionUpdateStatus] = UNSET
    description: Union[Unset, None, "ApiRichText"] = UNSET
    expected_results: Union[Unset, None, "ApiRichText"] = UNSET
    actual_results: Union[Unset, None, "ApiRichText"] = UNSET
    actual_results_last_updated_by: Union[Unset, None, "ApiUserInfo"] = UNSET
    actual_results_last_updated: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        name = self.name
        step_type: Union[Unset, str] = UNSET
        if not isinstance(self.step_type, Unset):
            step_type = self.step_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["Index"] = index
        if name is not UNSET:
            field_dict["Name"] = name
        if step_type is not UNSET:
            field_dict["StepType"] = step_type
        if status is not UNSET:
            field_dict["Status"] = status
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_rich_text import ApiRichText
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        index = d.pop("Index", UNSET)

        name = d.pop("Name", UNSET)

        _step_type = d.pop("StepType", UNSET)
        step_type: Union[Unset, ApiTestStepExecutionStepType]
        if isinstance(_step_type, Unset):
            step_type = UNSET
        else:
            step_type = ApiTestStepExecutionStepType(_step_type)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiTestStepExecutionUpdateStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiTestStepExecutionUpdateStatus(_status)

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

        api_test_step_execution_new = cls(
            index=index,
            name=name,
            step_type=step_type,
            status=status,
            description=description,
            expected_results=expected_results,
            actual_results=actual_results,
            actual_results_last_updated_by=actual_results_last_updated_by,
            actual_results_last_updated=actual_results_last_updated,
        )

        return api_test_step_execution_new
