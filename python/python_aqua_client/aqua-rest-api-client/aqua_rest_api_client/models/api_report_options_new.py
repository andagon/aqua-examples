from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_object_report_allowed_options_update import ApiBaseObjectReportAllowedOptionsUpdate


T = TypeVar("T", bound="ApiReportOptionsNew")


@attr.s(auto_attribs=True)
class ApiReportOptionsNew:
    """Represents new report options.

    Attributes:
        name (str): The report's name.
        color (str): The report's color.
            Allowed are only predefined colors, for more information see: [Get predefined
            colors](#operation/System_GetColors).
        allowed_options (List['ApiBaseObjectReportAllowedOptionsUpdate']): List of allowed options.
        plugin_code (Union[Unset, None, str]): Code of report plugin to be used (if any).
    """

    name: str
    color: str
    allowed_options: List["ApiBaseObjectReportAllowedOptionsUpdate"]
    plugin_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        color = self.color
        allowed_options = []
        for allowed_options_item_data in self.allowed_options:
            allowed_options_item = allowed_options_item_data.to_dict()

            allowed_options.append(allowed_options_item)

        plugin_code = self.plugin_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Name": name,
                "Color": color,
                "AllowedOptions": allowed_options,
            }
        )
        if plugin_code is not UNSET:
            field_dict["PluginCode"] = plugin_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_object_report_allowed_options_update import ApiBaseObjectReportAllowedOptionsUpdate

        d = src_dict.copy()
        name = d.pop("Name")

        color = d.pop("Color")

        allowed_options = []
        _allowed_options = d.pop("AllowedOptions")
        for allowed_options_item_data in _allowed_options:
            allowed_options_item = ApiBaseObjectReportAllowedOptionsUpdate.from_dict(allowed_options_item_data)

            allowed_options.append(allowed_options_item)

        plugin_code = d.pop("PluginCode", UNSET)

        api_report_options_new = cls(
            name=name,
            color=color,
            allowed_options=allowed_options,
            plugin_code=plugin_code,
        )

        return api_report_options_new
