from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_long_operation_copy_in_project import ApiItemLongOperationCopyInProject


T = TypeVar("T", bound="ApiItemsPatchRequestCopyInProject")


@attr.s(auto_attribs=True)
class ApiItemsPatchRequestCopyInProject:
    """
    Attributes:
        operation_type (str):
        copy_operation (Union[Unset, None, ApiItemLongOperationCopyInProject]): Represents request to copy items to a
            given folder (in scope of the same project)
    """

    operation_type: str
    copy_operation: Union[Unset, None, "ApiItemLongOperationCopyInProject"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        copy_operation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.copy_operation, Unset):
            copy_operation = self.copy_operation.to_dict() if self.copy_operation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if copy_operation is not UNSET:
            field_dict["CopyOperation"] = copy_operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_long_operation_copy_in_project import ApiItemLongOperationCopyInProject

        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        _copy_operation = d.pop("CopyOperation", UNSET)
        copy_operation: Union[Unset, None, ApiItemLongOperationCopyInProject]
        if _copy_operation is None:
            copy_operation = None
        elif isinstance(_copy_operation, Unset):
            copy_operation = UNSET
        else:
            copy_operation = ApiItemLongOperationCopyInProject.from_dict(_copy_operation)

        api_items_patch_request_copy_in_project = cls(
            operation_type=operation_type,
            copy_operation=copy_operation,
        )

        api_items_patch_request_copy_in_project.additional_properties = d
        return api_items_patch_request_copy_in_project

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
