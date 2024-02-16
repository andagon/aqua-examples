from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestDataVariable")


@attr.s(auto_attribs=True)
class ApiTestDataVariable:
    """Contains the meta data of a certain variable in the test data.

    Attributes:
        name (Union[Unset, None, str]): The variable name.
    """

    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        api_test_data_variable = cls(
            name=name,
        )

        return api_test_data_variable
