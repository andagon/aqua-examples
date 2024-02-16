from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestExecutionPatchRequest")


@attr.s(auto_attribs=True)
class ApiTestExecutionPatchRequest:
    """Represents the test execution patch request.

    Attributes:
        patch_type (str):
        test_executions_ids (Union[Unset, None, List[int]]): The list of test executions ids which will be modified.
    """

    patch_type: str
    test_executions_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        patch_type = self.patch_type
        test_executions_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.test_executions_ids, Unset):
            if self.test_executions_ids is None:
                test_executions_ids = None
            else:
                test_executions_ids = self.test_executions_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "PatchType": patch_type,
            }
        )
        if test_executions_ids is not UNSET:
            field_dict["TestExecutionsIds"] = test_executions_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_type = d.pop("PatchType")

        test_executions_ids = cast(List[int], d.pop("TestExecutionsIds", UNSET))

        api_test_execution_patch_request = cls(
            patch_type=patch_type,
            test_executions_ids=test_executions_ids,
        )

        return api_test_execution_patch_request
