from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLabelAttached")


@attr.s(auto_attribs=True)
class ApiLabelAttached:
    """
    Attributes:
        id (Union[Unset, int]): Id of attached label. Does not reference to global label.
        name (Union[Unset, None, str]): Name of label.
        description (Union[Unset, None, str]): Description of label.
        parent_id (Union[Unset, None, int]): Reference to another attached label.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    parent_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if parent_id is not UNSET:
            field_dict["ParentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        parent_id = d.pop("ParentId", UNSET)

        api_label_attached = cls(
            id=id,
            name=name,
            description=description,
            parent_id=parent_id,
        )

        return api_label_attached
