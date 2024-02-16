from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserPatchPosition")


@attr.s(auto_attribs=True)
class ApiUserPatchPosition:
    """
    Attributes:
        patch_operation (str):
        position (Union[Unset, None, str]): The position text to set
    """

    patch_operation: str
    position: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_operation = self.patch_operation
        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PatchOperation": patch_operation,
            }
        )
        if position is not UNSET:
            field_dict["Position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_operation = d.pop("PatchOperation")

        position = d.pop("Position", UNSET)

        api_user_patch_position = cls(
            patch_operation=patch_operation,
            position=position,
        )

        api_user_patch_position.additional_properties = d
        return api_user_patch_position

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
