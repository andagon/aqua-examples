from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRegisteredFileEditor")


@attr.s(auto_attribs=True)
class ApiRegisteredFileEditor:
    """Contains meta-data of the registered file editor (used in automation).

    Attributes:
        file_extension (Union[Unset, None, str]): Extension of the files supported by this editor (e.g. "cvs")
        key (Union[Unset, None, str]): Unique key to identify the registered editor. For example 'CSV'.
        js_controller_name (Union[Unset, None, str]): Name of the javascript object that implements functionality of
            this editor.
            (the proper javascript file needs to be injected/evaluated in order to access the editor code).
        icon_16 (Union[Unset, None, str]): Small icon representing the editor/file type.
            Contains Base64 encoded PNG bytes to be used with 'data:image/png;base64,'
        icon_32 (Union[Unset, None, str]): Large icon representing the editor/file type.
            Contains Base64 encoded PNG bytes to be used with 'data:image/png;base64,'
    """

    file_extension: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    js_controller_name: Union[Unset, None, str] = UNSET
    icon_16: Union[Unset, None, str] = UNSET
    icon_32: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        file_extension = self.file_extension
        key = self.key
        js_controller_name = self.js_controller_name
        icon_16 = self.icon_16
        icon_32 = self.icon_32

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if file_extension is not UNSET:
            field_dict["FileExtension"] = file_extension
        if key is not UNSET:
            field_dict["Key"] = key
        if js_controller_name is not UNSET:
            field_dict["JSControllerName"] = js_controller_name
        if icon_16 is not UNSET:
            field_dict["Icon16"] = icon_16
        if icon_32 is not UNSET:
            field_dict["Icon32"] = icon_32

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_extension = d.pop("FileExtension", UNSET)

        key = d.pop("Key", UNSET)

        js_controller_name = d.pop("JSControllerName", UNSET)

        icon_16 = d.pop("Icon16", UNSET)

        icon_32 = d.pop("Icon32", UNSET)

        api_registered_file_editor = cls(
            file_extension=file_extension,
            key=key,
            js_controller_name=js_controller_name,
            icon_16=icon_16,
            icon_32=icon_32,
        )

        return api_registered_file_editor
