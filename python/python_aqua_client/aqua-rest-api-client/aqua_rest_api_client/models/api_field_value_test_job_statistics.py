from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_job_statistics_entry import ApiTestJobStatisticsEntry


T = TypeVar("T", bound="ApiFieldValueTestJobStatistics")


@attr.s(auto_attribs=True)
class ApiFieldValueTestJobStatistics:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
        value (Union[Unset, None, List['ApiTestJobStatisticsEntry']]):
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, List["ApiTestJobStatisticsEntry"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text
        value: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.value, Unset):
            if self.value is None:
                value = None
            else:
                value = []
                for value_item_data in self.value:
                    value_item = value_item_data.to_dict()

                    value.append(value_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldValueType": field_value_type,
            }
        )
        if text is not UNSET:
            field_dict["Text"] = text
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_job_statistics_entry import ApiTestJobStatisticsEntry

        d = src_dict.copy()
        field_value_type = d.pop("FieldValueType")

        text = d.pop("Text", UNSET)

        value = []
        _value = d.pop("Value", UNSET)
        for value_item_data in _value or []:
            value_item = ApiTestJobStatisticsEntry.from_dict(value_item_data)

            value.append(value_item)

        api_field_value_test_job_statistics = cls(
            field_value_type=field_value_type,
            text=text,
            value=value,
        )

        api_field_value_test_job_statistics.additional_properties = d
        return api_field_value_test_job_statistics

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
