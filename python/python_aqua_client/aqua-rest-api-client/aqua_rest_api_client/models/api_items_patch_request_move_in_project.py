from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_long_operation_move_in_project import ApiItemLongOperationMoveInProject


T = TypeVar("T", bound="ApiItemsPatchRequestMoveInProject")


@attr.s(auto_attribs=True)
class ApiItemsPatchRequestMoveInProject:
    """
    Attributes:
        operation_type (str):
        move_operation (Union[Unset, None, ApiItemLongOperationMoveInProject]): Represents request to move items to a
            given folder (in scope of the same project)
    """

    operation_type: str
    move_operation: Union[Unset, None, "ApiItemLongOperationMoveInProject"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        move_operation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.move_operation, Unset):
            move_operation = self.move_operation.to_dict() if self.move_operation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if move_operation is not UNSET:
            field_dict["MoveOperation"] = move_operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_long_operation_move_in_project import ApiItemLongOperationMoveInProject

        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        _move_operation = d.pop("MoveOperation", UNSET)
        move_operation: Union[Unset, None, ApiItemLongOperationMoveInProject]
        if _move_operation is None:
            move_operation = None
        elif isinstance(_move_operation, Unset):
            move_operation = UNSET
        else:
            move_operation = ApiItemLongOperationMoveInProject.from_dict(_move_operation)

        api_items_patch_request_move_in_project = cls(
            operation_type=operation_type,
            move_operation=move_operation,
        )

        api_items_patch_request_move_in_project.additional_properties = d
        return api_items_patch_request_move_in_project

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
