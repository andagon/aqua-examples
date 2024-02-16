from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.api_test_step_execution_status import ApiTestStepExecutionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_label_info import ApiLabelInfo
    from ..models.api_rich_text import ApiRichText
    from ..models.value_tuple_of_integer_and_string import ValueTupleOfIntegerAndString


T = TypeVar("T", bound="ApiBulkExecutionsRequest")


@attr.s(auto_attribs=True)
class ApiBulkExecutionsRequest:
    """
    Attributes:
        project_id (Union[Unset, int]): The Id of the project containing the test cases
        folder_id (Union[Unset, int]): The Id of the folder containing the test cases.
            This is used for a permission check to verify that the
            user has permission to Finalize the test executions if needed
        test_case_ids (Union[Unset, None, List[int]]): The test case Id and the value set to use for each test case
        value_set_guids (Union[Unset, None, List['ValueTupleOfIntegerAndString']]): The value set to use for each test
            case execution (Item1 is the
            test case Id and Item2 is the value set GUID)
        finalize (Union[Unset, bool]): Whether or not the test execution should be finalized
        labels (Union[Unset, None, List['ApiLabelInfo']]): The labels that should be added to the test executions
        version (Union[Unset, None, str]): The version number to associate with the test executions
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
        actual_result (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
    """

    project_id: Union[Unset, int] = UNSET
    folder_id: Union[Unset, int] = UNSET
    test_case_ids: Union[Unset, None, List[int]] = UNSET
    value_set_guids: Union[Unset, None, List["ValueTupleOfIntegerAndString"]] = UNSET
    finalize: Union[Unset, bool] = UNSET
    labels: Union[Unset, None, List["ApiLabelInfo"]] = UNSET
    version: Union[Unset, None, str] = UNSET
    status: Union[Unset, ApiTestStepExecutionStatus] = UNSET
    actual_result: Union[Unset, None, "ApiRichText"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        folder_id = self.folder_id
        test_case_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.test_case_ids, Unset):
            if self.test_case_ids is None:
                test_case_ids = None
            else:
                test_case_ids = self.test_case_ids

        value_set_guids: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.value_set_guids, Unset):
            if self.value_set_guids is None:
                value_set_guids = None
            else:
                value_set_guids = []
                for value_set_guids_item_data in self.value_set_guids:
                    value_set_guids_item = value_set_guids_item_data.to_dict()

                    value_set_guids.append(value_set_guids_item)

        finalize = self.finalize
        labels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            if self.labels is None:
                labels = None
            else:
                labels = []
                for labels_item_data in self.labels:
                    labels_item = labels_item_data.to_dict()

                    labels.append(labels_item)

        version = self.version
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        actual_result: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.actual_result, Unset):
            actual_result = self.actual_result.to_dict() if self.actual_result else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if test_case_ids is not UNSET:
            field_dict["TestCaseIds"] = test_case_ids
        if value_set_guids is not UNSET:
            field_dict["ValueSetGuids"] = value_set_guids
        if finalize is not UNSET:
            field_dict["Finalize"] = finalize
        if labels is not UNSET:
            field_dict["Labels"] = labels
        if version is not UNSET:
            field_dict["Version"] = version
        if status is not UNSET:
            field_dict["Status"] = status
        if actual_result is not UNSET:
            field_dict["ActualResult"] = actual_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_label_info import ApiLabelInfo
        from ..models.api_rich_text import ApiRichText
        from ..models.value_tuple_of_integer_and_string import ValueTupleOfIntegerAndString

        d = src_dict.copy()
        project_id = d.pop("ProjectId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        test_case_ids = cast(List[int], d.pop("TestCaseIds", UNSET))

        value_set_guids = []
        _value_set_guids = d.pop("ValueSetGuids", UNSET)
        for value_set_guids_item_data in _value_set_guids or []:
            value_set_guids_item = ValueTupleOfIntegerAndString.from_dict(value_set_guids_item_data)

            value_set_guids.append(value_set_guids_item)

        finalize = d.pop("Finalize", UNSET)

        labels = []
        _labels = d.pop("Labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = ApiLabelInfo.from_dict(labels_item_data)

            labels.append(labels_item)

        version = d.pop("Version", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiTestStepExecutionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiTestStepExecutionStatus(_status)

        _actual_result = d.pop("ActualResult", UNSET)
        actual_result: Union[Unset, None, ApiRichText]
        if _actual_result is None:
            actual_result = None
        elif isinstance(_actual_result, Unset):
            actual_result = UNSET
        else:
            actual_result = ApiRichText.from_dict(_actual_result)

        api_bulk_executions_request = cls(
            project_id=project_id,
            folder_id=folder_id,
            test_case_ids=test_case_ids,
            value_set_guids=value_set_guids,
            finalize=finalize,
            labels=labels,
            version=version,
            status=status,
            actual_result=actual_result,
        )

        return api_bulk_executions_request
