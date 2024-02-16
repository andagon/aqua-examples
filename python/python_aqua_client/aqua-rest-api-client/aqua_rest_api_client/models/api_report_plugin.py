from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportPlugin")


@attr.s(auto_attribs=True)
class ApiReportPlugin:
    """Represents a report plugin.

    Attributes:
        unique_code (Union[Unset, None, str]): Unique code of this report plugin.
        name (Union[Unset, None, str]): Name of the plugin.
        description (Union[Unset, None, str]): Plugin description (can be empty)
    """

    unique_code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        unique_code = self.unique_code
        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if unique_code is not UNSET:
            field_dict["UniqueCode"] = unique_code
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unique_code = d.pop("UniqueCode", UNSET)

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        api_report_plugin = cls(
            unique_code=unique_code,
            name=name,
            description=description,
        )

        return api_report_plugin
