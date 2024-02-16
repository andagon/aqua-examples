from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_automation_script_save import ApiAutomationScriptSave


T = TypeVar("T", bound="ApiAutomationSave")


@attr.s(auto_attribs=True)
class ApiAutomationSave:
    """Automation part of a test step, as used when saving data.

    Attributes:
        script_id (Union[Unset, int]): If not zero indicates that automation script (represented by this object) is from
            script library.
            In such case update is only possible via corresponding Script item, not via Test Case.
        script (Union[Unset, None, ApiAutomationScriptSave]):
    """

    script_id: Union[Unset, int] = UNSET
    script: Union[Unset, None, "ApiAutomationScriptSave"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        script_id = self.script_id
        script: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.script, Unset):
            script = self.script.to_dict() if self.script else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if script_id is not UNSET:
            field_dict["ScriptId"] = script_id
        if script is not UNSET:
            field_dict["Script"] = script

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_automation_script_save import ApiAutomationScriptSave

        d = src_dict.copy()
        script_id = d.pop("ScriptId", UNSET)

        _script = d.pop("Script", UNSET)
        script: Union[Unset, None, ApiAutomationScriptSave]
        if _script is None:
            script = None
        elif isinstance(_script, Unset):
            script = UNSET
        else:
            script = ApiAutomationScriptSave.from_dict(_script)

        api_automation_save = cls(
            script_id=script_id,
            script=script,
        )

        return api_automation_save
