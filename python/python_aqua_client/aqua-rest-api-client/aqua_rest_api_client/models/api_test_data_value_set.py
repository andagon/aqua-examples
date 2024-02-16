from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_data_variable_with_value import ApiTestDataVariableWithValue


T = TypeVar("T", bound="ApiTestDataValueSet")


@attr.s(auto_attribs=True)
class ApiTestDataValueSet:
    """
    Attributes:
        guid (Union[Unset, None, str]): The GUID of the value set.
        name (Union[Unset, None, str]): The name of the value set.
        variables (Union[Unset, None, List['ApiTestDataVariableWithValue']]): The variables contained in this value set
            together with their
            values.
    """

    guid: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    variables: Union[Unset, None, List["ApiTestDataVariableWithValue"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        name = self.name
        variables: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.variables, Unset):
            if self.variables is None:
                variables = None
            else:
                variables = []
                for variables_item_data in self.variables:
                    variables_item = variables_item_data.to_dict()

                    variables.append(variables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if name is not UNSET:
            field_dict["Name"] = name
        if variables is not UNSET:
            field_dict["Variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_data_variable_with_value import ApiTestDataVariableWithValue

        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        name = d.pop("Name", UNSET)

        variables = []
        _variables = d.pop("Variables", UNSET)
        for variables_item_data in _variables or []:
            variables_item = ApiTestDataVariableWithValue.from_dict(variables_item_data)

            variables.append(variables_item)

        api_test_data_value_set = cls(
            guid=guid,
            name=name,
            variables=variables,
        )

        api_test_data_value_set.additional_properties = d
        return api_test_data_value_set

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
