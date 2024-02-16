from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_history_script_file_modified import ApiHistoryScriptFileModified


T = TypeVar("T", bound="ApiHistoryAutomationModified")


@attr.s(auto_attribs=True)
class ApiHistoryAutomationModified:
    """The list of changes to the automation related files.

    Attributes:
        script_files_added (Union[Unset, None, List[str]]): The list of names of the script files which were added.
        script_files_modified (Union[Unset, None, List['ApiHistoryScriptFileModified']]): The list of the script
            changes.
        script_files_removed (Union[Unset, None, List[str]]): The list of names of the script files which were removed.
        data_files_added (Union[Unset, None, List[str]]): The list of names of the data files which were added.
        data_files_removed (Union[Unset, None, List[str]]): The list of names of the data files which were removed.
    """

    script_files_added: Union[Unset, None, List[str]] = UNSET
    script_files_modified: Union[Unset, None, List["ApiHistoryScriptFileModified"]] = UNSET
    script_files_removed: Union[Unset, None, List[str]] = UNSET
    data_files_added: Union[Unset, None, List[str]] = UNSET
    data_files_removed: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        script_files_added: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.script_files_added, Unset):
            if self.script_files_added is None:
                script_files_added = None
            else:
                script_files_added = self.script_files_added

        script_files_modified: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.script_files_modified, Unset):
            if self.script_files_modified is None:
                script_files_modified = None
            else:
                script_files_modified = []
                for script_files_modified_item_data in self.script_files_modified:
                    script_files_modified_item = script_files_modified_item_data.to_dict()

                    script_files_modified.append(script_files_modified_item)

        script_files_removed: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.script_files_removed, Unset):
            if self.script_files_removed is None:
                script_files_removed = None
            else:
                script_files_removed = self.script_files_removed

        data_files_added: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.data_files_added, Unset):
            if self.data_files_added is None:
                data_files_added = None
            else:
                data_files_added = self.data_files_added

        data_files_removed: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.data_files_removed, Unset):
            if self.data_files_removed is None:
                data_files_removed = None
            else:
                data_files_removed = self.data_files_removed

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if script_files_added is not UNSET:
            field_dict["ScriptFilesAdded"] = script_files_added
        if script_files_modified is not UNSET:
            field_dict["ScriptFilesModified"] = script_files_modified
        if script_files_removed is not UNSET:
            field_dict["ScriptFilesRemoved"] = script_files_removed
        if data_files_added is not UNSET:
            field_dict["DataFilesAdded"] = data_files_added
        if data_files_removed is not UNSET:
            field_dict["DataFilesRemoved"] = data_files_removed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_history_script_file_modified import ApiHistoryScriptFileModified

        d = src_dict.copy()
        script_files_added = cast(List[str], d.pop("ScriptFilesAdded", UNSET))

        script_files_modified = []
        _script_files_modified = d.pop("ScriptFilesModified", UNSET)
        for script_files_modified_item_data in _script_files_modified or []:
            script_files_modified_item = ApiHistoryScriptFileModified.from_dict(script_files_modified_item_data)

            script_files_modified.append(script_files_modified_item)

        script_files_removed = cast(List[str], d.pop("ScriptFilesRemoved", UNSET))

        data_files_added = cast(List[str], d.pop("DataFilesAdded", UNSET))

        data_files_removed = cast(List[str], d.pop("DataFilesRemoved", UNSET))

        api_history_automation_modified = cls(
            script_files_added=script_files_added,
            script_files_modified=script_files_modified,
            script_files_removed=script_files_removed,
            data_files_added=data_files_added,
            data_files_removed=data_files_removed,
        )

        return api_history_automation_modified
