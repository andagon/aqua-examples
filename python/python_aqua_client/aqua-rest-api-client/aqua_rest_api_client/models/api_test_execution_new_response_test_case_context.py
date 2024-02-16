from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_execution_identifier import ApiTestExecutionIdentifier


T = TypeVar("T", bound="ApiTestExecutionNewResponseTestCaseContext")


@attr.s(auto_attribs=True)
class ApiTestExecutionNewResponseTestCaseContext:
    """
    Attributes:
        context (str):
        test_execution_identifier (Union[Unset, None, ApiTestExecutionIdentifier]):
    """

    context: str
    test_execution_identifier: Union[Unset, None, "ApiTestExecutionIdentifier"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context
        test_execution_identifier: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.test_execution_identifier, Unset):
            test_execution_identifier = (
                self.test_execution_identifier.to_dict() if self.test_execution_identifier else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Context": context,
            }
        )
        if test_execution_identifier is not UNSET:
            field_dict["TestExecutionIdentifier"] = test_execution_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_execution_identifier import ApiTestExecutionIdentifier

        d = src_dict.copy()
        context = d.pop("Context")

        _test_execution_identifier = d.pop("TestExecutionIdentifier", UNSET)
        test_execution_identifier: Union[Unset, None, ApiTestExecutionIdentifier]
        if _test_execution_identifier is None:
            test_execution_identifier = None
        elif isinstance(_test_execution_identifier, Unset):
            test_execution_identifier = UNSET
        else:
            test_execution_identifier = ApiTestExecutionIdentifier.from_dict(_test_execution_identifier)

        api_test_execution_new_response_test_case_context = cls(
            context=context,
            test_execution_identifier=test_execution_identifier,
        )

        api_test_execution_new_response_test_case_context.additional_properties = d
        return api_test_execution_new_response_test_case_context

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
