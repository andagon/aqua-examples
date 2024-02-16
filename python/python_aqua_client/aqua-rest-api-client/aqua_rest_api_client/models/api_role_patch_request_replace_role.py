from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRolePatchRequestReplaceRole")


@attr.s(auto_attribs=True)
class ApiRolePatchRequestReplaceRole:
    """
    Attributes:
        operation_type (str):
        role_id_to_replace_with (Union[Unset, int]): The id of the role which should be set.
    """

    operation_type: str
    role_id_to_replace_with: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        role_id_to_replace_with = self.role_id_to_replace_with

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if role_id_to_replace_with is not UNSET:
            field_dict["RoleIdToReplaceWith"] = role_id_to_replace_with

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        role_id_to_replace_with = d.pop("RoleIdToReplaceWith", UNSET)

        api_role_patch_request_replace_role = cls(
            operation_type=operation_type,
            role_id_to_replace_with=role_id_to_replace_with,
        )

        api_role_patch_request_replace_role.additional_properties = d
        return api_role_patch_request_replace_role

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
