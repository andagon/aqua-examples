from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiUserViewPatchCollectionResponse")


@attr.s(auto_attribs=True)
class ApiUserViewPatchCollectionResponse:
    """Represent the response for the user view patch collection operation."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        api_user_view_patch_collection_response = cls()

        return api_user_view_patch_collection_response
