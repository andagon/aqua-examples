import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiPostInfo")


@attr.s(auto_attribs=True)
class ApiPostInfo:
    """This class contains just the basic information on a post but not
    its contents or the list of users mentioned in it.

        Attributes:
            id (Union[Unset, int]): The id of the post.
            number (Union[Unset, int]): The index of this post in the list posts for the associated item.
            creator (Union[Unset, None, ApiUserInfo]): The user information
            last_editor (Union[Unset, None, ApiUserInfo]): The user information
            date_created (Union[Unset, datetime.datetime]): The date when the post was created.
            date_modified (Union[Unset, datetime.datetime]): The date when the post was last modified.
            deleted (Union[Unset, bool]): Indicates whether the post has been deleted. Deleted posts do not contain any
                content but are still included in the list of post for a certain item.
    """

    id: Union[Unset, int] = UNSET
    number: Union[Unset, int] = UNSET
    creator: Union[Unset, None, "ApiUserInfo"] = UNSET
    last_editor: Union[Unset, None, "ApiUserInfo"] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    date_modified: Union[Unset, datetime.datetime] = UNSET
    deleted: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        number = self.number
        creator: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict() if self.creator else None

        last_editor: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_editor, Unset):
            last_editor = self.last_editor.to_dict() if self.last_editor else None

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: Union[Unset, str] = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        deleted = self.deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if number is not UNSET:
            field_dict["Number"] = number
        if creator is not UNSET:
            field_dict["Creator"] = creator
        if last_editor is not UNSET:
            field_dict["LastEditor"] = last_editor
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if date_modified is not UNSET:
            field_dict["DateModified"] = date_modified
        if deleted is not UNSET:
            field_dict["Deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        number = d.pop("Number", UNSET)

        _creator = d.pop("Creator", UNSET)
        creator: Union[Unset, None, ApiUserInfo]
        if _creator is None:
            creator = None
        elif isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = ApiUserInfo.from_dict(_creator)

        _last_editor = d.pop("LastEditor", UNSET)
        last_editor: Union[Unset, None, ApiUserInfo]
        if _last_editor is None:
            last_editor = None
        elif isinstance(_last_editor, Unset):
            last_editor = UNSET
        else:
            last_editor = ApiUserInfo.from_dict(_last_editor)

        _date_created = d.pop("DateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_modified = d.pop("DateModified", UNSET)
        date_modified: Union[Unset, datetime.datetime]
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        deleted = d.pop("Deleted", UNSET)

        api_post_info = cls(
            id=id,
            number=number,
            creator=creator,
            last_editor=last_editor,
            date_created=date_created,
            date_modified=date_modified,
            deleted=deleted,
        )

        return api_post_info
