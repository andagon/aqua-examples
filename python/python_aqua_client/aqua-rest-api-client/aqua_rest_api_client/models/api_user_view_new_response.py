from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserViewNewResponse")


@attr.s(auto_attribs=True)
class ApiUserViewNewResponse:
    """Contains information about created user view.

    Attributes:
        user_view_id (Union[Unset, int]): The id of the user view.
    """

    user_view_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_view_id = self.user_view_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_view_id is not UNSET:
            field_dict["UserViewId"] = user_view_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_view_id = d.pop("UserViewId", UNSET)

        api_user_view_new_response = cls(
            user_view_id=user_view_id,
        )

        return api_user_view_new_response
