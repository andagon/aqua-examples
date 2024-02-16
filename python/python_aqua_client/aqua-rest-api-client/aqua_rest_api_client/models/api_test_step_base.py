from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_test_step_type import ApiTestStepType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_rich_text import ApiRichText


T = TypeVar("T", bound="ApiTestStepBase")


@attr.s(auto_attribs=True)
class ApiTestStepBase:
    """A base class representing test step of a test case.

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
    """

    name: Union[Unset, None, str] = UNSET
    index: Union[Unset, int] = UNSET
    description: Union[Unset, None, "ApiRichText"] = UNSET
    expected_result: Union[Unset, None, "ApiRichText"] = UNSET
    actual_result_template: Union[Unset, None, "ApiRichText"] = UNSET
    step_type: Union[Unset, ApiTestStepType] = UNSET

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

        field_dict: Dict[str, Any] = {}
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        api_test_step_base = cls(
            name=name,
            index=index,
            description=description,
            expected_result=expected_result,
            actual_result_template=actual_result_template,
            step_type=step_type,
        )

        return api_test_step_base
