from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestScenarioExecutionPreviewRequest")


@attr.s(auto_attribs=True)
class ApiTestScenarioExecutionPreviewRequest:
    """Represents the test scenario execution preview request.

    Attributes:
        tested_version (Union[Unset, None, str]): Tested version, is only used if test job tested version is not set.
        test_job_ids (Union[Unset, None, List[int]]): List of test job ids.
    """

    tested_version: Union[Unset, None, str] = UNSET
    test_job_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tested_version = self.tested_version
        test_job_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.test_job_ids, Unset):
            if self.test_job_ids is None:
                test_job_ids = None
            else:
                test_job_ids = self.test_job_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if test_job_ids is not UNSET:
            field_dict["TestJobIds"] = test_job_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tested_version = d.pop("TestedVersion", UNSET)

        test_job_ids = cast(List[int], d.pop("TestJobIds", UNSET))

        api_test_scenario_execution_preview_request = cls(
            tested_version=tested_version,
            test_job_ids=test_job_ids,
        )

        return api_test_scenario_execution_preview_request
