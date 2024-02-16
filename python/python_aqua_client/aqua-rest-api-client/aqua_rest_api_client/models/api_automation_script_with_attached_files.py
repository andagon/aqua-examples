from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_automation_attached_script_file_info import ApiAutomationAttachedScriptFileInfo


T = TypeVar("T", bound="ApiAutomationScriptWithAttachedFiles")


@attr.s(auto_attribs=True)
class ApiAutomationScriptWithAttachedFiles:
    """
    Attributes:
        technology (str):
        attached_files (Union[Unset, None, List['ApiAutomationAttachedScriptFileInfo']]): A list of attached files.
    """

    technology: str
    attached_files: Union[Unset, None, List["ApiAutomationAttachedScriptFileInfo"]] = UNSET
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Technology": technology,
            }
        )
        if attached_files is not UNSET:
            field_dict["AttachedFiles"] = attached_files

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

        api_automation_script_with_attached_files = cls(
            technology=technology,
            attached_files=attached_files,
        )

        api_automation_script_with_attached_files.additional_properties = d
        return api_automation_script_with_attached_files

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
