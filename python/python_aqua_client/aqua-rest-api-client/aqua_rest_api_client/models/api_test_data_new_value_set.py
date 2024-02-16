from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiTestDataNewValueSet")


@attr.s(auto_attribs=True)
class ApiTestDataNewValueSet:
    """Contains the meta data of a value set to be created in the test data.

    Attributes:
        name (str): The name of the value set.
    """

    name: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        api_test_data_new_value_set = cls(
            name=name,
        )

        return api_test_data_new_value_set
