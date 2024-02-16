from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachment_new import ApiAttachmentNew


T = TypeVar("T", bound="ApiAttachments")


@attr.s(auto_attribs=True)
class ApiAttachments:
    """Contains all changes to the attachments of an item.

    Attributes:
        added (Union[Unset, None, List['ApiAttachmentNew']]): The list of attachments to add to the item.
        removed (Union[Unset, None, List[int]]): The list of ids of the attachments which should be removed from
            the item.
    """

    added: Union[Unset, None, List["ApiAttachmentNew"]] = UNSET
    removed: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        added: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.added, Unset):
            if self.added is None:
                added = None
            else:
                added = []
                for added_item_data in self.added:
                    added_item = added_item_data.to_dict()

                    added.append(added_item)

        removed: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.removed, Unset):
            if self.removed is None:
                removed = None
            else:
                removed = self.removed

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if added is not UNSET:
            field_dict["Added"] = added
        if removed is not UNSET:
            field_dict["Removed"] = removed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachment_new import ApiAttachmentNew

        d = src_dict.copy()
        added = []
        _added = d.pop("Added", UNSET)
        for added_item_data in _added or []:
            added_item = ApiAttachmentNew.from_dict(added_item_data)

            added.append(added_item)

        removed = cast(List[int], d.pop("Removed", UNSET))

        api_attachments = cls(
            added=added,
            removed=removed,
        )

        return api_attachments
