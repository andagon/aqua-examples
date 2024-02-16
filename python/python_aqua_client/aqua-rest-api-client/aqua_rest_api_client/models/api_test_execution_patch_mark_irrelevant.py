from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestExecutionPatchMarkIrrelevant")


@attr.s(auto_attribs=True)
class ApiTestExecutionPatchMarkIrrelevant:
    """
    Attributes:
        patch_type (str):
        test_executions_ids (Union[Unset, None, List[int]]): The list of test executions ids which will be modified.
        irrelevant_reason (Union[Unset, None, str]): The reason for marking the test executions irrelevant.
    """

    patch_type: str
    test_executions_ids: Union[Unset, None, List[int]] = UNSET
    irrelevant_reason: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_type = self.patch_type
        test_executions_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.test_executions_ids, Unset):
            if self.test_executions_ids is None:
                test_executions_ids = None
            else:
                test_executions_ids = self.test_executions_ids

        irrelevant_reason = self.irrelevant_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PatchType": patch_type,
            }
        )
        if test_executions_ids is not UNSET:
            field_dict["TestExecutionsIds"] = test_executions_ids
        if irrelevant_reason is not UNSET:
            field_dict["IrrelevantReason"] = irrelevant_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_type = d.pop("PatchType")

        test_executions_ids = cast(List[int], d.pop("TestExecutionsIds", UNSET))

        irrelevant_reason = d.pop("IrrelevantReason", UNSET)

        api_test_execution_patch_mark_irrelevant = cls(
            patch_type=patch_type,
            test_executions_ids=test_executions_ids,
            irrelevant_reason=irrelevant_reason,
        )

        api_test_execution_patch_mark_irrelevant.additional_properties = d
        return api_test_execution_patch_mark_irrelevant

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
