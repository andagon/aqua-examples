from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_project_notification_type import ApiProjectNotificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectNotificationTemplate")


@attr.s(auto_attribs=True)
class ApiProjectNotificationTemplate:
    """Represents a single notification template in a project

    Attributes:
        subject (Union[Unset, None, str]): Subject line pattern
        body (Union[Unset, None, str]): Email body pattern (html)
        culture_name (Union[Unset, None, str]): Language of this template (to be used for expanding values like e.g.
            item type).
            It is expected that all templates in a project are configured with same language.
            Accepted values are "en-GB" and "de-DE".
        id (Union[Unset, int]): Id of this notification template.
        type (Union[Unset, ApiProjectNotificationType]): The type of notification.
            This enum has the following values:
              - `BaseObjectChangedProperties` Any change of base object property.
              - `BaseObjectChangedStatus` Base object's status field has changed
              - `BaseObjectCreated` Base object has been created.
              - `BaseObjectDeleted` Base object has been deleted.
              - `BaseObjectMoved` Base object has been moved between folders.
        max_name_length (Union[Unset, int]): Specifies maximum length of item's name when included in Subject line.
            If actual name is longer than this value then it is cut off with "..."
    """

    subject: Union[Unset, None, str] = UNSET
    body: Union[Unset, None, str] = UNSET
    culture_name: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    type: Union[Unset, ApiProjectNotificationType] = UNSET
    max_name_length: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        body = self.body
        culture_name = self.culture_name
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        max_name_length = self.max_name_length

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if body is not UNSET:
            field_dict["Body"] = body
        if culture_name is not UNSET:
            field_dict["CultureName"] = culture_name
        if id is not UNSET:
            field_dict["Id"] = id
        if type is not UNSET:
            field_dict["Type"] = type
        if max_name_length is not UNSET:
            field_dict["MaxNameLength"] = max_name_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject = d.pop("Subject", UNSET)

        body = d.pop("Body", UNSET)

        culture_name = d.pop("CultureName", UNSET)

        id = d.pop("Id", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiProjectNotificationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiProjectNotificationType(_type)

        max_name_length = d.pop("MaxNameLength", UNSET)

        api_project_notification_template = cls(
            subject=subject,
            body=body,
            culture_name=culture_name,
            id=id,
            type=type,
            max_name_length=max_name_length,
        )

        return api_project_notification_template
