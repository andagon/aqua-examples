from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_long_operation_archive import ApiItemLongOperationArchive


T = TypeVar("T", bound="ApiItemsPatchRequestArchive")


@attr.s(auto_attribs=True)
class ApiItemsPatchRequestArchive:
    """
    Attributes:
        operation_type (str):
        archive_operation (Union[Unset, None, ApiItemLongOperationArchive]): Represents request to batch archive (or un-
            archive) items.
    """

    operation_type: str
    archive_operation: Union[Unset, None, "ApiItemLongOperationArchive"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        archive_operation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.archive_operation, Unset):
            archive_operation = self.archive_operation.to_dict() if self.archive_operation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if archive_operation is not UNSET:
            field_dict["ArchiveOperation"] = archive_operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_long_operation_archive import ApiItemLongOperationArchive

        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        _archive_operation = d.pop("ArchiveOperation", UNSET)
        archive_operation: Union[Unset, None, ApiItemLongOperationArchive]
        if _archive_operation is None:
            archive_operation = None
        elif isinstance(_archive_operation, Unset):
            archive_operation = UNSET
        else:
            archive_operation = ApiItemLongOperationArchive.from_dict(_archive_operation)

        api_items_patch_request_archive = cls(
            operation_type=operation_type,
            archive_operation=archive_operation,
        )

        api_items_patch_request_archive.additional_properties = d
        return api_items_patch_request_archive

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
