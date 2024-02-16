from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLicenseInfo")


@attr.s(auto_attribs=True)
class ApiLicenseInfo:
    """Represent a license info.

    Attributes:
        name (Union[Unset, None, str]): License file name.
    """

    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        api_license_info = cls(
            name=name,
        )

        return api_license_info
