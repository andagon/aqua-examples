from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_import_phase import ApiImportPhase
from ..models.api_long_operation_status import ApiLongOperationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_import_error_report_item import ApiImportErrorReportItem


T = TypeVar("T", bound="ApiImportLongRunningTaskInfo")


@attr.s(auto_attribs=True)
class ApiImportLongRunningTaskInfo:
    """
    Attributes:
        info_type (str):
        status (Union[Unset, ApiLongOperationStatus]): Represents status of a long running operation.
            This enum has the following values:
              - `Aborted` Long operation has been aborted.
              - `BlockedByAnotherTask` Long operation has been blocked by another task.
              - `Failed` Long operation has failed.
              - `Finished` Long operation has finished without problems.
              - `FinishedWithWarning` Long operation has finished but there were some problems.
              - `InProgress` Long operation is in progress.
              - `Queued` Long operation has been queued, not started yet.
        done (Union[Unset, int]): Number of elements processed so far. Includes also failed elements.
        total (Union[Unset, int]): Number of all elements to be processed.
        failed (Union[Unset, int]): Number of all elements that could not be processed.
        failed_items (Union[Unset, None, List['ApiImportErrorReportItem']]): List of failed imports.
        expected_phases (Union[Unset, None, List[ApiImportPhase]]): List of expected phases during import, filled only
            after the excel file was read
        current_phase (Union[Unset, ApiImportPhase]): Represents reason of a failure of import operation
            The enumeration is sorted in the order these phases occur during import
            This enum has the following values:
              - `CreatingDependencies` Creating Depedencies
              - `CreatingHierarchy` Creating Requirement Hierarchy
              - `CreatingTestJobs` Creating TestJobs from Testcases for TestScenarios, only using TestCases/TestScenarios
            created during this import
              - `Done` Finished
              - `Error` Aborted due to error during import
              - `Finishing` Finishing up, writing Data to DB
              - `ImportingDefects` Importing Defects
              - `ImportingRequirements` Importing Requirements
              - `ImportingTestCases` Importing TestCases and TestSteps
              - `ImportingTestScenarios` Importing Testscenarion WITHOUT TestJobs
              - `Initializing` Preparing for reading of file
              - `ReadingFile` Reading the excel file and trying to map columns to baseobject-properties
    """

    info_type: str
    status: Union[Unset, ApiLongOperationStatus] = UNSET
    done: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    failed: Union[Unset, int] = UNSET
    failed_items: Union[Unset, None, List["ApiImportErrorReportItem"]] = UNSET
    expected_phases: Union[Unset, None, List[ApiImportPhase]] = UNSET
    current_phase: Union[Unset, ApiImportPhase] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        info_type = self.info_type
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        done = self.done
        total = self.total
        failed = self.failed
        failed_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.failed_items, Unset):
            if self.failed_items is None:
                failed_items = None
            else:
                failed_items = []
                for failed_items_item_data in self.failed_items:
                    failed_items_item = failed_items_item_data.to_dict()

                    failed_items.append(failed_items_item)

        expected_phases: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.expected_phases, Unset):
            if self.expected_phases is None:
                expected_phases = None
            else:
                expected_phases = []
                for expected_phases_item_data in self.expected_phases:
                    expected_phases_item = expected_phases_item_data.value

                    expected_phases.append(expected_phases_item)

        current_phase: Union[Unset, str] = UNSET
        if not isinstance(self.current_phase, Unset):
            current_phase = self.current_phase.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "InfoType": info_type,
            }
        )
        if status is not UNSET:
            field_dict["Status"] = status
        if done is not UNSET:
            field_dict["Done"] = done
        if total is not UNSET:
            field_dict["Total"] = total
        if failed is not UNSET:
            field_dict["Failed"] = failed
        if failed_items is not UNSET:
            field_dict["FailedItems"] = failed_items
        if expected_phases is not UNSET:
            field_dict["ExpectedPhases"] = expected_phases
        if current_phase is not UNSET:
            field_dict["CurrentPhase"] = current_phase

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_import_error_report_item import ApiImportErrorReportItem

        d = src_dict.copy()
        info_type = d.pop("InfoType")

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiLongOperationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiLongOperationStatus(_status)

        done = d.pop("Done", UNSET)

        total = d.pop("Total", UNSET)

        failed = d.pop("Failed", UNSET)

        failed_items = []
        _failed_items = d.pop("FailedItems", UNSET)
        for failed_items_item_data in _failed_items or []:
            failed_items_item = ApiImportErrorReportItem.from_dict(failed_items_item_data)

            failed_items.append(failed_items_item)

        expected_phases = []
        _expected_phases = d.pop("ExpectedPhases", UNSET)
        for expected_phases_item_data in _expected_phases or []:
            expected_phases_item = ApiImportPhase(expected_phases_item_data)

            expected_phases.append(expected_phases_item)

        _current_phase = d.pop("CurrentPhase", UNSET)
        current_phase: Union[Unset, ApiImportPhase]
        if isinstance(_current_phase, Unset):
            current_phase = UNSET
        else:
            current_phase = ApiImportPhase(_current_phase)

        api_import_long_running_task_info = cls(
            info_type=info_type,
            status=status,
            done=done,
            total=total,
            failed=failed,
            failed_items=failed_items,
            expected_phases=expected_phases,
            current_phase=current_phase,
        )

        api_import_long_running_task_info.additional_properties = d
        return api_import_long_running_task_info

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
