from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestDataValueSetInfo")


@attr.s(auto_attribs=True)
class ApiTestDataValueSetInfo:
    """Contains the meta data of a certain value set in the test data.

    Attributes:
        guid (Union[Unset, None, str]): The GUID of the value set.
        name (Union[Unset, None, str]): The name of the value set.
    """

    guid: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        name = d.pop("Name", UNSET)

        api_test_data_value_set_info = cls(
            guid=guid,
            name=name,
        )

        return api_test_data_value_set_info
