from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_post import ApiPost


T = TypeVar("T", bound="ApiPostPaginated")


@attr.s(auto_attribs=True)
class ApiPostPaginated:
    """Contains paginated posts with total count of posts.

    Attributes:
        posts (Union[Unset, None, List['ApiPost']]): The list of paginated posts.
        posts_total_count (Union[Unset, int]): The total count of posts for this object.
    """

    posts: Union[Unset, None, List["ApiPost"]] = UNSET
    posts_total_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        posts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.posts, Unset):
            if self.posts is None:
                posts = None
            else:
                posts = []
                for posts_item_data in self.posts:
                    posts_item = posts_item_data.to_dict()

                    posts.append(posts_item)

        posts_total_count = self.posts_total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if posts is not UNSET:
            field_dict["Posts"] = posts
        if posts_total_count is not UNSET:
            field_dict["PostsTotalCount"] = posts_total_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_post import ApiPost

        d = src_dict.copy()
        posts = []
        _posts = d.pop("Posts", UNSET)
        for posts_item_data in _posts or []:
            posts_item = ApiPost.from_dict(posts_item_data)

            posts.append(posts_item)

        posts_total_count = d.pop("PostsTotalCount", UNSET)

        api_post_paginated = cls(
            posts=posts,
            posts_total_count=posts_total_count,
        )

        return api_post_paginated
