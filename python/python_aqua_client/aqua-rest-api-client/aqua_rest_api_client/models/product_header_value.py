from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductHeaderValue")


@attr.s(auto_attribs=True)
class ProductHeaderValue:
    """
    Attributes:
        name (Union[Unset, None, str]):
        version (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if version is not UNSET:
            field_dict["Version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        version = d.pop("Version", UNSET)

        product_header_value = cls(
            name=name,
            version=version,
        )

        return product_header_value
