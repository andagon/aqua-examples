from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_agile_backlog_status import ApiAgileBacklogStatus


T = TypeVar("T", bound="ApiAgileBacklog")


@attr.s(auto_attribs=True)
class ApiAgileBacklog:
    """Provides settings for backlog in Agile

    Attributes:
        requirement_statuses (Union[Unset, None, List['ApiAgileBacklogStatus']]): Available statuses for requirements
        defect_statuses (Union[Unset, None, List['ApiAgileBacklogStatus']]): Available statuses for defects
        test_case_statuses (Union[Unset, None, List['ApiAgileBacklogStatus']]): Available statuses for test cases
    """

    requirement_statuses: Union[Unset, None, List["ApiAgileBacklogStatus"]] = UNSET
    defect_statuses: Union[Unset, None, List["ApiAgileBacklogStatus"]] = UNSET
    test_case_statuses: Union[Unset, None, List["ApiAgileBacklogStatus"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        requirement_statuses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.requirement_statuses, Unset):
            if self.requirement_statuses is None:
                requirement_statuses = None
            else:
                requirement_statuses = []
                for requirement_statuses_item_data in self.requirement_statuses:
                    requirement_statuses_item = requirement_statuses_item_data.to_dict()

                    requirement_statuses.append(requirement_statuses_item)

        defect_statuses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.defect_statuses, Unset):
            if self.defect_statuses is None:
                defect_statuses = None
            else:
                defect_statuses = []
                for defect_statuses_item_data in self.defect_statuses:
                    defect_statuses_item = defect_statuses_item_data.to_dict()

                    defect_statuses.append(defect_statuses_item)

        test_case_statuses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.test_case_statuses, Unset):
            if self.test_case_statuses is None:
                test_case_statuses = None
            else:
                test_case_statuses = []
                for test_case_statuses_item_data in self.test_case_statuses:
                    test_case_statuses_item = test_case_statuses_item_data.to_dict()

                    test_case_statuses.append(test_case_statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if requirement_statuses is not UNSET:
            field_dict["RequirementStatuses"] = requirement_statuses
        if defect_statuses is not UNSET:
            field_dict["DefectStatuses"] = defect_statuses
        if test_case_statuses is not UNSET:
            field_dict["TestCaseStatuses"] = test_case_statuses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_agile_backlog_status import ApiAgileBacklogStatus

        d = src_dict.copy()
        requirement_statuses = []
        _requirement_statuses = d.pop("RequirementStatuses", UNSET)
        for requirement_statuses_item_data in _requirement_statuses or []:
            requirement_statuses_item = ApiAgileBacklogStatus.from_dict(requirement_statuses_item_data)

            requirement_statuses.append(requirement_statuses_item)

        defect_statuses = []
        _defect_statuses = d.pop("DefectStatuses", UNSET)
        for defect_statuses_item_data in _defect_statuses or []:
            defect_statuses_item = ApiAgileBacklogStatus.from_dict(defect_statuses_item_data)

            defect_statuses.append(defect_statuses_item)

        test_case_statuses = []
        _test_case_statuses = d.pop("TestCaseStatuses", UNSET)
        for test_case_statuses_item_data in _test_case_statuses or []:
            test_case_statuses_item = ApiAgileBacklogStatus.from_dict(test_case_statuses_item_data)

            test_case_statuses.append(test_case_statuses_item)

        api_agile_backlog = cls(
            requirement_statuses=requirement_statuses,
            defect_statuses=defect_statuses,
            test_case_statuses=test_case_statuses,
        )

        return api_agile_backlog
