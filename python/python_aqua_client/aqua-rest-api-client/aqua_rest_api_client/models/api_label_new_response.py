from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLabelNewResponse")


@attr.s(auto_attribs=True)
class ApiLabelNewResponse:
    """Represents a newly created label.

    Attributes:
        id (Union[Unset, int]): Id of this label.
    """

    id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        api_label_new_response = cls(
            id=id,
        )

        return api_label_new_response
