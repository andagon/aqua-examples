from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLongOperation")


@attr.s(auto_attribs=True)
class ApiLongOperation:
    """Result of a REST API call that started long operation (asynchronous) to perform the actual job.
    Status of the task can be queried using GET System/LongOperation/{guid}/Status or GET System/LongOperation/{guid}
    In most cases it is also possible to be notified via SignalR when operation finishes.

        Attributes:
            long_running_task_guid (Union[Unset, None, str]): Id of the long running task. Can be used to query the progress
                (see GET /System/LongOperation/{guid}).
    """

    long_running_task_guid: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        long_running_task_guid = self.long_running_task_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if long_running_task_guid is not UNSET:
            field_dict["LongRunningTaskGuid"] = long_running_task_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        long_running_task_guid = d.pop("LongRunningTaskGuid", UNSET)

        api_long_operation = cls(
            long_running_task_guid=long_running_task_guid,
        )

        return api_long_operation
