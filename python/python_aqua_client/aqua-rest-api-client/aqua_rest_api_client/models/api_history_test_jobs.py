from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_history_test_job_modified import ApiHistoryTestJobModified


T = TypeVar("T", bound="ApiHistoryTestJobs")


@attr.s(auto_attribs=True)
class ApiHistoryTestJobs:
    """The list of changes to the test jobs of a test scenario.

    Attributes:
        added (Union[Unset, None, List[str]]): The list of names of the test jobs which were added
            to the test scenario.
        removed (Union[Unset, None, List[str]]): The list of names of the test jobs which were removed
            from the test scenario.
        rearranged (Union[Unset, bool]): True is any test jobs have been rearranged (i.e. changed their positions).
        modified (Union[Unset, None, List['ApiHistoryTestJobModified']]): The list of test jobs which were modified.
    """

    added: Union[Unset, None, List[str]] = UNSET
    removed: Union[Unset, None, List[str]] = UNSET
    rearranged: Union[Unset, bool] = UNSET
    modified: Union[Unset, None, List["ApiHistoryTestJobModified"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        added: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.added, Unset):
            if self.added is None:
                added = None
            else:
                added = self.added

        removed: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.removed, Unset):
            if self.removed is None:
                removed = None
            else:
                removed = self.removed

        rearranged = self.rearranged
        modified: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.modified, Unset):
            if self.modified is None:
                modified = None
            else:
                modified = []
                for modified_item_data in self.modified:
                    modified_item = modified_item_data.to_dict()

                    modified.append(modified_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if added is not UNSET:
            field_dict["Added"] = added
        if removed is not UNSET:
            field_dict["Removed"] = removed
        if rearranged is not UNSET:
            field_dict["Rearranged"] = rearranged
        if modified is not UNSET:
            field_dict["Modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_history_test_job_modified import ApiHistoryTestJobModified

        d = src_dict.copy()
        added = cast(List[str], d.pop("Added", UNSET))

        removed = cast(List[str], d.pop("Removed", UNSET))

        rearranged = d.pop("Rearranged", UNSET)

        modified = []
        _modified = d.pop("Modified", UNSET)
        for modified_item_data in _modified or []:
            modified_item = ApiHistoryTestJobModified.from_dict(modified_item_data)

            modified.append(modified_item)

        api_history_test_jobs = cls(
            added=added,
            removed=removed,
            rearranged=rearranged,
            modified=modified,
        )

        return api_history_test_jobs
