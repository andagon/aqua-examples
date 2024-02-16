from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSprintNewResponse")


@attr.s(auto_attribs=True)
class ApiSprintNewResponse:
    """Contains information about created sprint.

    Attributes:
        sprint_id (Union[Unset, int]): The id of the sprint.
    """

    sprint_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sprint_id = self.sprint_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if sprint_id is not UNSET:
            field_dict["SprintId"] = sprint_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sprint_id = d.pop("SprintId", UNSET)

        api_sprint_new_response = cls(
            sprint_id=sprint_id,
        )

        return api_sprint_new_response
