from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserPatchRequestSetUserPassword")


@attr.s(auto_attribs=True)
class ApiUserPatchRequestSetUserPassword:
    """
    Attributes:
        operation_type (str):
        new_password (Union[Unset, None, str]): New user password.
    """

    operation_type: str
    new_password: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        new_password = self.new_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if new_password is not UNSET:
            field_dict["NewPassword"] = new_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        new_password = d.pop("NewPassword", UNSET)

        api_user_patch_request_set_user_password = cls(
            operation_type=operation_type,
            new_password=new_password,
        )

        api_user_patch_request_set_user_password.additional_properties = d
        return api_user_patch_request_set_user_password

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
