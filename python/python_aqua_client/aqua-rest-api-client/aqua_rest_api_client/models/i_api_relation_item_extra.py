from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="IApiRelationItemExtra")


@attr.s(auto_attribs=True)
class IApiRelationItemExtra:
    """Holds additional, relation-specific data for one side of a relation."""

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        i_api_relation_item_extra = cls()

        return i_api_relation_item_extra
