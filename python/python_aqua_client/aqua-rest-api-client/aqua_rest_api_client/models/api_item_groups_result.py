from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_group import ApiItemGroup


T = TypeVar("T", bound="ApiItemGroupsResult")


@attr.s(auto_attribs=True)
class ApiItemGroupsResult:
    """
    Attributes:
        total (Union[Unset, int]):
        groups (Union[Unset, None, List['ApiItemGroup']]):
    """

    total: Union[Unset, int] = UNSET
    groups: Union[Unset, None, List["ApiItemGroup"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        groups: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            if self.groups is None:
                groups = None
            else:
                groups = []
                for groups_item_data in self.groups:
                    groups_item = groups_item_data.to_dict()

                    groups.append(groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if total is not UNSET:
            field_dict["Total"] = total
        if groups is not UNSET:
            field_dict["Groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_group import ApiItemGroup

        d = src_dict.copy()
        total = d.pop("Total", UNSET)

        groups = []
        _groups = d.pop("Groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = ApiItemGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        api_item_groups_result = cls(
            total=total,
            groups=groups,
        )

        return api_item_groups_result
