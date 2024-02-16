from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemVersion")


@attr.s(auto_attribs=True)
class ApiItemVersion:
    """Version information for an item.

    Attributes:
        version (Union[Unset, int]): The version of the item. This version field is incremented each time
            the item is modified.
        operation_number (Union[Unset, int]): This field is incremented when the item itself was not modified
            but the information in some system-managed fields changed.
        sub_operation_number (Union[Unset, int]): The same as OperationNumber but for changes which are
            less important and do not increment the operation number.
    """

    version: Union[Unset, int] = UNSET
    operation_number: Union[Unset, int] = UNSET
    sub_operation_number: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        operation_number = self.operation_number
        sub_operation_number = self.sub_operation_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version
        if operation_number is not UNSET:
            field_dict["OperationNumber"] = operation_number
        if sub_operation_number is not UNSET:
            field_dict["SubOperationNumber"] = sub_operation_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("Version", UNSET)

        operation_number = d.pop("OperationNumber", UNSET)

        sub_operation_number = d.pop("SubOperationNumber", UNSET)

        api_item_version = cls(
            version=version,
            operation_number=operation_number,
            sub_operation_number=sub_operation_number,
        )

        return api_item_version
