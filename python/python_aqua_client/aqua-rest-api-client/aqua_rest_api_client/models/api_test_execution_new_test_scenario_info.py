from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_run_dependency_entry import ApiRunDependencyEntry


T = TypeVar("T", bound="ApiTestExecutionNewTestScenarioInfo")


@attr.s(auto_attribs=True)
class ApiTestExecutionNewTestScenarioInfo:
    """Contains information specific for the execution
    in scope of a test scenario.

        Attributes:
            index (Union[Unset, int]): The index of this execution in the test scenario
                execution. The index does not need to be consecutive as partial
                execution of a test scenario is allowed.
            run_dependency (Union[Unset, None, List['ApiRunDependencyEntry']]): The run dependencies for this execution. The
                run dependencies
                can be defined freely here but are enforced afterwards by the UI
                when updating the execution.
            test_scenario_id (Union[Unset, int]): The id of the test scenario in scope of which this execution
                is performed.
            test_job_id (Union[Unset, None, int]): The id of the test job to which this execution belongs. This id is
                optional
                and ids which do not exist anymore will be silently dropped. A valid id needs
                to be provided when the last execution information for a test job should be
                updated.
    """

    index: Union[Unset, int] = UNSET
    run_dependency: Union[Unset, None, List["ApiRunDependencyEntry"]] = UNSET
    test_scenario_id: Union[Unset, int] = UNSET
    test_job_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        run_dependency: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.run_dependency, Unset):
            if self.run_dependency is None:
                run_dependency = None
            else:
                run_dependency = []
                for run_dependency_item_data in self.run_dependency:
                    run_dependency_item = run_dependency_item_data.to_dict()

                    run_dependency.append(run_dependency_item)

        test_scenario_id = self.test_scenario_id
        test_job_id = self.test_job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["Index"] = index
        if run_dependency is not UNSET:
            field_dict["RunDependency"] = run_dependency
        if test_scenario_id is not UNSET:
            field_dict["TestScenarioId"] = test_scenario_id
        if test_job_id is not UNSET:
            field_dict["TestJobId"] = test_job_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_run_dependency_entry import ApiRunDependencyEntry

        d = src_dict.copy()
        index = d.pop("Index", UNSET)

        run_dependency = []
        _run_dependency = d.pop("RunDependency", UNSET)
        for run_dependency_item_data in _run_dependency or []:
            run_dependency_item = ApiRunDependencyEntry.from_dict(run_dependency_item_data)

            run_dependency.append(run_dependency_item)

        test_scenario_id = d.pop("TestScenarioId", UNSET)

        test_job_id = d.pop("TestJobId", UNSET)

        api_test_execution_new_test_scenario_info = cls(
            index=index,
            run_dependency=run_dependency,
            test_scenario_id=test_scenario_id,
            test_job_id=test_job_id,
        )

        return api_test_execution_new_test_scenario_info
