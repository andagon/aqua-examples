from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachments import ApiAttachments
    from ..models.api_field_update import ApiFieldUpdate


T = TypeVar("T", bound="ApiItemUpdate")


@attr.s(auto_attribs=True)
class ApiItemUpdate:
    """Specifies the changes to perform on a specific item.

    Attributes:
        details (Union[Unset, None, List['ApiFieldUpdate']]): The list of updates to perform on the different fields of
            the item.
        attachments (Union[Unset, None, ApiAttachments]): Contains all changes to the attachments of an item.
    """

    details: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET
    attachments: Union[Unset, None, "ApiAttachments"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        details: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            if self.details is None:
                details = None
            else:
                details = []
                for details_item_data in self.details:
                    details_item = details_item_data.to_dict()

                    details.append(details_item)

        attachments: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict() if self.attachments else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if details is not UNSET:
            field_dict["Details"] = details
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachments import ApiAttachments
        from ..models.api_field_update import ApiFieldUpdate

        d = src_dict.copy()
        details = []
        _details = d.pop("Details", UNSET)
        for details_item_data in _details or []:
            details_item = ApiFieldUpdate.from_dict(details_item_data)

            details.append(details_item)

        _attachments = d.pop("Attachments", UNSET)
        attachments: Union[Unset, None, ApiAttachments]
        if _attachments is None:
            attachments = None
        elif isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = ApiAttachments.from_dict(_attachments)

        api_item_update = cls(
            details=details,
            attachments=attachments,
        )

        return api_item_update
