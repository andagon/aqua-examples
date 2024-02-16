from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_object_report_allowed_options_update import ApiBaseObjectReportAllowedOptionsUpdate


T = TypeVar("T", bound="ApiReportOptionsUpdate")


@attr.s(auto_attribs=True)
class ApiReportOptionsUpdate:
    """Represents updated report options.

    Attributes:
        name (Union[Unset, None, str]): The report's name.
        color (Union[Unset, None, str]): The report's color.
            Allowed are only predefined colors, for more information see: [Get predefined
            colors](#operation/System_GetColors).
        plugin_code (Union[Unset, None, str]): Code of report plugin to be used (if any).
        allowed_options (Union[Unset, None, List['ApiBaseObjectReportAllowedOptionsUpdate']]): List of allowed options.
            Include options for all desired object types.
            Object types not found will be removed from report.
    """

    name: Union[Unset, None, str] = UNSET
    color: Union[Unset, None, str] = UNSET
    plugin_code: Union[Unset, None, str] = UNSET
    allowed_options: Union[Unset, None, List["ApiBaseObjectReportAllowedOptionsUpdate"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        color = self.color
        plugin_code = self.plugin_code
        allowed_options: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.allowed_options, Unset):
            if self.allowed_options is None:
                allowed_options = None
            else:
                allowed_options = []
                for allowed_options_item_data in self.allowed_options:
                    allowed_options_item = allowed_options_item_data.to_dict()

                    allowed_options.append(allowed_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if color is not UNSET:
            field_dict["Color"] = color
        if plugin_code is not UNSET:
            field_dict["PluginCode"] = plugin_code
        if allowed_options is not UNSET:
            field_dict["AllowedOptions"] = allowed_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_object_report_allowed_options_update import ApiBaseObjectReportAllowedOptionsUpdate

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        color = d.pop("Color", UNSET)

        plugin_code = d.pop("PluginCode", UNSET)

        allowed_options = []
        _allowed_options = d.pop("AllowedOptions", UNSET)
        for allowed_options_item_data in _allowed_options or []:
            allowed_options_item = ApiBaseObjectReportAllowedOptionsUpdate.from_dict(allowed_options_item_data)

            allowed_options.append(allowed_options_item)

        api_report_options_update = cls(
            name=name,
            color=color,
            plugin_code=plugin_code,
            allowed_options=allowed_options,
        )

        return api_report_options_update
