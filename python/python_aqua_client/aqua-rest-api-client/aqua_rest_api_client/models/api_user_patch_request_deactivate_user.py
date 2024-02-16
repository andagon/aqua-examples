from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiUserPatchRequestDeactivateUser")


@attr.s(auto_attribs=True)
class ApiUserPatchRequestDeactivateUser:
    """
    Attributes:
        operation_type (str):
    """

    operation_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        api_user_patch_request_deactivate_user = cls(
            operation_type=operation_type,
        )

        api_user_patch_request_deactivate_user.additional_properties = d
        return api_user_patch_request_deactivate_user

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
