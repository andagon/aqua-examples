from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_test_step_execution_update_status import ApiTestStepExecutionUpdateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_rich_text import ApiRichText


T = TypeVar("T", bound="ApiTestStepExecutionUpdateSingleStep")


@attr.s(auto_attribs=True)
class ApiTestStepExecutionUpdateSingleStep:
    """A test step execution single step to be updated.

    Attributes:
        status (Union[Unset, None, ApiTestStepExecutionUpdateStatus]): The list of statuses a test step execution can be
            set to
            when updating it.
            This enum has the following values:
              - `Blocked` The execution of the step is blocked.
              - `Failed` The execution of the step has failed.

              - `NotApplicable` Step is not applicable for the current test execution, not considered for overall execution
            status.
              - `NotRun` The step has not been executed yet.
              - `Pass` The step has been executed successfully.
        actual_results (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
    """

    status: Union[Unset, None, ApiTestStepExecutionUpdateStatus] = UNSET
    actual_results: Union[Unset, None, "ApiRichText"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, None, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        actual_results: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.actual_results, Unset):
            actual_results = self.actual_results.to_dict() if self.actual_results else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status is not UNSET:
            field_dict["Status"] = status
        if actual_results is not UNSET:
            field_dict["ActualResults"] = actual_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_rich_text import ApiRichText

        d = src_dict.copy()
        _status = d.pop("Status", UNSET)
        status: Union[Unset, None, ApiTestStepExecutionUpdateStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiTestStepExecutionUpdateStatus(_status)

        _actual_results = d.pop("ActualResults", UNSET)
        actual_results: Union[Unset, None, ApiRichText]
        if _actual_results is None:
            actual_results = None
        elif isinstance(_actual_results, Unset):
            actual_results = UNSET
        else:
            actual_results = ApiRichText.from_dict(_actual_results)

        api_test_step_execution_update_single_step = cls(
            status=status,
            actual_results=actual_results,
        )

        return api_test_step_execution_update_single_step
