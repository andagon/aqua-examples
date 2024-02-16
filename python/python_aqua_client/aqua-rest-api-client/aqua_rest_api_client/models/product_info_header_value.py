from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_header_value import ProductHeaderValue


T = TypeVar("T", bound="ProductInfoHeaderValue")


@attr.s(auto_attribs=True)
class ProductInfoHeaderValue:
    """
    Attributes:
        product (Union[Unset, None, ProductHeaderValue]):
        comment (Union[Unset, None, str]):
    """

    product: Union[Unset, None, "ProductHeaderValue"] = UNSET
    comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        product: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict() if self.product else None

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if product is not UNSET:
            field_dict["Product"] = product
        if comment is not UNSET:
            field_dict["Comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_header_value import ProductHeaderValue

        d = src_dict.copy()
        _product = d.pop("Product", UNSET)
        product: Union[Unset, None, ProductHeaderValue]
        if _product is None:
            product = None
        elif isinstance(_product, Unset):
            product = UNSET
        else:
            product = ProductHeaderValue.from_dict(_product)

        comment = d.pop("Comment", UNSET)

        product_info_header_value = cls(
            product=product,
            comment=comment,
        )

        return product_info_header_value
