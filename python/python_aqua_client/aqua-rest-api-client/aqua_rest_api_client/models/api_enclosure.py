import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_enclosure_type import ApiEnclosureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_enclosure_permissions import ApiEnclosurePermissions
    from ..models.api_rich_text import ApiRichText
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiEnclosure")


@attr.s(auto_attribs=True)
class ApiEnclosure:
    """An enclosure of a defect.

    Attributes:
        id (Union[Unset, int]): The id of the enclosure.
        type (Union[Unset, ApiEnclosureType]): Identifies the type of enclosure.
            This enum has the following values:
              - `Description` The enclosure is a description of the defect.
              - `Note` The enclosure is a note.
              - `ReplicationProcedure` The enclosure is a replication procedure which explains how
            to reproduce the defect.
              - `Resolution` The enclosure explains how the defect has been resolved.
        creation_date (Union[Unset, datetime.datetime]): The date when the enclosure has been created.
        content (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
        owner (Union[Unset, None, ApiUserInfo]): The user information
        permissions (Union[Unset, None, ApiEnclosurePermissions]): Represents permissions of a Enclosure.
    """

    id: Union[Unset, int] = UNSET
    type: Union[Unset, ApiEnclosureType] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    content: Union[Unset, None, "ApiRichText"] = UNSET
    owner: Union[Unset, None, "ApiUserInfo"] = UNSET
    permissions: Union[Unset, None, "ApiEnclosurePermissions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        content: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict() if self.content else None

        owner: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict() if self.owner else None

        permissions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict() if self.permissions else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if type is not UNSET:
            field_dict["Type"] = type
        if creation_date is not UNSET:
            field_dict["CreationDate"] = creation_date
        if content is not UNSET:
            field_dict["Content"] = content
        if owner is not UNSET:
            field_dict["Owner"] = owner
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_enclosure_permissions import ApiEnclosurePermissions
        from ..models.api_rich_text import ApiRichText
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiEnclosureType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiEnclosureType(_type)

        _creation_date = d.pop("CreationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _content = d.pop("Content", UNSET)
        content: Union[Unset, None, ApiRichText]
        if _content is None:
            content = None
        elif isinstance(_content, Unset):
            content = UNSET
        else:
            content = ApiRichText.from_dict(_content)

        _owner = d.pop("Owner", UNSET)
        owner: Union[Unset, None, ApiUserInfo]
        if _owner is None:
            owner = None
        elif isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = ApiUserInfo.from_dict(_owner)

        _permissions = d.pop("Permissions", UNSET)
        permissions: Union[Unset, None, ApiEnclosurePermissions]
        if _permissions is None:
            permissions = None
        elif isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ApiEnclosurePermissions.from_dict(_permissions)

        api_enclosure = cls(
            id=id,
            type=type,
            creation_date=creation_date,
            content=content,
            owner=owner,
            permissions=permissions,
        )

        return api_enclosure
