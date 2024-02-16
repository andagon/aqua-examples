from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiIntegrationVerifyResponse")


@attr.s(auto_attribs=True)
class ApiIntegrationVerifyResponse:
    """The verification response

    Attributes:
        is_success (Union[Unset, bool]): True if the connection succeeded
    """

    is_success: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_success = self.is_success

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_success is not UNSET:
            field_dict["IsSuccess"] = is_success

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_success = d.pop("IsSuccess", UNSET)

        api_integration_verify_response = cls(
            is_success=is_success,
        )

        return api_integration_verify_response
