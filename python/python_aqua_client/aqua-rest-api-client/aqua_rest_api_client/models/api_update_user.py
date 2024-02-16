from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUpdateUser")


@attr.s(auto_attribs=True)
class ApiUpdateUser:
    """
    Attributes:
        user_name (Union[Unset, None, str]): The new username of the user.
        first_name (Union[Unset, None, str]): The new first name of the user.
        surname (Union[Unset, None, str]): The new surname / last name of the user.
        email (Union[Unset, None, str]): The new email address of the user.
        phone (Union[Unset, None, str]): The new phone number of the user.
        position (Union[Unset, None, str]): The new position of the user in the company.
    """

    user_name: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    surname: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        first_name = self.first_name
        surname = self.surname
        email = self.email
        phone = self.phone
        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if surname is not UNSET:
            field_dict["Surname"] = surname
        if email is not UNSET:
            field_dict["Email"] = email
        if phone is not UNSET:
            field_dict["Phone"] = phone
        if position is not UNSET:
            field_dict["Position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("UserName", UNSET)

        first_name = d.pop("FirstName", UNSET)

        surname = d.pop("Surname", UNSET)

        email = d.pop("Email", UNSET)

        phone = d.pop("Phone", UNSET)

        position = d.pop("Position", UNSET)

        api_update_user = cls(
            user_name=user_name,
            first_name=first_name,
            surname=surname,
            email=email,
            phone=phone,
            position=position,
        )

        return api_update_user
