from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAutomationScriptQTPSave")


@attr.s(auto_attribs=True)
class ApiAutomationScriptQTPSave:
    """
    Attributes:
        technology (str):
        is_new (Union[Unset, bool]): Indicates whether data represent a new (transient) content or an update of existing
            content.
            Should be set to true if we are saving a new automation into step that previously contained any automation
            already.
    """

    technology: str
    is_new: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        technology = self.technology
        is_new = self.is_new

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Technology": technology,
            }
        )
        if is_new is not UNSET:
            field_dict["IsNew"] = is_new

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        technology = d.pop("Technology")

        is_new = d.pop("IsNew", UNSET)

        api_automation_script_qtp_save = cls(
            technology=technology,
            is_new=is_new,
        )

        api_automation_script_qtp_save.additional_properties = d
        return api_automation_script_qtp_save

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
