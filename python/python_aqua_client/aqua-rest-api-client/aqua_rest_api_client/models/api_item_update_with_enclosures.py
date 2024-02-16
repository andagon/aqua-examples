from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachments import ApiAttachments
    from ..models.api_enclosures_update import ApiEnclosuresUpdate
    from ..models.api_field_update import ApiFieldUpdate


T = TypeVar("T", bound="ApiItemUpdateWithEnclosures")


@attr.s(auto_attribs=True)
class ApiItemUpdateWithEnclosures:
    """
    Attributes:
        details (Union[Unset, None, List['ApiFieldUpdate']]): The list of updates to perform on the different fields of
            the item.
        attachments (Union[Unset, None, ApiAttachments]): Contains all changes to the attachments of an item.
        enclosures (Union[Unset, None, ApiEnclosuresUpdate]): Contains a list of different changes which should be
            applied to the
            enclosure collection.
    """

    details: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET
    attachments: Union[Unset, None, "ApiAttachments"] = UNSET
    enclosures: Union[Unset, None, "ApiEnclosuresUpdate"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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

        enclosures: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.enclosures, Unset):
            enclosures = self.enclosures.to_dict() if self.enclosures else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["Details"] = details
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments
        if enclosures is not UNSET:
            field_dict["Enclosures"] = enclosures

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachments import ApiAttachments
        from ..models.api_enclosures_update import ApiEnclosuresUpdate
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

        _enclosures = d.pop("Enclosures", UNSET)
        enclosures: Union[Unset, None, ApiEnclosuresUpdate]
        if _enclosures is None:
            enclosures = None
        elif isinstance(_enclosures, Unset):
            enclosures = UNSET
        else:
            enclosures = ApiEnclosuresUpdate.from_dict(_enclosures)

        api_item_update_with_enclosures = cls(
            details=details,
            attachments=attachments,
            enclosures=enclosures,
        )

        api_item_update_with_enclosures.additional_properties = d
        return api_item_update_with_enclosures

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
