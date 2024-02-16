from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCustomNotificationNew")


@attr.s(auto_attribs=True)
class ApiCustomNotificationNew:
    """A new email notification to be send to given users.

    Attributes:
        recipients (Union[Unset, None, List[int]]): List of recipients (ids of users)
        subject (Union[Unset, None, str]): Subject of the email to be send (plain text)
        body (Union[Unset, None, str]): Body of the email to be send (plain text)
    """

    recipients: Union[Unset, None, List[int]] = UNSET
    subject: Union[Unset, None, str] = UNSET
    body: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        recipients: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.recipients, Unset):
            if self.recipients is None:
                recipients = None
            else:
                recipients = self.recipients

        subject = self.subject
        body = self.body

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if recipients is not UNSET:
            field_dict["Recipients"] = recipients
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if body is not UNSET:
            field_dict["Body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        recipients = cast(List[int], d.pop("Recipients", UNSET))

        subject = d.pop("Subject", UNSET)

        body = d.pop("Body", UNSET)

        api_custom_notification_new = cls(
            recipients=recipients,
            subject=subject,
            body=body,
        )

        return api_custom_notification_new
