from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_long_operation import ApiLongOperation


T = TypeVar("T", bound="ApiProjectNewResponse")


@attr.s(auto_attribs=True)
class ApiProjectNewResponse:
    """Contains information about created project.

    Attributes:
        project_id (Union[Unset, int]): The id of the project.
        copy_items_long_operation (Union[Unset, None, ApiLongOperation]): Result of a REST API call that started long
            operation (asynchronous) to perform the actual job.
            Status of the task can be queried using GET System/LongOperation/{guid}/Status or GET
            System/LongOperation/{guid}
            In most cases it is also possible to be notified via SignalR when operation finishes.
    """

    project_id: Union[Unset, int] = UNSET
    copy_items_long_operation: Union[Unset, None, "ApiLongOperation"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        copy_items_long_operation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.copy_items_long_operation, Unset):
            copy_items_long_operation = (
                self.copy_items_long_operation.to_dict() if self.copy_items_long_operation else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if copy_items_long_operation is not UNSET:
            field_dict["CopyItemsLongOperation"] = copy_items_long_operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_long_operation import ApiLongOperation

        d = src_dict.copy()
        project_id = d.pop("ProjectId", UNSET)

        _copy_items_long_operation = d.pop("CopyItemsLongOperation", UNSET)
        copy_items_long_operation: Union[Unset, None, ApiLongOperation]
        if _copy_items_long_operation is None:
            copy_items_long_operation = None
        elif isinstance(_copy_items_long_operation, Unset):
            copy_items_long_operation = UNSET
        else:
            copy_items_long_operation = ApiLongOperation.from_dict(_copy_items_long_operation)

        api_project_new_response = cls(
            project_id=project_id,
            copy_items_long_operation=copy_items_long_operation,
        )

        return api_project_new_response
