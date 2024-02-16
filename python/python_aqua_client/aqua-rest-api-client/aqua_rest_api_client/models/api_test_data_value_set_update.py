from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_data_variable_with_value import ApiTestDataVariableWithValue


T = TypeVar("T", bound="ApiTestDataValueSetUpdate")


@attr.s(auto_attribs=True)
class ApiTestDataValueSetUpdate:
    """Contains information about updated value set (along with values).
    Variables ()number and names) must match existing test data.

        Attributes:
            value_set_name (Union[Unset, None, str]): The name of the value set.
            variables (Union[Unset, None, List['ApiTestDataVariableWithValue']]): The variables contained in this value set
                together with their
                values.
    """

    value_set_name: Union[Unset, None, str] = UNSET
    variables: Union[Unset, None, List["ApiTestDataVariableWithValue"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value_set_name = self.value_set_name
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
        field_dict.update({})
        if value_set_name is not UNSET:
            field_dict["ValueSetName"] = value_set_name
        if variables is not UNSET:
            field_dict["Variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_data_variable_with_value import ApiTestDataVariableWithValue

        d = src_dict.copy()
        value_set_name = d.pop("ValueSetName", UNSET)

        variables = []
        _variables = d.pop("Variables", UNSET)
        for variables_item_data in _variables or []:
            variables_item = ApiTestDataVariableWithValue.from_dict(variables_item_data)

            variables.append(variables_item)

        api_test_data_value_set_update = cls(
            value_set_name=value_set_name,
            variables=variables,
        )

        return api_test_data_value_set_update
