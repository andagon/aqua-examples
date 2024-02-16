from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiResetPasswordResult")


@attr.s(auto_attribs=True)
class ApiResetPasswordResult:
    """Provides information about the result of resetting a user's password

    Attributes:
        is_success (Union[Unset, bool]): Result about resetting for users
        message (Union[Unset, None, str]): Info about resetting for users
    """

    is_success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_success = self.is_success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_success is not UNSET:
            field_dict["IsSuccess"] = is_success
        if message is not UNSET:
            field_dict["Message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_success = d.pop("IsSuccess", UNSET)

        message = d.pop("Message", UNSET)

        api_reset_password_result = cls(
            is_success=is_success,
            message=message,
        )

        return api_reset_password_result
