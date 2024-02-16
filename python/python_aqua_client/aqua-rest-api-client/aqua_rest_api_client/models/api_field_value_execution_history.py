from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_case_execution_history import ApiTestCaseExecutionHistory


T = TypeVar("T", bound="ApiFieldValueExecutionHistory")


@attr.s(auto_attribs=True)
class ApiFieldValueExecutionHistory:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
        value (Union[Unset, None, ApiTestCaseExecutionHistory]): Historic information regarding the last executions
            of a test case or test job.
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, "ApiTestCaseExecutionHistory"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text
        value: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict() if self.value else None

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
        from ..models.api_test_case_execution_history import ApiTestCaseExecutionHistory

        d = src_dict.copy()
        field_value_type = d.pop("FieldValueType")

        text = d.pop("Text", UNSET)

        _value = d.pop("Value", UNSET)
        value: Union[Unset, None, ApiTestCaseExecutionHistory]
        if _value is None:
            value = None
        elif isinstance(_value, Unset):
            value = UNSET
        else:
            value = ApiTestCaseExecutionHistory.from_dict(_value)

        api_field_value_execution_history = cls(
            field_value_type=field_value_type,
            text=text,
            value=value,
        )

        api_field_value_execution_history.additional_properties = d
        return api_field_value_execution_history

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
