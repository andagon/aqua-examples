from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_enclosure_type import ApiEnclosureType
from ..models.api_history_enclosure_change_type import ApiHistoryEnclosureChangeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_rich_text import ApiRichText


T = TypeVar("T", bound="ApiHistoryEnclosureChanged")


@attr.s(auto_attribs=True)
class ApiHistoryEnclosureChanged:
    """Contains the changes to a single enclosure.

    Attributes:
        id (Union[Unset, None, int]): The id of the changed enclosure. Might be null, if
            the id has not been tracked.
        enclosure_type (Union[Unset, None, ApiEnclosureType]): Identifies the type of enclosure.
            This enum has the following values:
              - `Description` The enclosure is a description of the defect.
              - `Note` The enclosure is a note.
              - `ReplicationProcedure` The enclosure is a replication procedure which explains how
            to reproduce the defect.
              - `Resolution` The enclosure explains how the defect has been resolved.
        change_type (Union[Unset, ApiHistoryEnclosureChangeType]): Identifies the type of change to a certain enclosure.
            This enum has the following values:
              - `Added` The enclosure has been added.
              - `Deleted` The enclosure has been deleted.
              - `Modified` The enclosure has been modified.
        old_content (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
        new_content (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
    """

    id: Union[Unset, None, int] = UNSET
    enclosure_type: Union[Unset, None, ApiEnclosureType] = UNSET
    change_type: Union[Unset, ApiHistoryEnclosureChangeType] = UNSET
    old_content: Union[Unset, None, "ApiRichText"] = UNSET
    new_content: Union[Unset, None, "ApiRichText"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        enclosure_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.enclosure_type, Unset):
            enclosure_type = self.enclosure_type.value if self.enclosure_type else None

        change_type: Union[Unset, str] = UNSET
        if not isinstance(self.change_type, Unset):
            change_type = self.change_type.value

        old_content: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.old_content, Unset):
            old_content = self.old_content.to_dict() if self.old_content else None

        new_content: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.new_content, Unset):
            new_content = self.new_content.to_dict() if self.new_content else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if enclosure_type is not UNSET:
            field_dict["EnclosureType"] = enclosure_type
        if change_type is not UNSET:
            field_dict["ChangeType"] = change_type
        if old_content is not UNSET:
            field_dict["OldContent"] = old_content
        if new_content is not UNSET:
            field_dict["NewContent"] = new_content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_rich_text import ApiRichText

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _enclosure_type = d.pop("EnclosureType", UNSET)
        enclosure_type: Union[Unset, None, ApiEnclosureType]
        if _enclosure_type is None:
            enclosure_type = None
        elif isinstance(_enclosure_type, Unset):
            enclosure_type = UNSET
        else:
            enclosure_type = ApiEnclosureType(_enclosure_type)

        _change_type = d.pop("ChangeType", UNSET)
        change_type: Union[Unset, ApiHistoryEnclosureChangeType]
        if isinstance(_change_type, Unset):
            change_type = UNSET
        else:
            change_type = ApiHistoryEnclosureChangeType(_change_type)

        _old_content = d.pop("OldContent", UNSET)
        old_content: Union[Unset, None, ApiRichText]
        if _old_content is None:
            old_content = None
        elif isinstance(_old_content, Unset):
            old_content = UNSET
        else:
            old_content = ApiRichText.from_dict(_old_content)

        _new_content = d.pop("NewContent", UNSET)
        new_content: Union[Unset, None, ApiRichText]
        if _new_content is None:
            new_content = None
        elif isinstance(_new_content, Unset):
            new_content = UNSET
        else:
            new_content = ApiRichText.from_dict(_new_content)

        api_history_enclosure_changed = cls(
            id=id,
            enclosure_type=enclosure_type,
            change_type=change_type,
            old_content=old_content,
            new_content=new_content,
        )

        return api_history_enclosure_changed
