from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAgileBacklogStatus")


@attr.s(auto_attribs=True)
class ApiAgileBacklogStatus:
    """Provides status for items in Agile backlog

    Attributes:
        id (Union[Unset, int]): ID
        name (Union[Unset, None, str]): Name
        is_hidden (Union[Unset, bool]): Provides information whether an item with this status
            should be hidden in the backlog or not
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    is_hidden: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        is_hidden = self.is_hidden

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if is_hidden is not UNSET:
            field_dict["IsHidden"] = is_hidden

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        is_hidden = d.pop("IsHidden", UNSET)

        api_agile_backlog_status = cls(
            id=id,
            name=name,
            is_hidden=is_hidden,
        )

        return api_agile_backlog_status
