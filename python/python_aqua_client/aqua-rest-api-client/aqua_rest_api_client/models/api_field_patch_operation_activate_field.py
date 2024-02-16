from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldPatchOperationActivateField")


@attr.s(auto_attribs=True)
class ApiFieldPatchOperationActivateField:
    """
    Attributes:
        field_id (str): The id of the field.
        patch_operation (str):
        item_type (Union[Unset, ApiItemType]): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
    """

    field_id: str
    patch_operation: str
    item_type: Union[Unset, ApiItemType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        patch_operation = self.patch_operation
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldId": field_id,
                "PatchOperation": patch_operation,
            }
        )
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId")

        patch_operation = d.pop("PatchOperation")

        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        api_field_patch_operation_activate_field = cls(
            field_id=field_id,
            patch_operation=patch_operation,
            item_type=item_type,
        )

        api_field_patch_operation_activate_field.additional_properties = d
        return api_field_patch_operation_activate_field

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
