from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistoryScriptFileModified")


@attr.s(auto_attribs=True)
class ApiHistoryScriptFileModified:
    """Changes to the script.

    Attributes:
        file_name (Union[Unset, None, str]): The name of the File, is empty if script is changed directly.
        value_before (Union[Unset, None, str]): The old value before the change, is empty if file changed.
        value_after (Union[Unset, None, str]): The new value after the change, is empty if file changed.
    """

    file_name: Union[Unset, None, str] = UNSET
    value_before: Union[Unset, None, str] = UNSET
    value_after: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name
        value_before = self.value_before
        value_after = self.value_after

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["FileName"] = file_name
        if value_before is not UNSET:
            field_dict["ValueBefore"] = value_before
        if value_after is not UNSET:
            field_dict["ValueAfter"] = value_after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_name = d.pop("FileName", UNSET)

        value_before = d.pop("ValueBefore", UNSET)

        value_after = d.pop("ValueAfter", UNSET)

        api_history_script_file_modified = cls(
            file_name=file_name,
            value_before=value_before,
            value_after=value_after,
        )

        return api_history_script_file_modified
