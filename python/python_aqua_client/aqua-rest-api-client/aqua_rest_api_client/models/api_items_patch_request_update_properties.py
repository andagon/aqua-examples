from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_long_operation_update_properties import ApiItemLongOperationUpdateProperties


T = TypeVar("T", bound="ApiItemsPatchRequestUpdateProperties")


@attr.s(auto_attribs=True)
class ApiItemsPatchRequestUpdateProperties:
    """
    Attributes:
        operation_type (str):
        update_properties_operation (Union[Unset, None, ApiItemLongOperationUpdateProperties]): Represents request to
            batch update items (update properties).
    """

    operation_type: str
    update_properties_operation: Union[Unset, None, "ApiItemLongOperationUpdateProperties"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        update_properties_operation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.update_properties_operation, Unset):
            update_properties_operation = (
                self.update_properties_operation.to_dict() if self.update_properties_operation else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if update_properties_operation is not UNSET:
            field_dict["UpdatePropertiesOperation"] = update_properties_operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_long_operation_update_properties import ApiItemLongOperationUpdateProperties

        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        _update_properties_operation = d.pop("UpdatePropertiesOperation", UNSET)
        update_properties_operation: Union[Unset, None, ApiItemLongOperationUpdateProperties]
        if _update_properties_operation is None:
            update_properties_operation = None
        elif isinstance(_update_properties_operation, Unset):
            update_properties_operation = UNSET
        else:
            update_properties_operation = ApiItemLongOperationUpdateProperties.from_dict(_update_properties_operation)

        api_items_patch_request_update_properties = cls(
            operation_type=operation_type,
            update_properties_operation=update_properties_operation,
        )

        api_items_patch_request_update_properties.additional_properties = d
        return api_items_patch_request_update_properties

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
