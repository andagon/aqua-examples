from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_cases_have_steps_response_test_cases import ApiTestCasesHaveStepsResponseTestCases


T = TypeVar("T", bound="ApiTestCasesHaveStepsResponse")


@attr.s(auto_attribs=True)
class ApiTestCasesHaveStepsResponse:
    """Contains an entry for each test case that has steps

    Attributes:
        test_cases (Union[Unset, None, ApiTestCasesHaveStepsResponseTestCases]): The indication if the test case has
            steps. Any missing
            Test Case Ids that were originally provided in the
            input can be assumed to have no steps
    """

    test_cases: Union[Unset, None, "ApiTestCasesHaveStepsResponseTestCases"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        test_cases: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.test_cases, Unset):
            test_cases = self.test_cases.to_dict() if self.test_cases else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if test_cases is not UNSET:
            field_dict["TestCases"] = test_cases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_cases_have_steps_response_test_cases import ApiTestCasesHaveStepsResponseTestCases

        d = src_dict.copy()
        _test_cases = d.pop("TestCases", UNSET)
        test_cases: Union[Unset, None, ApiTestCasesHaveStepsResponseTestCases]
        if _test_cases is None:
            test_cases = None
        elif isinstance(_test_cases, Unset):
            test_cases = UNSET
        else:
            test_cases = ApiTestCasesHaveStepsResponseTestCases.from_dict(_test_cases)

        api_test_cases_have_steps_response = cls(
            test_cases=test_cases,
        )

        return api_test_cases_have_steps_response
