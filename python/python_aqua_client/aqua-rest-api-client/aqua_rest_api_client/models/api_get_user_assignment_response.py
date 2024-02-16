from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_user_role import ApiUserRole


T = TypeVar("T", bound="ApiGetUserAssignmentResponse")


@attr.s(auto_attribs=True)
class ApiGetUserAssignmentResponse:
    """Represents the get user assignment response.

    Attributes:
        assignements (Union[Unset, None, List['ApiUserRole']]): The list of assignments.
    """

    assignements: Union[Unset, None, List["ApiUserRole"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        assignements: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assignements, Unset):
            if self.assignements is None:
                assignements = None
            else:
                assignements = []
                for assignements_item_data in self.assignements:
                    assignements_item = assignements_item_data.to_dict()

                    assignements.append(assignements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if assignements is not UNSET:
            field_dict["Assignements"] = assignements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_user_role import ApiUserRole

        d = src_dict.copy()
        assignements = []
        _assignements = d.pop("Assignements", UNSET)
        for assignements_item_data in _assignements or []:
            assignements_item = ApiUserRole.from_dict(assignements_item_data)

            assignements.append(assignements_item)

        api_get_user_assignment_response = cls(
            assignements=assignements,
        )

        return api_get_user_assignment_response
