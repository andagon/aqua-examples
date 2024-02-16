from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestExecutionIdentifier")


@attr.s(auto_attribs=True)
class ApiTestExecutionIdentifier:
    """
    Attributes:
        id (Union[Unset, int]): The id of the item
        formatted_id (Union[Unset, None, str]): A nicely formatted version of the id which
            contains the item type identifier and the numerical
            id padded to six digits. E.g.: RQ004242.
            This id is only for presentation. You must use the
            numerical id for all requests.
        type (Union[Unset, ApiItemType]): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
    """

    id: Union[Unset, int] = UNSET
    formatted_id: Union[Unset, None, str] = UNSET
    type: Union[Unset, ApiItemType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        formatted_id = self.formatted_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if formatted_id is not UNSET:
            field_dict["FormattedId"] = formatted_id
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        formatted_id = d.pop("FormattedId", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiItemType(_type)

        api_test_execution_identifier = cls(
            id=id,
            formatted_id=formatted_id,
            type=type,
        )

        api_test_execution_identifier.additional_properties = d
        return api_test_execution_identifier

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
