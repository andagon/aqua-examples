from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_license_type import ApiLicenseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserLicenseAssignment")


@attr.s(auto_attribs=True)
class ApiUserLicenseAssignment:
    """The user license assignment information.

    Attributes:
        code (Union[Unset, None, str]): The code of the license.
        type (Union[Unset, ApiLicenseType]): Identifies the type of the licens.
            This enum has the following values:
              - `Floated` Floated licens.
              - `Named` Named licens.
    """

    code: Union[Unset, None, str] = UNSET
    type: Union[Unset, ApiLicenseType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if code is not UNSET:
            field_dict["Code"] = code
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("Code", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiLicenseType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiLicenseType(_type)

        api_user_license_assignment = cls(
            code=code,
            type=type,
        )

        return api_user_license_assignment
