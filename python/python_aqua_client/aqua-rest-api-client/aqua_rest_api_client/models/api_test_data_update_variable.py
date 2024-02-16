from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiTestDataUpdateVariable")


@attr.s(auto_attribs=True)
class ApiTestDataUpdateVariable:
    """Contains the meta data of a certain variable in the test data.

    Attributes:
        name (str): The variable name.
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

        api_test_data_update_variable = cls(
            name=name,
        )

        return api_test_data_update_variable
