from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.api_history_post_change_type import ApiHistoryPostChangeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistoryPostChanged")


@attr.s(auto_attribs=True)
class ApiHistoryPostChanged:
    """Contains the changes to a certain post.

    Attributes:
        change_type (Union[Unset, ApiHistoryPostChangeType]): Identifies the type of change to a certain post
            This enum has the following values:
              - `Added` The post has been added.
              - `Modified` The post has been modified.
              - `Removed` The post has been deleted.
        number (Union[Unset, int]): The index of this post in the list posts of the current item.
        mentioned_users (Union[Unset, None, List[str]]): The list of full names of the users which are mentioned in the
            post
            after the change.
        content_truncated (Union[Unset, None, str]): Truncated version of the content as plain text.
    """

    change_type: Union[Unset, ApiHistoryPostChangeType] = UNSET
    number: Union[Unset, int] = UNSET
    mentioned_users: Union[Unset, None, List[str]] = UNSET
    content_truncated: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        change_type: Union[Unset, str] = UNSET
        if not isinstance(self.change_type, Unset):
            change_type = self.change_type.value

        number = self.number
        mentioned_users: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.mentioned_users, Unset):
            if self.mentioned_users is None:
                mentioned_users = None
            else:
                mentioned_users = self.mentioned_users

        content_truncated = self.content_truncated

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if change_type is not UNSET:
            field_dict["ChangeType"] = change_type
        if number is not UNSET:
            field_dict["Number"] = number
        if mentioned_users is not UNSET:
            field_dict["MentionedUsers"] = mentioned_users
        if content_truncated is not UNSET:
            field_dict["ContentTruncated"] = content_truncated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _change_type = d.pop("ChangeType", UNSET)
        change_type: Union[Unset, ApiHistoryPostChangeType]
        if isinstance(_change_type, Unset):
            change_type = UNSET
        else:
            change_type = ApiHistoryPostChangeType(_change_type)

        number = d.pop("Number", UNSET)

        mentioned_users = cast(List[str], d.pop("MentionedUsers", UNSET))

        content_truncated = d.pop("ContentTruncated", UNSET)

        api_history_post_changed = cls(
            change_type=change_type,
            number=number,
            mentioned_users=mentioned_users,
            content_truncated=content_truncated,
        )

        return api_history_post_changed
