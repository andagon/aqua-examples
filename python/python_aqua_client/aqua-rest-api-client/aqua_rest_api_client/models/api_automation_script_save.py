from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAutomationScriptSave")


@attr.s(auto_attribs=True)
class ApiAutomationScriptSave:
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

    def to_dict(self) -> Dict[str, Any]:
        technology = self.technology
        is_new = self.is_new

        field_dict: Dict[str, Any] = {}
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

        api_automation_script_save = cls(
            technology=technology,
            is_new=is_new,
        )

        return api_automation_script_save
