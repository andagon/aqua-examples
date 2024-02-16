from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_license_profile_utilization import ApiLicenseProfileUtilization
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLicenseProfileUtilizationInfo")


@attr.s(auto_attribs=True)
class ApiLicenseProfileUtilizationInfo:
    """
    Attributes:
        utilization (Union[Unset, ApiLicenseProfileUtilization]):
            This enum has the following values:
              - `FloatingLicenseNotAvailable` Floating license active, but no more instances available.
              - `LicenseGranted` License was granted.

              - `NoValidLicense` No active license.
              - `ProfileDeactivatedByLicense` License active, but profile assignment was deactivated by license.
        profile_code (Union[Unset, None, str]):
        as_floating (Union[Unset, bool]):
    """

    utilization: Union[Unset, ApiLicenseProfileUtilization] = UNSET
    profile_code: Union[Unset, None, str] = UNSET
    as_floating: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        utilization: Union[Unset, str] = UNSET
        if not isinstance(self.utilization, Unset):
            utilization = self.utilization.value

        profile_code = self.profile_code
        as_floating = self.as_floating

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if utilization is not UNSET:
            field_dict["Utilization"] = utilization
        if profile_code is not UNSET:
            field_dict["ProfileCode"] = profile_code
        if as_floating is not UNSET:
            field_dict["AsFloating"] = as_floating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _utilization = d.pop("Utilization", UNSET)
        utilization: Union[Unset, ApiLicenseProfileUtilization]
        if isinstance(_utilization, Unset):
            utilization = UNSET
        else:
            utilization = ApiLicenseProfileUtilization(_utilization)

        profile_code = d.pop("ProfileCode", UNSET)

        as_floating = d.pop("AsFloating", UNSET)

        api_license_profile_utilization_info = cls(
            utilization=utilization,
            profile_code=profile_code,
            as_floating=as_floating,
        )

        return api_license_profile_utilization_info
