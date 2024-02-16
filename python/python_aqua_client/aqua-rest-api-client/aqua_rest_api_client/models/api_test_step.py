from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_test_step_type import ApiTestStepType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_automation import ApiAutomation
    from ..models.api_nested_test_case_info import ApiNestedTestCaseInfo
    from ..models.api_rich_text import ApiRichText


T = TypeVar("T", bound="ApiTestStep")


@attr.s(auto_attribs=True)
class ApiTestStep:
    """
    Attributes:
        name (Union[Unset, None, str]): Test step name.
        index (Union[Unset, int]): The index of this test step.
        description (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
        expected_result (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
        actual_result_template (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in
            several different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
        step_type (Union[Unset, ApiTestStepType]): Identifies the type of an execution.
            This enum has the following values:
              - `Condition` Represents 'condition'
              - `NestedTestCase` Only for internal use.
              - `Step` Represents 'step'
        id (Union[Unset, int]): The id of the test step.
        automation (Union[Unset, None, ApiAutomation]): Automation part of a test step, as used when loading data.
        nested_test_case (Union[Unset, None, ApiNestedTestCaseInfo]): Contains information about nested test case.
    """

    name: Union[Unset, None, str] = UNSET
    index: Union[Unset, int] = UNSET
    description: Union[Unset, None, "ApiRichText"] = UNSET
    expected_result: Union[Unset, None, "ApiRichText"] = UNSET
    actual_result_template: Union[Unset, None, "ApiRichText"] = UNSET
    step_type: Union[Unset, ApiTestStepType] = UNSET
    id: Union[Unset, int] = UNSET
    automation: Union[Unset, None, "ApiAutomation"] = UNSET
    nested_test_case: Union[Unset, None, "ApiNestedTestCaseInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        index = self.index
        description: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict() if self.description else None

        expected_result: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.expected_result, Unset):
            expected_result = self.expected_result.to_dict() if self.expected_result else None

        actual_result_template: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.actual_result_template, Unset):
            actual_result_template = self.actual_result_template.to_dict() if self.actual_result_template else None

        step_type: Union[Unset, str] = UNSET
        if not isinstance(self.step_type, Unset):
            step_type = self.step_type.value

        id = self.id
        automation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.automation, Unset):
            automation = self.automation.to_dict() if self.automation else None

        nested_test_case: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.nested_test_case, Unset):
            nested_test_case = self.nested_test_case.to_dict() if self.nested_test_case else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if index is not UNSET:
            field_dict["Index"] = index
        if description is not UNSET:
            field_dict["Description"] = description
        if expected_result is not UNSET:
            field_dict["ExpectedResult"] = expected_result
        if actual_result_template is not UNSET:
            field_dict["ActualResultTemplate"] = actual_result_template
        if step_type is not UNSET:
            field_dict["StepType"] = step_type
        if id is not UNSET:
            field_dict["Id"] = id
        if automation is not UNSET:
            field_dict["Automation"] = automation
        if nested_test_case is not UNSET:
            field_dict["NestedTestCase"] = nested_test_case

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_automation import ApiAutomation
        from ..models.api_nested_test_case_info import ApiNestedTestCaseInfo
        from ..models.api_rich_text import ApiRichText

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        index = d.pop("Index", UNSET)

        _description = d.pop("Description", UNSET)
        description: Union[Unset, None, ApiRichText]
        if _description is None:
            description = None
        elif isinstance(_description, Unset):
            description = UNSET
        else:
            description = ApiRichText.from_dict(_description)

        _expected_result = d.pop("ExpectedResult", UNSET)
        expected_result: Union[Unset, None, ApiRichText]
        if _expected_result is None:
            expected_result = None
        elif isinstance(_expected_result, Unset):
            expected_result = UNSET
        else:
            expected_result = ApiRichText.from_dict(_expected_result)

        _actual_result_template = d.pop("ActualResultTemplate", UNSET)
        actual_result_template: Union[Unset, None, ApiRichText]
        if _actual_result_template is None:
            actual_result_template = None
        elif isinstance(_actual_result_template, Unset):
            actual_result_template = UNSET
        else:
            actual_result_template = ApiRichText.from_dict(_actual_result_template)

        _step_type = d.pop("StepType", UNSET)
        step_type: Union[Unset, ApiTestStepType]
        if isinstance(_step_type, Unset):
            step_type = UNSET
        else:
            step_type = ApiTestStepType(_step_type)

        id = d.pop("Id", UNSET)

        _automation = d.pop("Automation", UNSET)
        automation: Union[Unset, None, ApiAutomation]
        if _automation is None:
            automation = None
        elif isinstance(_automation, Unset):
            automation = UNSET
        else:
            automation = ApiAutomation.from_dict(_automation)

        _nested_test_case = d.pop("NestedTestCase", UNSET)
        nested_test_case: Union[Unset, None, ApiNestedTestCaseInfo]
        if _nested_test_case is None:
            nested_test_case = None
        elif isinstance(_nested_test_case, Unset):
            nested_test_case = UNSET
        else:
            nested_test_case = ApiNestedTestCaseInfo.from_dict(_nested_test_case)

        api_test_step = cls(
            name=name,
            index=index,
            description=description,
            expected_result=expected_result,
            actual_result_template=actual_result_template,
            step_type=step_type,
            id=id,
            automation=automation,
            nested_test_case=nested_test_case,
        )

        api_test_step.additional_properties = d
        return api_test_step

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
