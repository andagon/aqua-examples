from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_execution_log_message_type import ApiExecutionLogMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value_date_time import ApiFieldValueDateTime


T = TypeVar("T", bound="ApiTestExecutionLog")


@attr.s(auto_attribs=True)
class ApiTestExecutionLog:
    """Represents single log of an automated test execution.

    Attributes:
        id (Union[Unset, int]):
        step_name (Union[Unset, None, str]):
        step_index (Union[Unset, int]):
        message (Union[Unset, None, str]):
        detailed_message (Union[Unset, None, str]):
        occurrence_time (Union[Unset, None, ApiFieldValueDateTime]):
        type (Union[Unset, ApiExecutionLogMessageType]): Identifies the type of log execution entry.
            This enum has the following values:
              - `ExecutionError`
              - `InformationalDebug`
              - `InformationalInfo`
              - `InformationalSuccess`
              - `InformationalWarn`
              - `PreparationError`
              - `ScriptExecutionError`
              - `SUTError`
        screen_shot_check_sum (Union[Unset, None, str]):
        category (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    step_name: Union[Unset, None, str] = UNSET
    step_index: Union[Unset, int] = UNSET
    message: Union[Unset, None, str] = UNSET
    detailed_message: Union[Unset, None, str] = UNSET
    occurrence_time: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    type: Union[Unset, ApiExecutionLogMessageType] = UNSET
    screen_shot_check_sum: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        step_name = self.step_name
        step_index = self.step_index
        message = self.message
        detailed_message = self.detailed_message
        occurrence_time: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.occurrence_time, Unset):
            occurrence_time = self.occurrence_time.to_dict() if self.occurrence_time else None

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        screen_shot_check_sum = self.screen_shot_check_sum
        category = self.category

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if step_name is not UNSET:
            field_dict["StepName"] = step_name
        if step_index is not UNSET:
            field_dict["StepIndex"] = step_index
        if message is not UNSET:
            field_dict["Message"] = message
        if detailed_message is not UNSET:
            field_dict["DetailedMessage"] = detailed_message
        if occurrence_time is not UNSET:
            field_dict["OccurrenceTime"] = occurrence_time
        if type is not UNSET:
            field_dict["Type"] = type
        if screen_shot_check_sum is not UNSET:
            field_dict["ScreenShotCheckSum"] = screen_shot_check_sum
        if category is not UNSET:
            field_dict["Category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_date_time import ApiFieldValueDateTime

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        step_name = d.pop("StepName", UNSET)

        step_index = d.pop("StepIndex", UNSET)

        message = d.pop("Message", UNSET)

        detailed_message = d.pop("DetailedMessage", UNSET)

        _occurrence_time = d.pop("OccurrenceTime", UNSET)
        occurrence_time: Union[Unset, None, ApiFieldValueDateTime]
        if _occurrence_time is None:
            occurrence_time = None
        elif isinstance(_occurrence_time, Unset):
            occurrence_time = UNSET
        else:
            occurrence_time = ApiFieldValueDateTime.from_dict(_occurrence_time)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiExecutionLogMessageType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiExecutionLogMessageType(_type)

        screen_shot_check_sum = d.pop("ScreenShotCheckSum", UNSET)

        category = d.pop("Category", UNSET)

        api_test_execution_log = cls(
            id=id,
            step_name=step_name,
            step_index=step_index,
            message=message,
            detailed_message=detailed_message,
            occurrence_time=occurrence_time,
            type=type,
            screen_shot_check_sum=screen_shot_check_sum,
            category=category,
        )

        return api_test_execution_log
