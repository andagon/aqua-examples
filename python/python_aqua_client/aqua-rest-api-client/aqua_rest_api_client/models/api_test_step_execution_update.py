import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_test_step_execution_update_status import ApiTestStepExecutionUpdateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_rich_text import ApiRichText
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiTestStepExecutionUpdate")


@attr.s(auto_attribs=True)
class ApiTestStepExecutionUpdate:
    """
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
        id (Union[Unset, int]): The id of the test step.
        actual_results_last_updated_by (Union[Unset, None, ApiUserInfo]): The user information
        actual_results_last_updated (Union[Unset, datetime.datetime]): The time when the Actual Result was updated
    """

    status: Union[Unset, None, ApiTestStepExecutionUpdateStatus] = UNSET
    actual_results: Union[Unset, None, "ApiRichText"] = UNSET
    id: Union[Unset, int] = UNSET
    actual_results_last_updated_by: Union[Unset, None, "ApiUserInfo"] = UNSET
    actual_results_last_updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, None, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        actual_results: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.actual_results, Unset):
            actual_results = self.actual_results.to_dict() if self.actual_results else None

        id = self.id
        actual_results_last_updated_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.actual_results_last_updated_by, Unset):
            actual_results_last_updated_by = (
                self.actual_results_last_updated_by.to_dict() if self.actual_results_last_updated_by else None
            )

        actual_results_last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.actual_results_last_updated, Unset):
            actual_results_last_updated = self.actual_results_last_updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["Status"] = status
        if actual_results is not UNSET:
            field_dict["ActualResults"] = actual_results
        if id is not UNSET:
            field_dict["Id"] = id
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

        id = d.pop("Id", UNSET)

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

        api_test_step_execution_update = cls(
            status=status,
            actual_results=actual_results,
            id=id,
            actual_results_last_updated_by=actual_results_last_updated_by,
            actual_results_last_updated=actual_results_last_updated,
        )

        api_test_step_execution_update.additional_properties = d
        return api_test_step_execution_update

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
