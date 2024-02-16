from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestDataUpdateValueSet")


@attr.s(auto_attribs=True)
class ApiTestDataUpdateValueSet:
    """Contains the meta data of a certain value set in the test data.

    Attributes:
        name (str): The name of the value set.
        guid (Union[Unset, None, str]): The GUID of the value set.
            Must be null for newly created values sets.
    """

    name: str
    guid: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        guid = self.guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Name": name,
            }
        )
        if guid is not UNSET:
            field_dict["Guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        guid = d.pop("Guid", UNSET)

        api_test_data_update_value_set = cls(
            name=name,
            guid=guid,
        )

        return api_test_data_update_value_set
