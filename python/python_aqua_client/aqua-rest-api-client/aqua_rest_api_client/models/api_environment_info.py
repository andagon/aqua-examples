from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEnvironmentInfo")


@attr.s(auto_attribs=True)
class ApiEnvironmentInfo:
    """Provides information about a system environment

    Attributes:
        is_multi_tenant (Union[Unset, bool]): Multitenant environment is used
    """

    is_multi_tenant: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_multi_tenant = self.is_multi_tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_multi_tenant is not UNSET:
            field_dict["IsMultiTenant"] = is_multi_tenant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_multi_tenant = d.pop("IsMultiTenant", UNSET)

        api_environment_info = cls(
            is_multi_tenant=is_multi_tenant,
        )

        return api_environment_info
