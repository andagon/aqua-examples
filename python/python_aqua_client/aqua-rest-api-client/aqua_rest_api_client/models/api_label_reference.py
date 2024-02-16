from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLabelReference")


@attr.s(auto_attribs=True)
class ApiLabelReference:
    """Reference to a label. Contains minimal informations. Used for attaching labels to elements,
    retaining information about the global label and changing accordingly.

        Attributes:
            id (Union[Unset, int]): Id of this label.
            name (Union[Unset, None, str]): Name of this label.
            is_super_label (Union[Unset, bool]): Flag to indicate that this label has sub-labels.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    is_super_label: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        is_super_label = self.is_super_label

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if is_super_label is not UNSET:
            field_dict["IsSuperLabel"] = is_super_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        is_super_label = d.pop("IsSuperLabel", UNSET)

        api_label_reference = cls(
            id=id,
            name=name,
            is_super_label=is_super_label,
        )

        return api_label_reference
