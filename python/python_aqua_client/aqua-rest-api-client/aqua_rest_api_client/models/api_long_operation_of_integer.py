from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLongOperationOfInteger")


@attr.s(auto_attribs=True)
class ApiLongOperationOfInteger:
    """Result of a REST API call that started long operation (asynchronous) to perform the actual job.
    When LongRunningTaskGuid is null this indicates a situation when REST API was able to process the task without
    starting asynchronous job.
    Then the actual result is returned in Result field.

        Attributes:
            long_running_task_guid (Union[Unset, None, str]): Id of the long running task. Can be used to query the progress
                (see GET /System/LongOperation/{guid}).
                If empty indicates the long operation has not been started and actual result is immediately available in the
                Result field.
            result (Union[Unset, int]): Filled only when LongRunningTaskGuid is not provided. Contains actual, immediate
                result of the call.
    """

    long_running_task_guid: Union[Unset, None, str] = UNSET
    result: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        long_running_task_guid = self.long_running_task_guid
        result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if long_running_task_guid is not UNSET:
            field_dict["LongRunningTaskGuid"] = long_running_task_guid
        if result is not UNSET:
            field_dict["Result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        long_running_task_guid = d.pop("LongRunningTaskGuid", UNSET)

        result = d.pop("Result", UNSET)

        api_long_operation_of_integer = cls(
            long_running_task_guid=long_running_task_guid,
            result=result,
        )

        return api_long_operation_of_integer
