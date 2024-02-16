from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_automation_attached_script_file_info import ApiAutomationAttachedScriptFileInfo


T = TypeVar("T", bound="ApiAutomationScriptUnixShell")


@attr.s(auto_attribs=True)
class ApiAutomationScriptUnixShell:
    """
    Attributes:
        technology (str):
        attached_files (Union[Unset, None, List['ApiAutomationAttachedScriptFileInfo']]): A list of attached files.
        script_content (Union[Unset, None, str]): Script content.
        profile (Union[Unset, None, str]): Code of shell profile to be used (if any)
    """

    technology: str
    attached_files: Union[Unset, None, List["ApiAutomationAttachedScriptFileInfo"]] = UNSET
    script_content: Union[Unset, None, str] = UNSET
    profile: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        technology = self.technology
        attached_files: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attached_files, Unset):
            if self.attached_files is None:
                attached_files = None
            else:
                attached_files = []
                for attached_files_item_data in self.attached_files:
                    attached_files_item = attached_files_item_data.to_dict()

                    attached_files.append(attached_files_item)

        script_content = self.script_content
        profile = self.profile

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Technology": technology,
            }
        )
        if attached_files is not UNSET:
            field_dict["AttachedFiles"] = attached_files
        if script_content is not UNSET:
            field_dict["ScriptContent"] = script_content
        if profile is not UNSET:
            field_dict["Profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_automation_attached_script_file_info import ApiAutomationAttachedScriptFileInfo

        d = src_dict.copy()
        technology = d.pop("Technology")

        attached_files = []
        _attached_files = d.pop("AttachedFiles", UNSET)
        for attached_files_item_data in _attached_files or []:
            attached_files_item = ApiAutomationAttachedScriptFileInfo.from_dict(attached_files_item_data)

            attached_files.append(attached_files_item)

        script_content = d.pop("ScriptContent", UNSET)

        profile = d.pop("Profile", UNSET)

        api_automation_script_unix_shell = cls(
            technology=technology,
            attached_files=attached_files,
            script_content=script_content,
            profile=profile,
        )

        api_automation_script_unix_shell.additional_properties = d
        return api_automation_script_unix_shell

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
