from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_editable_info import ApiEditableInfo


T = TypeVar("T", bound="ApiEditStatus")


@attr.s(auto_attribs=True)
class ApiEditStatus:
    """Edit status information

    Attributes:
        version (Union[Unset, int]): This field provides information about item version.
        editable_info (Union[Unset, None, ApiEditableInfo]): Contains information about editable status of an item.
    """

    version: Union[Unset, int] = UNSET
    editable_info: Union[Unset, None, "ApiEditableInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        editable_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.editable_info, Unset):
            editable_info = self.editable_info.to_dict() if self.editable_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version
        if editable_info is not UNSET:
            field_dict["EditableInfo"] = editable_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_editable_info import ApiEditableInfo

        d = src_dict.copy()
        version = d.pop("Version", UNSET)

        _editable_info = d.pop("EditableInfo", UNSET)
        editable_info: Union[Unset, None, ApiEditableInfo]
        if _editable_info is None:
            editable_info = None
        elif isinstance(_editable_info, Unset):
            editable_info = UNSET
        else:
            editable_info = ApiEditableInfo.from_dict(_editable_info)

        api_edit_status = cls(
            version=version,
            editable_info=editable_info,
        )

        return api_edit_status
