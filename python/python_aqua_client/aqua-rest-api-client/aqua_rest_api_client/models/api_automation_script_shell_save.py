from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_automation_attached_script_file_new import ApiAutomationAttachedScriptFileNew


T = TypeVar("T", bound="ApiAutomationScriptShellSave")


@attr.s(auto_attribs=True)
class ApiAutomationScriptShellSave:
    """
    Attributes:
        technology (str):
        is_new (Union[Unset, bool]): Indicates whether data represent a new (transient) content or an update of existing
            content.
            Should be set to true if we are saving a new automation into step that previously contained any automation
            already.
        new_files (Union[Unset, None, List['ApiAutomationAttachedScriptFileNew']]): A list of files to be added.
            Note that each file includes Position (zero based index) where to insert the new file.
            Server at first deletes all files listed in 'DeletedFiles' and then inserts new files.
            In-place modification of attached files is not supported, thus modification is
            achieved by deleting existing attachment and adding a new one.
        deleted_files (Union[Unset, None, List[int]]): A list of files (their ids) to be removed.
        script_content (Union[Unset, None, str]): Script content.
        profile (Union[Unset, None, str]): Code of shell profile to be used (if any)
    """

    technology: str
    is_new: Union[Unset, bool] = UNSET
    new_files: Union[Unset, None, List["ApiAutomationAttachedScriptFileNew"]] = UNSET
    deleted_files: Union[Unset, None, List[int]] = UNSET
    script_content: Union[Unset, None, str] = UNSET
    profile: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        technology = self.technology
        is_new = self.is_new
        new_files: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.new_files, Unset):
            if self.new_files is None:
                new_files = None
            else:
                new_files = []
                for new_files_item_data in self.new_files:
                    new_files_item = new_files_item_data.to_dict()

                    new_files.append(new_files_item)

        deleted_files: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.deleted_files, Unset):
            if self.deleted_files is None:
                deleted_files = None
            else:
                deleted_files = self.deleted_files

        script_content = self.script_content
        profile = self.profile

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Technology": technology,
            }
        )
        if is_new is not UNSET:
            field_dict["IsNew"] = is_new
        if new_files is not UNSET:
            field_dict["NewFiles"] = new_files
        if deleted_files is not UNSET:
            field_dict["DeletedFiles"] = deleted_files
        if script_content is not UNSET:
            field_dict["ScriptContent"] = script_content
        if profile is not UNSET:
            field_dict["Profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_automation_attached_script_file_new import ApiAutomationAttachedScriptFileNew

        d = src_dict.copy()
        technology = d.pop("Technology")

        is_new = d.pop("IsNew", UNSET)

        new_files = []
        _new_files = d.pop("NewFiles", UNSET)
        for new_files_item_data in _new_files or []:
            new_files_item = ApiAutomationAttachedScriptFileNew.from_dict(new_files_item_data)

            new_files.append(new_files_item)

        deleted_files = cast(List[int], d.pop("DeletedFiles", UNSET))

        script_content = d.pop("ScriptContent", UNSET)

        profile = d.pop("Profile", UNSET)

        api_automation_script_shell_save = cls(
            technology=technology,
            is_new=is_new,
            new_files=new_files,
            deleted_files=deleted_files,
            script_content=script_content,
            profile=profile,
        )

        api_automation_script_shell_save.additional_properties = d
        return api_automation_script_shell_save

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
