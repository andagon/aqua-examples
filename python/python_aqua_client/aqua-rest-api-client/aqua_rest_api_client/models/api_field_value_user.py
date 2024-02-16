from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiFieldValueUser")


@attr.s(auto_attribs=True)
class ApiFieldValueUser:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
        id (Union[Unset, int]): The id of the user.
        user_info (Union[Unset, None, ApiUserInfo]): The user information
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    user_info: Union[Unset, None, "ApiUserInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text
        id = self.id
        user_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = self.user_info.to_dict() if self.user_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldValueType": field_value_type,
            }
        )
        if text is not UNSET:
            field_dict["Text"] = text
        if id is not UNSET:
            field_dict["Id"] = id
        if user_info is not UNSET:
            field_dict["UserInfo"] = user_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        field_value_type = d.pop("FieldValueType")

        text = d.pop("Text", UNSET)

        id = d.pop("Id", UNSET)

        _user_info = d.pop("UserInfo", UNSET)
        user_info: Union[Unset, None, ApiUserInfo]
        if _user_info is None:
            user_info = None
        elif isinstance(_user_info, Unset):
            user_info = UNSET
        else:
            user_info = ApiUserInfo.from_dict(_user_info)

        api_field_value_user = cls(
            field_value_type=field_value_type,
            text=text,
            id=id,
            user_info=user_info,
        )

        api_field_value_user.additional_properties = d
        return api_field_value_user

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
