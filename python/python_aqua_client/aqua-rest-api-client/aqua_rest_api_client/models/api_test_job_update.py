from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_run_dependency_entry import ApiRunDependencyEntry
    from ..models.api_test_job_details_update import ApiTestJobDetailsUpdate


T = TypeVar("T", bound="ApiTestJobUpdate")


@attr.s(auto_attribs=True)
class ApiTestJobUpdate:
    """
    Attributes:
        index_in_test_scenario (int): Index of the test job in test scenario.
        run_dependency (Union[Unset, None, List['ApiRunDependencyEntry']]): The list of run dependencies of this test
            job.
        details (Union[Unset, None, ApiTestJobDetailsUpdate]): Contains the details of the test job which should be
            updated.
    """

    index_in_test_scenario: int
    run_dependency: Union[Unset, None, List["ApiRunDependencyEntry"]] = UNSET
    details: Union[Unset, None, "ApiTestJobDetailsUpdate"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        index_in_test_scenario = self.index_in_test_scenario
        run_dependency: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.run_dependency, Unset):
            if self.run_dependency is None:
                run_dependency = None
            else:
                run_dependency = []
                for run_dependency_item_data in self.run_dependency:
                    run_dependency_item = run_dependency_item_data.to_dict()

                    run_dependency.append(run_dependency_item)

        details: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict() if self.details else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "IndexInTestScenario": index_in_test_scenario,
            }
        )
        if run_dependency is not UNSET:
            field_dict["RunDependency"] = run_dependency
        if details is not UNSET:
            field_dict["Details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_run_dependency_entry import ApiRunDependencyEntry
        from ..models.api_test_job_details_update import ApiTestJobDetailsUpdate

        d = src_dict.copy()
        index_in_test_scenario = d.pop("IndexInTestScenario")

        run_dependency = []
        _run_dependency = d.pop("RunDependency", UNSET)
        for run_dependency_item_data in _run_dependency or []:
            run_dependency_item = ApiRunDependencyEntry.from_dict(run_dependency_item_data)

            run_dependency.append(run_dependency_item)

        _details = d.pop("Details", UNSET)
        details: Union[Unset, None, ApiTestJobDetailsUpdate]
        if _details is None:
            details = None
        elif isinstance(_details, Unset):
            details = UNSET
        else:
            details = ApiTestJobDetailsUpdate.from_dict(_details)

        api_test_job_update = cls(
            index_in_test_scenario=index_in_test_scenario,
            run_dependency=run_dependency,
            details=details,
        )

        return api_test_job_update
