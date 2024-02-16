from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiTestExecutionNewResponse")


@attr.s(auto_attribs=True)
class ApiTestExecutionNewResponse:
    """Represents the response for creating new execution, the response depends on the execution context.

    Attributes:
        context (str):
    """

    context: str

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Context": context,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("Context")

        api_test_execution_new_response = cls(
            context=context,
        )

        return api_test_execution_new_response
