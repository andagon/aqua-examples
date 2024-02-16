from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

import attr

if TYPE_CHECKING:
    from ..models.api_test_data_update_value_set import ApiTestDataUpdateValueSet
    from ..models.api_test_data_update_variable import ApiTestDataUpdateVariable


T = TypeVar("T", bound="ApiTestDataUpdateLocal")


@attr.s(auto_attribs=True)
class ApiTestDataUpdateLocal:
    """
    Attributes:
        variant (str):
        value_sets (List['ApiTestDataUpdateValueSet']): The value sets which are part of the test data.
        variables (List['ApiTestDataUpdateVariable']): The variables which are part of the test data.
        values (List[List[str]]): The actual values contained in the test data. The table
            is a two-dimensional array which contains for each value
            set a list of values. The data is ordered according to
            the ValueSets and Variables list.
    """

    variant: str
    value_sets: List["ApiTestDataUpdateValueSet"]
    variables: List["ApiTestDataUpdateVariable"]
    values: List[List[str]]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variant = self.variant
        value_sets = []
        for value_sets_item_data in self.value_sets:
            value_sets_item = value_sets_item_data.to_dict()

            value_sets.append(value_sets_item)

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()

            variables.append(variables_item)

        values = []
        for values_item_data in self.values:
            values_item = values_item_data

            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Variant": variant,
                "ValueSets": value_sets,
                "Variables": variables,
                "Values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_data_update_value_set import ApiTestDataUpdateValueSet
        from ..models.api_test_data_update_variable import ApiTestDataUpdateVariable

        d = src_dict.copy()
        variant = d.pop("Variant")

        value_sets = []
        _value_sets = d.pop("ValueSets")
        for value_sets_item_data in _value_sets:
            value_sets_item = ApiTestDataUpdateValueSet.from_dict(value_sets_item_data)

            value_sets.append(value_sets_item)

        variables = []
        _variables = d.pop("Variables")
        for variables_item_data in _variables:
            variables_item = ApiTestDataUpdateVariable.from_dict(variables_item_data)

            variables.append(variables_item)

        values = []
        _values = d.pop("Values")
        for values_item_data in _values:
            values_item = cast(List[str], values_item_data)

            values.append(values_item)

        api_test_data_update_local = cls(
            variant=variant,
            value_sets=value_sets,
            variables=variables,
            values=values,
        )

        api_test_data_update_local.additional_properties = d
        return api_test_data_update_local

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
