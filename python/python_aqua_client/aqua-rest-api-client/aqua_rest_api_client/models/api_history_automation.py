from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_automation_technology import ApiAutomationTechnology
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_history_automation_modified import ApiHistoryAutomationModified


T = TypeVar("T", bound="ApiHistoryAutomation")


@attr.s(auto_attribs=True)
class ApiHistoryAutomation:
    """Contains the automation changes.

    Attributes:
        added (Union[Unset, None, ApiAutomationTechnology]): Represents the different test automation technologies
            supported
            by aqua.
            This enum has the following values:
              - `Database` aqua's database automation technology allows to execute
            SQL instructions against various database management
            systems.
              - `Jenkins` Integration with the Jenkins CI and CD server. Allows to
            trigger jobs on the Jenkins server.
              - `JMeter` Integration of the load and performance test tool Apache
            JMeter.
              - `None` No test automation technology is used.
              - `PowerShell` aqua's Powershell integration allows to execute
            arbitrary Powershell scripts.
              - `QTP` HP QuickTest Professional integration
              - `Ranorex` Ranorex integration
              - `SoapUI` SoapUI integration
              - `UFT` MicroFocus Unified Functional Testing integration
              - `UnixShell` aqua's UnixShell integration allows to execute arbitrary
            unix shell scripts in various languages.
        removed (Union[Unset, None, ApiAutomationTechnology]): Represents the different test automation technologies
            supported
            by aqua.
            This enum has the following values:
              - `Database` aqua's database automation technology allows to execute
            SQL instructions against various database management
            systems.
              - `Jenkins` Integration with the Jenkins CI and CD server. Allows to
            trigger jobs on the Jenkins server.
              - `JMeter` Integration of the load and performance test tool Apache
            JMeter.
              - `None` No test automation technology is used.
              - `PowerShell` aqua's Powershell integration allows to execute
            arbitrary Powershell scripts.
              - `QTP` HP QuickTest Professional integration
              - `Ranorex` Ranorex integration
              - `SoapUI` SoapUI integration
              - `UFT` MicroFocus Unified Functional Testing integration
              - `UnixShell` aqua's UnixShell integration allows to execute arbitrary
            unix shell scripts in various languages.
        modified (Union[Unset, None, ApiHistoryAutomationModified]): The list of changes to the automation related
            files.
    """

    added: Union[Unset, None, ApiAutomationTechnology] = UNSET
    removed: Union[Unset, None, ApiAutomationTechnology] = UNSET
    modified: Union[Unset, None, "ApiHistoryAutomationModified"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        added: Union[Unset, None, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.value if self.added else None

        removed: Union[Unset, None, str] = UNSET
        if not isinstance(self.removed, Unset):
            removed = self.removed.value if self.removed else None

        modified: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.to_dict() if self.modified else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if added is not UNSET:
            field_dict["Added"] = added
        if removed is not UNSET:
            field_dict["Removed"] = removed
        if modified is not UNSET:
            field_dict["Modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_history_automation_modified import ApiHistoryAutomationModified

        d = src_dict.copy()
        _added = d.pop("Added", UNSET)
        added: Union[Unset, None, ApiAutomationTechnology]
        if _added is None:
            added = None
        elif isinstance(_added, Unset):
            added = UNSET
        else:
            added = ApiAutomationTechnology(_added)

        _removed = d.pop("Removed", UNSET)
        removed: Union[Unset, None, ApiAutomationTechnology]
        if _removed is None:
            removed = None
        elif isinstance(_removed, Unset):
            removed = UNSET
        else:
            removed = ApiAutomationTechnology(_removed)

        _modified = d.pop("Modified", UNSET)
        modified: Union[Unset, None, ApiHistoryAutomationModified]
        if _modified is None:
            modified = None
        elif isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = ApiHistoryAutomationModified.from_dict(_modified)

        api_history_automation = cls(
            added=added,
            removed=removed,
            modified=modified,
        )

        return api_history_automation
