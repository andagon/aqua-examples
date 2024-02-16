from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_execution_identifier import ApiTestExecutionIdentifier


T = TypeVar("T", bound="ApiTestExecutionNewResponseTestScenarioContext")


@attr.s(auto_attribs=True)
class ApiTestExecutionNewResponseTestScenarioContext:
    """
    Attributes:
        context (str):
        test_scenario_execution_id (Union[Unset, int]): The id of the testscenario execution.
        test_execution_identifiers (Union[Unset, None, List['ApiTestExecutionIdentifier']]): List of related test
            executions.
    """

    context: str
    test_scenario_execution_id: Union[Unset, int] = UNSET
    test_execution_identifiers: Union[Unset, None, List["ApiTestExecutionIdentifier"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context
        test_scenario_execution_id = self.test_scenario_execution_id
        test_execution_identifiers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.test_execution_identifiers, Unset):
            if self.test_execution_identifiers is None:
                test_execution_identifiers = None
            else:
                test_execution_identifiers = []
                for test_execution_identifiers_item_data in self.test_execution_identifiers:
                    test_execution_identifiers_item = test_execution_identifiers_item_data.to_dict()

                    test_execution_identifiers.append(test_execution_identifiers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Context": context,
            }
        )
        if test_scenario_execution_id is not UNSET:
            field_dict["TestScenarioExecutionId"] = test_scenario_execution_id
        if test_execution_identifiers is not UNSET:
            field_dict["TestExecutionIdentifiers"] = test_execution_identifiers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_execution_identifier import ApiTestExecutionIdentifier

        d = src_dict.copy()
        context = d.pop("Context")

        test_scenario_execution_id = d.pop("TestScenarioExecutionId", UNSET)

        test_execution_identifiers = []
        _test_execution_identifiers = d.pop("TestExecutionIdentifiers", UNSET)
        for test_execution_identifiers_item_data in _test_execution_identifiers or []:
            test_execution_identifiers_item = ApiTestExecutionIdentifier.from_dict(test_execution_identifiers_item_data)

            test_execution_identifiers.append(test_execution_identifiers_item)

        api_test_execution_new_response_test_scenario_context = cls(
            context=context,
            test_scenario_execution_id=test_scenario_execution_id,
            test_execution_identifiers=test_execution_identifiers,
        )

        api_test_execution_new_response_test_scenario_context.additional_properties = d
        return api_test_execution_new_response_test_scenario_context

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
