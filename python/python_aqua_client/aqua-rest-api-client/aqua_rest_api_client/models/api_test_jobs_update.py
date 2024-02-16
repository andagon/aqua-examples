from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_job_new import ApiTestJobNew
    from ..models.api_test_job_update_with_id import ApiTestJobUpdateWithId


T = TypeVar("T", bound="ApiTestJobsUpdate")


@attr.s(auto_attribs=True)
class ApiTestJobsUpdate:
    """
    Attributes:
        added (Union[Unset, None, List['ApiTestJobNew']]): A list with the new test jobs which should be added.
        modified (Union[Unset, None, List['ApiTestJobUpdateWithId']]): A list with test jobs which should be updated.
        removed (Union[Unset, None, List[int]]): A list with the ids of the test jobs which should be removed.
    """

    added: Union[Unset, None, List["ApiTestJobNew"]] = UNSET
    modified: Union[Unset, None, List["ApiTestJobUpdateWithId"]] = UNSET
    removed: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        added: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.added, Unset):
            if self.added is None:
                added = None
            else:
                added = []
                for added_item_data in self.added:
                    added_item = added_item_data.to_dict()

                    added.append(added_item)

        modified: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.modified, Unset):
            if self.modified is None:
                modified = None
            else:
                modified = []
                for modified_item_data in self.modified:
                    modified_item = modified_item_data.to_dict()

                    modified.append(modified_item)

        removed: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.removed, Unset):
            if self.removed is None:
                removed = None
            else:
                removed = self.removed

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if added is not UNSET:
            field_dict["Added"] = added
        if modified is not UNSET:
            field_dict["Modified"] = modified
        if removed is not UNSET:
            field_dict["Removed"] = removed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_job_new import ApiTestJobNew
        from ..models.api_test_job_update_with_id import ApiTestJobUpdateWithId

        d = src_dict.copy()
        added = []
        _added = d.pop("Added", UNSET)
        for added_item_data in _added or []:
            added_item = ApiTestJobNew.from_dict(added_item_data)

            added.append(added_item)

        modified = []
        _modified = d.pop("Modified", UNSET)
        for modified_item_data in _modified or []:
            modified_item = ApiTestJobUpdateWithId.from_dict(modified_item_data)

            modified.append(modified_item)

        removed = cast(List[int], d.pop("Removed", UNSET))

        api_test_jobs_update = cls(
            added=added,
            modified=modified,
            removed=removed,
        )

        return api_test_jobs_update
