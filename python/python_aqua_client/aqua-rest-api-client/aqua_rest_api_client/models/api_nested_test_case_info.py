from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_base_item_accessibility import ApiBaseItemAccessibility
from ..models.api_nested_test_case_variables_inheritance import ApiNestedTestCaseVariablesInheritance
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_data_referenced_value_set_info import ApiTestDataReferencedValueSetInfo


T = TypeVar("T", bound="ApiNestedTestCaseInfo")


@attr.s(auto_attribs=True)
class ApiNestedTestCaseInfo:
    """Contains information about nested test case.

    Attributes:
        nested_test_case_accessibility (Union[Unset, ApiBaseItemAccessibility]): Identifies the test case accessibility.
            This enum has the following values:
              - `Accessible` The test case is accessible.
              - `Archived` The test case is archived
              - `Deleted` The test case is deleted.
              - `NoPermissions` No permissions to access the test case.
        has_variables (Union[Unset, None, bool]): No set if NestedTestCaseAccessibility is set to NoPermissions, true if
            test case contains any variables otherwise false.
        id (Union[Unset, int]): The id of the nested test case, set the id only if the type is nested test case.
        name (Union[Unset, None, str]): The name of the nested test case.
        nested_test_case_value_set (Union[Unset, None, ApiTestDataReferencedValueSetInfo]): Contains the meta data of
            certain value set which is referenced
            somewhere (e.g. test step or test job).
        nested_test_case_variables_inheritance (Union[Unset, ApiNestedTestCaseVariablesInheritance]): Identifies the
            source of variables.
            This enum has the following values:
              - `PreferNested` Variable source is from nested test case.
              - `PreferOuter` Variable source is from host test case.
    """

    nested_test_case_accessibility: Union[Unset, ApiBaseItemAccessibility] = UNSET
    has_variables: Union[Unset, None, bool] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    nested_test_case_value_set: Union[Unset, None, "ApiTestDataReferencedValueSetInfo"] = UNSET
    nested_test_case_variables_inheritance: Union[Unset, ApiNestedTestCaseVariablesInheritance] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        nested_test_case_accessibility: Union[Unset, str] = UNSET
        if not isinstance(self.nested_test_case_accessibility, Unset):
            nested_test_case_accessibility = self.nested_test_case_accessibility.value

        has_variables = self.has_variables
        id = self.id
        name = self.name
        nested_test_case_value_set: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.nested_test_case_value_set, Unset):
            nested_test_case_value_set = (
                self.nested_test_case_value_set.to_dict() if self.nested_test_case_value_set else None
            )

        nested_test_case_variables_inheritance: Union[Unset, str] = UNSET
        if not isinstance(self.nested_test_case_variables_inheritance, Unset):
            nested_test_case_variables_inheritance = self.nested_test_case_variables_inheritance.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if nested_test_case_accessibility is not UNSET:
            field_dict["NestedTestCaseAccessibility"] = nested_test_case_accessibility
        if has_variables is not UNSET:
            field_dict["HasVariables"] = has_variables
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if nested_test_case_value_set is not UNSET:
            field_dict["NestedTestCaseValueSet"] = nested_test_case_value_set
        if nested_test_case_variables_inheritance is not UNSET:
            field_dict["NestedTestCaseVariablesInheritance"] = nested_test_case_variables_inheritance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_data_referenced_value_set_info import ApiTestDataReferencedValueSetInfo

        d = src_dict.copy()
        _nested_test_case_accessibility = d.pop("NestedTestCaseAccessibility", UNSET)
        nested_test_case_accessibility: Union[Unset, ApiBaseItemAccessibility]
        if isinstance(_nested_test_case_accessibility, Unset):
            nested_test_case_accessibility = UNSET
        else:
            nested_test_case_accessibility = ApiBaseItemAccessibility(_nested_test_case_accessibility)

        has_variables = d.pop("HasVariables", UNSET)

        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        _nested_test_case_value_set = d.pop("NestedTestCaseValueSet", UNSET)
        nested_test_case_value_set: Union[Unset, None, ApiTestDataReferencedValueSetInfo]
        if _nested_test_case_value_set is None:
            nested_test_case_value_set = None
        elif isinstance(_nested_test_case_value_set, Unset):
            nested_test_case_value_set = UNSET
        else:
            nested_test_case_value_set = ApiTestDataReferencedValueSetInfo.from_dict(_nested_test_case_value_set)

        _nested_test_case_variables_inheritance = d.pop("NestedTestCaseVariablesInheritance", UNSET)
        nested_test_case_variables_inheritance: Union[Unset, ApiNestedTestCaseVariablesInheritance]
        if isinstance(_nested_test_case_variables_inheritance, Unset):
            nested_test_case_variables_inheritance = UNSET
        else:
            nested_test_case_variables_inheritance = ApiNestedTestCaseVariablesInheritance(
                _nested_test_case_variables_inheritance
            )

        api_nested_test_case_info = cls(
            nested_test_case_accessibility=nested_test_case_accessibility,
            has_variables=has_variables,
            id=id,
            name=name,
            nested_test_case_value_set=nested_test_case_value_set,
            nested_test_case_variables_inheritance=nested_test_case_variables_inheritance,
        )

        return api_nested_test_case_info
