from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_case_execution_history_entry import ApiTestCaseExecutionHistoryEntry


T = TypeVar("T", bound="ApiTestCaseExecutionHistory")


@attr.s(auto_attribs=True)
class ApiTestCaseExecutionHistory:
    """Historic information regarding the last executions
    of a test case or test job.

        Attributes:
            max_number_of_entries (Union[Unset, int]): The maximum number of entries the history can have. The history can
                have less entries when the test case or test job has not been executed
                that often yet.
            entries (Union[Unset, None, List['ApiTestCaseExecutionHistoryEntry']]): The list of history entries.
    """

    max_number_of_entries: Union[Unset, int] = UNSET
    entries: Union[Unset, None, List["ApiTestCaseExecutionHistoryEntry"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        max_number_of_entries = self.max_number_of_entries
        entries: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            if self.entries is None:
                entries = None
            else:
                entries = []
                for entries_item_data in self.entries:
                    entries_item = entries_item_data.to_dict()

                    entries.append(entries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if max_number_of_entries is not UNSET:
            field_dict["MaxNumberOfEntries"] = max_number_of_entries
        if entries is not UNSET:
            field_dict["Entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_case_execution_history_entry import ApiTestCaseExecutionHistoryEntry

        d = src_dict.copy()
        max_number_of_entries = d.pop("MaxNumberOfEntries", UNSET)

        entries = []
        _entries = d.pop("Entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ApiTestCaseExecutionHistoryEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        api_test_case_execution_history = cls(
            max_number_of_entries=max_number_of_entries,
            entries=entries,
        )

        return api_test_case_execution_history
