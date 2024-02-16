from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_subrequirement_new import ApiSubrequirementNew


T = TypeVar("T", bound="ApiSubrequirementsNew")


@attr.s(auto_attribs=True)
class ApiSubrequirementsNew:
    """Contains a list of sub requirements which should be
    added to the specified the requirement in a single operation.

        Attributes:
            subrequirements (Union[Unset, None, List['ApiSubrequirementNew']]): The sub requirements which should be added
    """

    subrequirements: Union[Unset, None, List["ApiSubrequirementNew"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subrequirements: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subrequirements, Unset):
            if self.subrequirements is None:
                subrequirements = None
            else:
                subrequirements = []
                for subrequirements_item_data in self.subrequirements:
                    subrequirements_item = subrequirements_item_data.to_dict()

                    subrequirements.append(subrequirements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subrequirements is not UNSET:
            field_dict["Subrequirements"] = subrequirements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_subrequirement_new import ApiSubrequirementNew

        d = src_dict.copy()
        subrequirements = []
        _subrequirements = d.pop("Subrequirements", UNSET)
        for subrequirements_item_data in _subrequirements or []:
            subrequirements_item = ApiSubrequirementNew.from_dict(subrequirements_item_data)

            subrequirements.append(subrequirements_item)

        api_subrequirements_new = cls(
            subrequirements=subrequirements,
        )

        return api_subrequirements_new
