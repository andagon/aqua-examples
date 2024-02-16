import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WarningHeaderValue")


@attr.s(auto_attribs=True)
class WarningHeaderValue:
    """
    Attributes:
        code (Union[Unset, int]):
        agent (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        date (Union[Unset, None, datetime.datetime]):
    """

    code: Union[Unset, int] = UNSET
    agent: Union[Unset, None, str] = UNSET
    text: Union[Unset, None, str] = UNSET
    date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        agent = self.agent
        text = self.text
        date: Union[Unset, None, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat() if self.date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if code is not UNSET:
            field_dict["Code"] = code
        if agent is not UNSET:
            field_dict["Agent"] = agent
        if text is not UNSET:
            field_dict["Text"] = text
        if date is not UNSET:
            field_dict["Date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("Code", UNSET)

        agent = d.pop("Agent", UNSET)

        text = d.pop("Text", UNSET)

        _date = d.pop("Date", UNSET)
        date: Union[Unset, None, datetime.datetime]
        if _date is None:
            date = None
        elif isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        warning_header_value = cls(
            code=code,
            agent=agent,
            text=text,
            date=date,
        )

        return warning_header_value
