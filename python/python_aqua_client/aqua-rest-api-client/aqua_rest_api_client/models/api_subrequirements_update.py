from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_subrequirement import ApiSubrequirement


T = TypeVar("T", bound="ApiSubrequirementsUpdate")


@attr.s(auto_attribs=True)
class ApiSubrequirementsUpdate:
    """
    Attributes:
        subrequirements (Union[Unset, None, List['ApiSubrequirement']]):
    """

    subrequirements: Union[Unset, None, List["ApiSubrequirement"]] = UNSET

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
        from ..models.api_subrequirement import ApiSubrequirement

        d = src_dict.copy()
        subrequirements = []
        _subrequirements = d.pop("Subrequirements", UNSET)
        for subrequirements_item_data in _subrequirements or []:
            subrequirements_item = ApiSubrequirement.from_dict(subrequirements_item_data)

            subrequirements.append(subrequirements_item)

        api_subrequirements_update = cls(
            subrequirements=subrequirements,
        )

        return api_subrequirements_update
