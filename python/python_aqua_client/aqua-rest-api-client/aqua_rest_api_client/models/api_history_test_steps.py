from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_history_test_step_modified import ApiHistoryTestStepModified


T = TypeVar("T", bound="ApiHistoryTestSteps")


@attr.s(auto_attribs=True)
class ApiHistoryTestSteps:
    """The list of changes to the test steps of a test case.

    Attributes:
        rearranged (Union[Unset, bool]): True is any steps have been rearranged (i.e. changed their positions).
        added (Union[Unset, None, List[str]]): The list of test steps which were added.
        removed (Union[Unset, None, List[str]]): The list of test steps which were removed.
        modified (Union[Unset, None, List['ApiHistoryTestStepModified']]): The list of test steps which were modified.
    """

    rearranged: Union[Unset, bool] = UNSET
    added: Union[Unset, None, List[str]] = UNSET
    removed: Union[Unset, None, List[str]] = UNSET
    modified: Union[Unset, None, List["ApiHistoryTestStepModified"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rearranged = self.rearranged
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
        if rearranged is not UNSET:
            field_dict["Rearranged"] = rearranged
        if added is not UNSET:
            field_dict["Added"] = added
        if removed is not UNSET:
            field_dict["Removed"] = removed
        if modified is not UNSET:
            field_dict["Modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_history_test_step_modified import ApiHistoryTestStepModified

        d = src_dict.copy()
        rearranged = d.pop("Rearranged", UNSET)

        added = cast(List[str], d.pop("Added", UNSET))

        removed = cast(List[str], d.pop("Removed", UNSET))

        modified = []
        _modified = d.pop("Modified", UNSET)
        for modified_item_data in _modified or []:
            modified_item = ApiHistoryTestStepModified.from_dict(modified_item_data)

            modified.append(modified_item)

        api_history_test_steps = cls(
            rearranged=rearranged,
            added=added,
            removed=removed,
            modified=modified,
        )

        return api_history_test_steps
