from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_license_type import ApiLicenseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserLicenseAssignmentChangeLicenseTypePatchRequest")


@attr.s(auto_attribs=True)
class ApiUserLicenseAssignmentChangeLicenseTypePatchRequest:
    """
    Attributes:
        operation_type (str):
        new_license_type (Union[Unset, ApiLicenseType]): Identifies the type of the licens.
            This enum has the following values:
              - `Floated` Floated licens.
              - `Named` Named licens.
    """

    operation_type: str
    new_license_type: Union[Unset, ApiLicenseType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        new_license_type: Union[Unset, str] = UNSET
        if not isinstance(self.new_license_type, Unset):
            new_license_type = self.new_license_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if new_license_type is not UNSET:
            field_dict["NewLicenseType"] = new_license_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        _new_license_type = d.pop("NewLicenseType", UNSET)
        new_license_type: Union[Unset, ApiLicenseType]
        if isinstance(_new_license_type, Unset):
            new_license_type = UNSET
        else:
            new_license_type = ApiLicenseType(_new_license_type)

        api_user_license_assignment_change_license_type_patch_request = cls(
            operation_type=operation_type,
            new_license_type=new_license_type,
        )

        api_user_license_assignment_change_license_type_patch_request.additional_properties = d
        return api_user_license_assignment_change_license_type_patch_request

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
