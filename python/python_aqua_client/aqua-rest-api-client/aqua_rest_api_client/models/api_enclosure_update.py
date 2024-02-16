from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_enclosure_type import ApiEnclosureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_rich_text import ApiRichText


T = TypeVar("T", bound="ApiEnclosureUpdate")


@attr.s(auto_attribs=True)
class ApiEnclosureUpdate:
    """Specifies the changes to perform on a specific enclosure.

    Attributes:
        type (Union[Unset, ApiEnclosureType]): Identifies the type of enclosure.
            This enum has the following values:
              - `Description` The enclosure is a description of the defect.
              - `Note` The enclosure is a note.
              - `ReplicationProcedure` The enclosure is a replication procedure which explains how
            to reproduce the defect.
              - `Resolution` The enclosure explains how the defect has been resolved.
        content (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
    """

    type: Union[Unset, ApiEnclosureType] = UNSET
    content: Union[Unset, None, "ApiRichText"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        content: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict() if self.content else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if content is not UNSET:
            field_dict["Content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_rich_text import ApiRichText

        d = src_dict.copy()
        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiEnclosureType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiEnclosureType(_type)

        _content = d.pop("Content", UNSET)
        content: Union[Unset, None, ApiRichText]
        if _content is None:
            content = None
        elif isinstance(_content, Unset):
            content = UNSET
        else:
            content = ApiRichText.from_dict(_content)

        api_enclosure_update = cls(
            type=type,
            content=content,
        )

        return api_enclosure_update
