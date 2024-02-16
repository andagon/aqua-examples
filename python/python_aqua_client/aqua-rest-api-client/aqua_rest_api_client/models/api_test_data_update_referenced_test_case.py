from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestDataUpdateReferencedTestCase")


@attr.s(auto_attribs=True)
class ApiTestDataUpdateReferencedTestCase:
    """
    Attributes:
        variant (str):
        referenced_test_case_id (Union[Unset, int]):
    """

    variant: str
    referenced_test_case_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variant = self.variant
        referenced_test_case_id = self.referenced_test_case_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Variant": variant,
            }
        )
        if referenced_test_case_id is not UNSET:
            field_dict["ReferencedTestCaseId"] = referenced_test_case_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        variant = d.pop("Variant")

        referenced_test_case_id = d.pop("ReferencedTestCaseId", UNSET)

        api_test_data_update_referenced_test_case = cls(
            variant=variant,
            referenced_test_case_id=referenced_test_case_id,
        )

        api_test_data_update_referenced_test_case.additional_properties = d
        return api_test_data_update_referenced_test_case

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
