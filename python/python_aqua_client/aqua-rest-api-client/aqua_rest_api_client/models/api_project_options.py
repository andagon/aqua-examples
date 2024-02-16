from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectOptions")


@attr.s(auto_attribs=True)
class ApiProjectOptions:
    """Represents options of a certain project.

    Attributes:
        require_expected_results (Union[Unset, bool]): If set, then 'Expected Results' field is mandatory when defining
            a test case.
        require_actual_results (Union[Unset, bool]): If set, then 'Actual Results' field is mandatory when manually
            executing a test case.
    """

    require_expected_results: Union[Unset, bool] = UNSET
    require_actual_results: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        require_expected_results = self.require_expected_results
        require_actual_results = self.require_actual_results

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if require_expected_results is not UNSET:
            field_dict["RequireExpectedResults"] = require_expected_results
        if require_actual_results is not UNSET:
            field_dict["RequireActualResults"] = require_actual_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        require_expected_results = d.pop("RequireExpectedResults", UNSET)

        require_actual_results = d.pop("RequireActualResults", UNSET)

        api_project_options = cls(
            require_expected_results=require_expected_results,
            require_actual_results=require_actual_results,
        )

        return api_project_options
