from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_test_execution_data_attribute_type import ApiTestExecutionDataAttributeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value_date_time import ApiFieldValueDateTime


T = TypeVar("T", bound="ApiTestExecutionDataAttribute")


@attr.s(auto_attribs=True)
class ApiTestExecutionDataAttribute:
    """Represents a single "exection data attribute".

    Attributes:
        id (Union[Unset, int]): Id of the attribute
        attr_name (Union[Unset, None, str]): Name of the attribute
        attr_value (Union[Unset, None, str]): Value of the attribute (as string)
        attr_type (Union[Unset, ApiTestExecutionDataAttributeType]): Identifies the type of execution data attribute
            This enum has the following values:
              - `Float`
              - `Integer`
              - `String`
        process_element_execution_id (Union[Unset, int]): Id of the related ProcessElementExecution
        test_step_execution_id (Union[Unset, int]): Id of the related TestStepExecution
        test_job_execution_id (Union[Unset, int]): Id of the related TestJobExecution
        date_modified (Union[Unset, None, ApiFieldValueDateTime]):
        step_name (Union[Unset, None, str]): Name of the related automated step.
        step_index (Union[Unset, int]): Zero based index of related automated step execution.
    """

    id: Union[Unset, int] = UNSET
    attr_name: Union[Unset, None, str] = UNSET
    attr_value: Union[Unset, None, str] = UNSET
    attr_type: Union[Unset, ApiTestExecutionDataAttributeType] = UNSET
    process_element_execution_id: Union[Unset, int] = UNSET
    test_step_execution_id: Union[Unset, int] = UNSET
    test_job_execution_id: Union[Unset, int] = UNSET
    date_modified: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    step_name: Union[Unset, None, str] = UNSET
    step_index: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        attr_name = self.attr_name
        attr_value = self.attr_value
        attr_type: Union[Unset, str] = UNSET
        if not isinstance(self.attr_type, Unset):
            attr_type = self.attr_type.value

        process_element_execution_id = self.process_element_execution_id
        test_step_execution_id = self.test_step_execution_id
        test_job_execution_id = self.test_job_execution_id
        date_modified: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.to_dict() if self.date_modified else None

        step_name = self.step_name
        step_index = self.step_index

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if attr_name is not UNSET:
            field_dict["AttrName"] = attr_name
        if attr_value is not UNSET:
            field_dict["AttrValue"] = attr_value
        if attr_type is not UNSET:
            field_dict["AttrType"] = attr_type
        if process_element_execution_id is not UNSET:
            field_dict["ProcessElementExecutionId"] = process_element_execution_id
        if test_step_execution_id is not UNSET:
            field_dict["TestStepExecutionId"] = test_step_execution_id
        if test_job_execution_id is not UNSET:
            field_dict["TestJobExecutionId"] = test_job_execution_id
        if date_modified is not UNSET:
            field_dict["DateModified"] = date_modified
        if step_name is not UNSET:
            field_dict["StepName"] = step_name
        if step_index is not UNSET:
            field_dict["StepIndex"] = step_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_date_time import ApiFieldValueDateTime

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        attr_name = d.pop("AttrName", UNSET)

        attr_value = d.pop("AttrValue", UNSET)

        _attr_type = d.pop("AttrType", UNSET)
        attr_type: Union[Unset, ApiTestExecutionDataAttributeType]
        if isinstance(_attr_type, Unset):
            attr_type = UNSET
        else:
            attr_type = ApiTestExecutionDataAttributeType(_attr_type)

        process_element_execution_id = d.pop("ProcessElementExecutionId", UNSET)

        test_step_execution_id = d.pop("TestStepExecutionId", UNSET)

        test_job_execution_id = d.pop("TestJobExecutionId", UNSET)

        _date_modified = d.pop("DateModified", UNSET)
        date_modified: Union[Unset, None, ApiFieldValueDateTime]
        if _date_modified is None:
            date_modified = None
        elif isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = ApiFieldValueDateTime.from_dict(_date_modified)

        step_name = d.pop("StepName", UNSET)

        step_index = d.pop("StepIndex", UNSET)

        api_test_execution_data_attribute = cls(
            id=id,
            attr_name=attr_name,
            attr_value=attr_value,
            attr_type=attr_type,
            process_element_execution_id=process_element_execution_id,
            test_step_execution_id=test_step_execution_id,
            test_job_execution_id=test_job_execution_id,
            date_modified=date_modified,
            step_name=step_name,
            step_index=step_index,
        )

        return api_test_execution_data_attribute
