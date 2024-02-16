from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiTestDataUpdate")


@attr.s(auto_attribs=True)
class ApiTestDataUpdate:
    """Base class for updated test data of a test case.
    This class is abstract, not intended to be used directly.

        Attributes:
            variant (str):
    """

    variant: str

    def to_dict(self) -> Dict[str, Any]:
        variant = self.variant

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Variant": variant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        variant = d.pop("Variant")

        api_test_data_update = cls(
            variant=variant,
        )

        return api_test_data_update
