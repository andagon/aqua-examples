from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiResetPasswordUser")


@attr.s(auto_attribs=True)
class ApiResetPasswordUser:
    """Contains info about user who is resetting the password

    Attributes:
        email (Union[Unset, None, str]): User's email
        tenant (Union[Unset, None, str]): User's tenant
    """

    email: Union[Unset, None, str] = UNSET
    tenant: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        tenant = self.tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if email is not UNSET:
            field_dict["Email"] = email
        if tenant is not UNSET:
            field_dict["Tenant"] = tenant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("Email", UNSET)

        tenant = d.pop("Tenant", UNSET)

        api_reset_password_user = cls(
            email=email,
            tenant=tenant,
        )

        return api_reset_password_user
