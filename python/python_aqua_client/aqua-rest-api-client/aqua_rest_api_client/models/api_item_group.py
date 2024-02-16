from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemGroup")


@attr.s(auto_attribs=True)
class ApiItemGroup:
    """
    Attributes:
        field_id (Union[Unset, None, str]):
        caption (Union[Unset, None, str]):
        count (Union[Unset, int]):
        filter_ (Union[Unset, Any]):
        sub_groups (Union[Unset, None, List['ApiItemGroup']]):
    """

    field_id: Union[Unset, None, str] = UNSET
    caption: Union[Unset, None, str] = UNSET
    count: Union[Unset, int] = UNSET
    filter_: Union[Unset, Any] = UNSET
    sub_groups: Union[Unset, None, List["ApiItemGroup"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        caption = self.caption
        count = self.count
        filter_ = self.filter_
        sub_groups: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_groups, Unset):
            if self.sub_groups is None:
                sub_groups = None
            else:
                sub_groups = []
                for sub_groups_item_data in self.sub_groups:
                    sub_groups_item = sub_groups_item_data.to_dict()

                    sub_groups.append(sub_groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if caption is not UNSET:
            field_dict["Caption"] = caption
        if count is not UNSET:
            field_dict["Count"] = count
        if filter_ is not UNSET:
            field_dict["Filter"] = filter_
        if sub_groups is not UNSET:
            field_dict["SubGroups"] = sub_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId", UNSET)

        caption = d.pop("Caption", UNSET)

        count = d.pop("Count", UNSET)

        filter_ = d.pop("Filter", UNSET)

        sub_groups = []
        _sub_groups = d.pop("SubGroups", UNSET)
        for sub_groups_item_data in _sub_groups or []:
            sub_groups_item = ApiItemGroup.from_dict(sub_groups_item_data)

            sub_groups.append(sub_groups_item)

        api_item_group = cls(
            field_id=field_id,
            caption=caption,
            count=count,
            filter_=filter_,
            sub_groups=sub_groups,
        )

        return api_item_group
