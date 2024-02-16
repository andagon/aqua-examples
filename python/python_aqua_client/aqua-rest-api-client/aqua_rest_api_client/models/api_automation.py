from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_automation_script import ApiAutomationScript


T = TypeVar("T", bound="ApiAutomation")


@attr.s(auto_attribs=True)
class ApiAutomation:
    """Automation part of a test step, as used when loading data.

    Attributes:
        script_id (Union[Unset, int]): If not zero indicates that automation script (represented by this object) is
            referenced from script library.
        script (Union[Unset, None, ApiAutomationScript]):
    """

    script_id: Union[Unset, int] = UNSET
    script: Union[Unset, None, "ApiAutomationScript"] = UNSET

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
        from ..models.api_automation_script import ApiAutomationScript

        d = src_dict.copy()
        script_id = d.pop("ScriptId", UNSET)

        _script = d.pop("Script", UNSET)
        script: Union[Unset, None, ApiAutomationScript]
        if _script is None:
            script = None
        elif isinstance(_script, Unset):
            script = UNSET
        else:
            script = ApiAutomationScript.from_dict(_script)

        api_automation = cls(
            script_id=script_id,
            script=script,
        )

        return api_automation
