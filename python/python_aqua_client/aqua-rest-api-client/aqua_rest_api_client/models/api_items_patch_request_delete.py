from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_long_operation_delete import ApiItemLongOperationDelete


T = TypeVar("T", bound="ApiItemsPatchRequestDelete")


@attr.s(auto_attribs=True)
class ApiItemsPatchRequestDelete:
    """
    Attributes:
        operation_type (str):
        delete_operation (Union[Unset, None, ApiItemLongOperationDelete]): Represents request to batch delete items.
    """

    operation_type: str
    delete_operation: Union[Unset, None, "ApiItemLongOperationDelete"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        delete_operation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.delete_operation, Unset):
            delete_operation = self.delete_operation.to_dict() if self.delete_operation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if delete_operation is not UNSET:
            field_dict["DeleteOperation"] = delete_operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_long_operation_delete import ApiItemLongOperationDelete

        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        _delete_operation = d.pop("DeleteOperation", UNSET)
        delete_operation: Union[Unset, None, ApiItemLongOperationDelete]
        if _delete_operation is None:
            delete_operation = None
        elif isinstance(_delete_operation, Unset):
            delete_operation = UNSET
        else:
            delete_operation = ApiItemLongOperationDelete.from_dict(_delete_operation)

        api_items_patch_request_delete = cls(
            operation_type=operation_type,
            delete_operation=delete_operation,
        )

        api_items_patch_request_delete.additional_properties = d
        return api_items_patch_request_delete

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
