from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_enclosure_type import ApiEnclosureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_rich_text import ApiRichText


T = TypeVar("T", bound="ApiEnclosureUpdateWithId")


@attr.s(auto_attribs=True)
class ApiEnclosureUpdateWithId:
    """
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
        id (Union[Unset, int]): The id of the enclosure to update.
    """

    type: Union[Unset, ApiEnclosureType] = UNSET
    content: Union[Unset, None, "ApiRichText"] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        content: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict() if self.content else None

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if content is not UNSET:
            field_dict["Content"] = content
        if id is not UNSET:
            field_dict["Id"] = id

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

        id = d.pop("Id", UNSET)

        api_enclosure_update_with_id = cls(
            type=type,
            content=content,
            id=id,
        )

        api_enclosure_update_with_id.additional_properties = d
        return api_enclosure_update_with_id

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
