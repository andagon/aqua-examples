from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLabelInfo")


@attr.s(auto_attribs=True)
class ApiLabelInfo:
    """Minimal version of a label.

    Attributes:
        id (Union[Unset, int]): Id of this label.
        version (Union[Unset, int]): Label version.
    """

    id: Union[Unset, int] = UNSET
    version: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if version is not UNSET:
            field_dict["Version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        version = d.pop("Version", UNSET)

        api_label_info = cls(
            id=id,
            version=version,
        )

        return api_label_info
