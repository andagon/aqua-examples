from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_edit_layout_entry import ApiEditLayoutEntry


T = TypeVar("T", bound="ApiEditLayoutEntryGroup")


@attr.s(auto_attribs=True)
class ApiEditLayoutEntryGroup:
    """
    Attributes:
        entry_type (str):
        caption (Union[Unset, None, str]): Group's caption.
        expanded (Union[Unset, bool]): Indicates whether group should be initially expanded.
        group_members (Union[Unset, None, List['ApiEditLayoutEntry']]): Members of this group
    """

    entry_type: str
    caption: Union[Unset, None, str] = UNSET
    expanded: Union[Unset, bool] = UNSET
    group_members: Union[Unset, None, List["ApiEditLayoutEntry"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry_type = self.entry_type
        caption = self.caption
        expanded = self.expanded
        group_members: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_members, Unset):
            if self.group_members is None:
                group_members = None
            else:
                group_members = []
                for group_members_item_data in self.group_members:
                    group_members_item = group_members_item_data.to_dict()

                    group_members.append(group_members_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "EntryType": entry_type,
            }
        )
        if caption is not UNSET:
            field_dict["Caption"] = caption
        if expanded is not UNSET:
            field_dict["Expanded"] = expanded
        if group_members is not UNSET:
            field_dict["GroupMembers"] = group_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_edit_layout_entry import ApiEditLayoutEntry

        d = src_dict.copy()
        entry_type = d.pop("EntryType")

        caption = d.pop("Caption", UNSET)

        expanded = d.pop("Expanded", UNSET)

        group_members = []
        _group_members = d.pop("GroupMembers", UNSET)
        for group_members_item_data in _group_members or []:
            group_members_item = ApiEditLayoutEntry.from_dict(group_members_item_data)

            group_members.append(group_members_item)

        api_edit_layout_entry_group = cls(
            entry_type=entry_type,
            caption=caption,
            expanded=expanded,
            group_members=group_members,
        )

        api_edit_layout_entry_group.additional_properties = d
        return api_edit_layout_entry_group

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
