from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserInfo")


@attr.s(auto_attribs=True)
class ApiUserInfo:
    """The user information

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

        field_dict: Dict[str, Any] = {}
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

        api_user_info = cls(
            id=id,
            user_name=user_name,
            first_name=first_name,
            surname=surname,
            fullname=fullname,
            email=email,
            phone=phone,
            position=position,
            picture_url=picture_url,
        )

        return api_user_info
