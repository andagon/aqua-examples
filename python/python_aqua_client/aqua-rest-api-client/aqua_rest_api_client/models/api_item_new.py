from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachment_new import ApiAttachmentNew
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_item_location_update import ApiItemLocationUpdate


T = TypeVar("T", bound="ApiItemNew")


@attr.s(auto_attribs=True)
class ApiItemNew:
    """Contains the necessary data to create a new item.

    Attributes:
        location (Union[Unset, None, ApiItemLocationUpdate]):
        details (Union[Unset, None, List['ApiFieldUpdate']]): The list values which should be set when creating the
            item.
        attachments (Union[Unset, None, List['ApiAttachmentNew']]): The list of attachments which should be added to the
            new item.
    """

    location: Union[Unset, None, "ApiItemLocationUpdate"] = UNSET
    details: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET
    attachments: Union[Unset, None, List["ApiAttachmentNew"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        details: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            if self.details is None:
                details = None
            else:
                details = []
                for details_item_data in self.details:
                    details_item = details_item_data.to_dict()

                    details.append(details_item)

        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if location is not UNSET:
            field_dict["Location"] = location
        if details is not UNSET:
            field_dict["Details"] = details
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachment_new import ApiAttachmentNew
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_item_location_update import ApiItemLocationUpdate

        d = src_dict.copy()
        _location = d.pop("Location", UNSET)
        location: Union[Unset, None, ApiItemLocationUpdate]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = ApiItemLocationUpdate.from_dict(_location)

        details = []
        _details = d.pop("Details", UNSET)
        for details_item_data in _details or []:
            details_item = ApiFieldUpdate.from_dict(details_item_data)

            details.append(details_item)

        attachments = []
        _attachments = d.pop("Attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = ApiAttachmentNew.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        api_item_new = cls(
            location=location,
            details=details,
            attachments=attachments,
        )

        return api_item_new
