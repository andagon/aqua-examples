from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSprintStatistic")


@attr.s(auto_attribs=True)
class ApiSprintStatistic:
    """Contains statistics, count of the assigned items, by the item type.

    Attributes:
        count_defects (Union[Unset, int]): Count of assigned defects.
        count_requirements (Union[Unset, int]): Count of assigned requirements.
        count_test_cases (Union[Unset, int]): Count of assigned test cases.
        count_test_scenarios (Union[Unset, int]): Count of assigned test scenarios.
        count_scripts (Union[Unset, int]): Count of assigned scripts.
    """

    count_defects: Union[Unset, int] = UNSET
    count_requirements: Union[Unset, int] = UNSET
    count_test_cases: Union[Unset, int] = UNSET
    count_test_scenarios: Union[Unset, int] = UNSET
    count_scripts: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        count_defects = self.count_defects
        count_requirements = self.count_requirements
        count_test_cases = self.count_test_cases
        count_test_scenarios = self.count_test_scenarios
        count_scripts = self.count_scripts

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if count_defects is not UNSET:
            field_dict["CountDefects"] = count_defects
        if count_requirements is not UNSET:
            field_dict["CountRequirements"] = count_requirements
        if count_test_cases is not UNSET:
            field_dict["CountTestCases"] = count_test_cases
        if count_test_scenarios is not UNSET:
            field_dict["CountTestScenarios"] = count_test_scenarios
        if count_scripts is not UNSET:
            field_dict["CountScripts"] = count_scripts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count_defects = d.pop("CountDefects", UNSET)

        count_requirements = d.pop("CountRequirements", UNSET)

        count_test_cases = d.pop("CountTestCases", UNSET)

        count_test_scenarios = d.pop("CountTestScenarios", UNSET)

        count_scripts = d.pop("CountScripts", UNSET)

        api_sprint_statistic = cls(
            count_defects=count_defects,
            count_requirements=count_requirements,
            count_test_cases=count_test_cases,
            count_test_scenarios=count_test_scenarios,
            count_scripts=count_scripts,
        )

        return api_sprint_statistic
