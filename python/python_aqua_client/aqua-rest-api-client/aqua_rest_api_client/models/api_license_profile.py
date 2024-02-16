from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLicenseProfile")


@attr.s(auto_attribs=True)
class ApiLicenseProfile:
    """
    Attributes:
        profile_code (Union[Unset, None, str]): The code of the license profile
        profile_name (Union[Unset, None, str]): The name of the license profile
        named_total (Union[Unset, int]): The maximal number of named licenses.
        floating_total (Union[Unset, int]): The maximal number of floating licenses.
        named_used (Union[Unset, int]): The used number of named licenses.
        floating_used (Union[Unset, int]): The used number of floating licenses.
    """

    profile_code: Union[Unset, None, str] = UNSET
    profile_name: Union[Unset, None, str] = UNSET
    named_total: Union[Unset, int] = UNSET
    floating_total: Union[Unset, int] = UNSET
    named_used: Union[Unset, int] = UNSET
    floating_used: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_code = self.profile_code
        profile_name = self.profile_name
        named_total = self.named_total
        floating_total = self.floating_total
        named_used = self.named_used
        floating_used = self.floating_used

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if profile_code is not UNSET:
            field_dict["ProfileCode"] = profile_code
        if profile_name is not UNSET:
            field_dict["ProfileName"] = profile_name
        if named_total is not UNSET:
            field_dict["NamedTotal"] = named_total
        if floating_total is not UNSET:
            field_dict["FloatingTotal"] = floating_total
        if named_used is not UNSET:
            field_dict["NamedUsed"] = named_used
        if floating_used is not UNSET:
            field_dict["FloatingUsed"] = floating_used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        profile_code = d.pop("ProfileCode", UNSET)

        profile_name = d.pop("ProfileName", UNSET)

        named_total = d.pop("NamedTotal", UNSET)

        floating_total = d.pop("FloatingTotal", UNSET)

        named_used = d.pop("NamedUsed", UNSET)

        floating_used = d.pop("FloatingUsed", UNSET)

        api_license_profile = cls(
            profile_code=profile_code,
            profile_name=profile_name,
            named_total=named_total,
            floating_total=floating_total,
            named_used=named_used,
            floating_used=floating_used,
        )

        return api_license_profile
