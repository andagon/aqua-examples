from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMyUserInfo")


@attr.s(auto_attribs=True)
class ApiMyUserInfo:
    """
    Attributes:
        id (Union[Unset, int]): The id of the user
        user_name (Union[Unset, None, str]): The username of the user
        first_name (Union[Unset, None, str]): The first name of the user
        surname (Union[Unset, None, str]): The surname / last name of the user
        fullname (Union[Unset, None, str]): The full name of the user. This string is correctly formatted and
            should be used when displaying a user e.g. in a list.
        email (Union[Unset, None, str]): The email address of the user
        phone (Union[Unset, None, str]): The phone number of the user
        position (Union[Unset, None, str]): The position of the user in the company
        picture_url (Union[Unset, None, str]): The absolute url of the user's picture. Might be null, if
            the user does not have a picture assigned.
        customer_id (Union[Unset, int]): The id of the current customer.
        is_first_login (Union[Unset, bool]): Indicates whether this is the first login to aqua
            by the current user.
        server_administrator (Union[Unset, bool]): Indicates if the user is server administrator or not.
        tenant_name (Union[Unset, None, str]): The name of the tenant if the current user has one
        secure_mode_hash (Union[Unset, None, str]): The hash required to securely retrieve LaunchDarkly user variations
    """

    id: Union[Unset, int] = UNSET
    user_name: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    surname: Union[Unset, None, str] = UNSET
    fullname: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, str] = UNSET
    picture_url: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    is_first_login: Union[Unset, bool] = UNSET
    server_administrator: Union[Unset, bool] = UNSET
    tenant_name: Union[Unset, None, str] = UNSET
    secure_mode_hash: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_name = self.user_name
        first_name = self.first_name
        surname = self.surname
        fullname = self.fullname
        email = self.email
        phone = self.phone
        position = self.position
        picture_url = self.picture_url
        customer_id = self.customer_id
        is_first_login = self.is_first_login
        server_administrator = self.server_administrator
        tenant_name = self.tenant_name
        secure_mode_hash = self.secure_mode_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if surname is not UNSET:
            field_dict["Surname"] = surname
        if fullname is not UNSET:
            field_dict["Fullname"] = fullname
        if email is not UNSET:
            field_dict["Email"] = email
        if phone is not UNSET:
            field_dict["Phone"] = phone
        if position is not UNSET:
            field_dict["Position"] = position
        if picture_url is not UNSET:
            field_dict["PictureUrl"] = picture_url
        if customer_id is not UNSET:
            field_dict["CustomerId"] = customer_id
        if is_first_login is not UNSET:
            field_dict["IsFirstLogin"] = is_first_login
        if server_administrator is not UNSET:
            field_dict["ServerAdministrator"] = server_administrator
        if tenant_name is not UNSET:
            field_dict["TenantName"] = tenant_name
        if secure_mode_hash is not UNSET:
            field_dict["SecureModeHash"] = secure_mode_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        user_name = d.pop("UserName", UNSET)

        first_name = d.pop("FirstName", UNSET)

        surname = d.pop("Surname", UNSET)

        fullname = d.pop("Fullname", UNSET)

        email = d.pop("Email", UNSET)

        phone = d.pop("Phone", UNSET)

        position = d.pop("Position", UNSET)

        picture_url = d.pop("PictureUrl", UNSET)

        customer_id = d.pop("CustomerId", UNSET)

        is_first_login = d.pop("IsFirstLogin", UNSET)

        server_administrator = d.pop("ServerAdministrator", UNSET)

        tenant_name = d.pop("TenantName", UNSET)

        secure_mode_hash = d.pop("SecureModeHash", UNSET)

        api_my_user_info = cls(
            id=id,
            user_name=user_name,
            first_name=first_name,
            surname=surname,
            fullname=fullname,
            email=email,
            phone=phone,
            position=position,
            picture_url=picture_url,
            customer_id=customer_id,
            is_first_login=is_first_login,
            server_administrator=server_administrator,
            tenant_name=tenant_name,
            secure_mode_hash=secure_mode_hash,
        )

        api_my_user_info.additional_properties = d
        return api_my_user_info

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
