import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_tag_header_value import EntityTagHeaderValue


T = TypeVar("T", bound="RangeConditionHeaderValue")


@attr.s(auto_attribs=True)
class RangeConditionHeaderValue:
    """
    Attributes:
        date (Union[Unset, None, datetime.datetime]):
        entity_tag (Union[Unset, None, EntityTagHeaderValue]):
    """

    date: Union[Unset, None, datetime.datetime] = UNSET
    entity_tag: Union[Unset, None, "EntityTagHeaderValue"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date: Union[Unset, None, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat() if self.date else None

        entity_tag: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_tag, Unset):
            entity_tag = self.entity_tag.to_dict() if self.entity_tag else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if date is not UNSET:
            field_dict["Date"] = date
        if entity_tag is not UNSET:
            field_dict["EntityTag"] = entity_tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_tag_header_value import EntityTagHeaderValue

        d = src_dict.copy()
        _date = d.pop("Date", UNSET)
        date: Union[Unset, None, datetime.datetime]
        if _date is None:
            date = None
        elif isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _entity_tag = d.pop("EntityTag", UNSET)
        entity_tag: Union[Unset, None, EntityTagHeaderValue]
        if _entity_tag is None:
            entity_tag = None
        elif isinstance(_entity_tag, Unset):
            entity_tag = UNSET
        else:
            entity_tag = EntityTagHeaderValue.from_dict(_entity_tag)

        range_condition_header_value = cls(
            date=date,
            entity_tag=entity_tag,
        )

        return range_condition_header_value
