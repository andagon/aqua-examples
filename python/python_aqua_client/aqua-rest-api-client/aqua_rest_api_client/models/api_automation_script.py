from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiAutomationScript")


@attr.s(auto_attribs=True)
class ApiAutomationScript:
    """
    Attributes:
        technology (str):
    """

    technology: str

    def to_dict(self) -> Dict[str, Any]:
        technology = self.technology

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Technology": technology,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        technology = d.pop("Technology")

        api_automation_script = cls(
            technology=technology,
        )

        return api_automation_script
