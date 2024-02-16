from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAddSingleTestStepResponse")


@attr.s(auto_attribs=True)
class ApiAddSingleTestStepResponse:
    """Contains information about created test step.

    Attributes:
        test_step_id (Union[Unset, int]): The id of the test step.
    """

    test_step_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        test_step_id = self.test_step_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if test_step_id is not UNSET:
            field_dict["TestStepId"] = test_step_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        test_step_id = d.pop("TestStepId", UNSET)

        api_add_single_test_step_response = cls(
            test_step_id=test_step_id,
        )

        return api_add_single_test_step_response
