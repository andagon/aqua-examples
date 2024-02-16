from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_nested_test_case_variables_inheritance import ApiNestedTestCaseVariablesInheritance
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNestedTestCaseInfoNew")


@attr.s(auto_attribs=True)
class ApiNestedTestCaseInfoNew:
    """Contains information about nested test case.

    Attributes:
        id (Union[Unset, int]): The id of the nested test case, set the id only if the type is nested test case.
        nested_test_case_value_set_guid (Union[Unset, None, str]): The guid of the value set, set the guid only if the
            type is nested test case.
        nested_test_case_variables_inheritance (Union[Unset, ApiNestedTestCaseVariablesInheritance]): Identifies the
            source of variables.
            This enum has the following values:
              - `PreferNested` Variable source is from nested test case.
              - `PreferOuter` Variable source is from host test case.
    """

    id: Union[Unset, int] = UNSET
    nested_test_case_value_set_guid: Union[Unset, None, str] = UNSET
    nested_test_case_variables_inheritance: Union[Unset, ApiNestedTestCaseVariablesInheritance] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        nested_test_case_value_set_guid = self.nested_test_case_value_set_guid
        nested_test_case_variables_inheritance: Union[Unset, str] = UNSET
        if not isinstance(self.nested_test_case_variables_inheritance, Unset):
            nested_test_case_variables_inheritance = self.nested_test_case_variables_inheritance.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if nested_test_case_value_set_guid is not UNSET:
            field_dict["NestedTestCaseValueSetGuid"] = nested_test_case_value_set_guid
        if nested_test_case_variables_inheritance is not UNSET:
            field_dict["NestedTestCaseVariablesInheritance"] = nested_test_case_variables_inheritance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        nested_test_case_value_set_guid = d.pop("NestedTestCaseValueSetGuid", UNSET)

        _nested_test_case_variables_inheritance = d.pop("NestedTestCaseVariablesInheritance", UNSET)
        nested_test_case_variables_inheritance: Union[Unset, ApiNestedTestCaseVariablesInheritance]
        if isinstance(_nested_test_case_variables_inheritance, Unset):
            nested_test_case_variables_inheritance = UNSET
        else:
            nested_test_case_variables_inheritance = ApiNestedTestCaseVariablesInheritance(
                _nested_test_case_variables_inheritance
            )

        api_nested_test_case_info_new = cls(
            id=id,
            nested_test_case_value_set_guid=nested_test_case_value_set_guid,
            nested_test_case_variables_inheritance=nested_test_case_variables_inheritance,
        )

        return api_nested_test_case_info_new
