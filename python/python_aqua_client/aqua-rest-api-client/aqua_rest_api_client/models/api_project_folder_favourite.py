from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_location import ApiItemLocation


T = TypeVar("T", bound="ApiProjectFolderFavourite")


@attr.s(auto_attribs=True)
class ApiProjectFolderFavourite:
    """Represents a folder favourite.

    Attributes:
        id (Union[Unset, int]): Id of the record.
        location (Union[Unset, None, ApiItemLocation]): Specifies the location (project and folder) of an item
        label (Union[Unset, None, str]): Custom label of this folder favorite.
    """

    id: Union[Unset, int] = UNSET
    location: Union[Unset, None, "ApiItemLocation"] = UNSET
    label: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if location is not UNSET:
            field_dict["Location"] = location
        if label is not UNSET:
            field_dict["Label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_location import ApiItemLocation

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _location = d.pop("Location", UNSET)
        location: Union[Unset, None, ApiItemLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = ApiItemLocation.from_dict(_location)

        label = d.pop("Label", UNSET)

        api_project_folder_favourite = cls(
            id=id,
            location=location,
            label=label,
        )

        return api_project_folder_favourite
