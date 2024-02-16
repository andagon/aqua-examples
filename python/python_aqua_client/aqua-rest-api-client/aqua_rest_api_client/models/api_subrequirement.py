from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.api_editable_status import ApiEditableStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_info import ApiItemInfo


T = TypeVar("T", bound="ApiSubrequirement")


@attr.s(auto_attribs=True)
class ApiSubrequirement:
    """A sub requirement is a child of another requirement. This
    class contains basic information for the sub requirement.

        Attributes:
            id (Union[Unset, int]): The id of the sub requirement.
            item (Union[Unset, None, ApiItemInfo]):
            parent_id (Union[Unset, int]): The id of the parent of this sub requirement.
            child_index (Union[Unset, int]): The index of this requirement in the list of sub requirements
                of the parent requirement.
            position (Union[Unset, None, List[int]]): This list contains the position of this sub requirement in each level
                of the sub requirement tree of the root requirement. E.g. [4,2]
                means that this sub requirement is the 2nd sub requirement of the 4th
                sub requirement of the root requirement.
                This information is relative to the requirement for which the sub requirements
                were requested.
            further_subrequirements_count (Union[Unset, int]): The number of sub requirements of the current sub
                requirement.
            editable_status (Union[Unset, None, ApiEditableStatus]):
                This enum has the following values:
                  - `Editable` The item can be edited.
                  - `Locked` The item is already locked (either by another user or
                by the same user in a different context)
                  - `NoPermissionToEdit` The current user is not permitted to edit the item.
                  - `NoPermissionToView` The current user is not permitted to view the item.
                  - `Unknown` No information is provided whether the item is editable or not.
                The item should not be edited based on this editable status.
    """

    id: Union[Unset, int] = UNSET
    item: Union[Unset, None, "ApiItemInfo"] = UNSET
    parent_id: Union[Unset, int] = UNSET
    child_index: Union[Unset, int] = UNSET
    position: Union[Unset, None, List[int]] = UNSET
    further_subrequirements_count: Union[Unset, int] = UNSET
    editable_status: Union[Unset, None, ApiEditableStatus] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict() if self.item else None

        parent_id = self.parent_id
        child_index = self.child_index
        position: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.position, Unset):
            if self.position is None:
                position = None
            else:
                position = self.position

        further_subrequirements_count = self.further_subrequirements_count
        editable_status: Union[Unset, None, str] = UNSET
        if not isinstance(self.editable_status, Unset):
            editable_status = self.editable_status.value if self.editable_status else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if item is not UNSET:
            field_dict["Item"] = item
        if parent_id is not UNSET:
            field_dict["ParentId"] = parent_id
        if child_index is not UNSET:
            field_dict["ChildIndex"] = child_index
        if position is not UNSET:
            field_dict["Position"] = position
        if further_subrequirements_count is not UNSET:
            field_dict["FurtherSubrequirementsCount"] = further_subrequirements_count
        if editable_status is not UNSET:
            field_dict["EditableStatus"] = editable_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_info import ApiItemInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _item = d.pop("Item", UNSET)
        item: Union[Unset, None, ApiItemInfo]
        if _item is None:
            item = None
        elif isinstance(_item, Unset):
            item = UNSET
        else:
            item = ApiItemInfo.from_dict(_item)

        parent_id = d.pop("ParentId", UNSET)

        child_index = d.pop("ChildIndex", UNSET)

        position = cast(List[int], d.pop("Position", UNSET))

        further_subrequirements_count = d.pop("FurtherSubrequirementsCount", UNSET)

        _editable_status = d.pop("EditableStatus", UNSET)
        editable_status: Union[Unset, None, ApiEditableStatus]
        if _editable_status is None:
            editable_status = None
        elif isinstance(_editable_status, Unset):
            editable_status = UNSET
        else:
            editable_status = ApiEditableStatus(_editable_status)

        api_subrequirement = cls(
            id=id,
            item=item,
            parent_id=parent_id,
            child_index=child_index,
            position=position,
            further_subrequirements_count=further_subrequirements_count,
            editable_status=editable_status,
        )

        return api_subrequirement
