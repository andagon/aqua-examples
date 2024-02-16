from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestDataReferencedValueSetInfo")


@attr.s(auto_attribs=True)
class ApiTestDataReferencedValueSetInfo:
    """Contains the meta data of certain value set which is referenced
    somewhere (e.g. test step or test job).

        Attributes:
            guid (Union[Unset, None, str]): The GUID of the value set.
            name (Union[Unset, None, str]): The name of the value set. Is null, when the
                value set has been deleted.
            deleted (Union[Unset, bool]): Indicates whether the value set has been deleted.
    """

    guid: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    deleted: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        name = self.name
        deleted = self.deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if name is not UNSET:
            field_dict["Name"] = name
        if deleted is not UNSET:
            field_dict["Deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        name = d.pop("Name", UNSET)

        deleted = d.pop("Deleted", UNSET)

        api_test_data_referenced_value_set_info = cls(
            guid=guid,
            name=name,
            deleted=deleted,
        )

        return api_test_data_referenced_value_set_info
