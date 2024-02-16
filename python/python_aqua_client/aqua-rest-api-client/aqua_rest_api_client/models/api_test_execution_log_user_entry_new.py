import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_execution_log_message_type import ApiExecutionLogMessageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestExecutionLogUserEntryNew")


@attr.s(auto_attribs=True)
class ApiTestExecutionLogUserEntryNew:
    """Contains the necessary information for creating a new
    execution log entry which was specified by an end user.

        Attributes:
            category (str): The category of the log message.
            message (str): The message of the log message
            type (ApiExecutionLogMessageType): Identifies the type of log execution entry.
                This enum has the following values:
                  - `ExecutionError`
                  - `InformationalDebug`
                  - `InformationalInfo`
                  - `InformationalSuccess`
                  - `InformationalWarn`
                  - `PreparationError`
                  - `ScriptExecutionError`
                  - `SUTError`
            detailed_message (Union[Unset, None, str]): A more detailed message with additional information
            occurrence_time (Union[Unset, None, datetime.datetime]): The time when the logged event occurred. When no time
                is
                provided, the current server time will be used.
    """

    category: str
    message: str
    type: ApiExecutionLogMessageType
    detailed_message: Union[Unset, None, str] = UNSET
    occurrence_time: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        message = self.message
        type = self.type.value

        detailed_message = self.detailed_message
        occurrence_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.occurrence_time, Unset):
            occurrence_time = self.occurrence_time.isoformat() if self.occurrence_time else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Category": category,
                "Message": message,
                "Type": type,
            }
        )
        if detailed_message is not UNSET:
            field_dict["DetailedMessage"] = detailed_message
        if occurrence_time is not UNSET:
            field_dict["OccurrenceTime"] = occurrence_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("Category")

        message = d.pop("Message")

        type = ApiExecutionLogMessageType(d.pop("Type"))

        detailed_message = d.pop("DetailedMessage", UNSET)

        _occurrence_time = d.pop("OccurrenceTime", UNSET)
        occurrence_time: Union[Unset, None, datetime.datetime]
        if _occurrence_time is None:
            occurrence_time = None
        elif isinstance(_occurrence_time, Unset):
            occurrence_time = UNSET
        else:
            occurrence_time = isoparse(_occurrence_time)

        api_test_execution_log_user_entry_new = cls(
            category=category,
            message=message,
            type=type,
            detailed_message=detailed_message,
            occurrence_time=occurrence_time,
        )

        return api_test_execution_log_user_entry_new
