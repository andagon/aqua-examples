from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_automatic_execution_support import ApiAutomaticExecutionSupport
from ..models.api_automation_technology import ApiAutomationTechnology
from ..models.api_base_item_accessibility import ApiBaseItemAccessibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value_date_time import ApiFieldValueDateTime


T = TypeVar("T", bound="ApiTestCaseJobInfo")


@attr.s(auto_attribs=True)
class ApiTestCaseJobInfo:
    """
    Attributes:
        id (int): The id of the test case
        name (str): The name of the test case
        test_case_accessibility (Union[Unset, ApiBaseItemAccessibility]): Identifies the test case accessibility.
            This enum has the following values:
              - `Accessible` The test case is accessible.
              - `Archived` The test case is archived
              - `Deleted` The test case is deleted.
              - `NoPermissions` No permissions to access the test case.
        last_modified (Union[Unset, None, ApiFieldValueDateTime]):
        supports_automatic_execution (Union[Unset, ApiAutomaticExecutionSupport]):
            This enum has the following values:
              - `Complete` Automatic execution complete supported.
              - `None` Automatic execution not supported.
              - `Partially` Automatic execution partially supported.
        has_variables (Union[Unset, bool]): If set, then the test case contains test data.
        required_agent_technologies (Union[Unset, None, List[ApiAutomationTechnology]]): Contains the information about
            required agent technologies for the test job execution.
    """

    id: int
    name: str
    test_case_accessibility: Union[Unset, ApiBaseItemAccessibility] = UNSET
    last_modified: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    supports_automatic_execution: Union[Unset, ApiAutomaticExecutionSupport] = UNSET
    has_variables: Union[Unset, bool] = UNSET
    required_agent_technologies: Union[Unset, None, List[ApiAutomationTechnology]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        test_case_accessibility: Union[Unset, str] = UNSET
        if not isinstance(self.test_case_accessibility, Unset):
            test_case_accessibility = self.test_case_accessibility.value

        last_modified: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.to_dict() if self.last_modified else None

        supports_automatic_execution: Union[Unset, str] = UNSET
        if not isinstance(self.supports_automatic_execution, Unset):
            supports_automatic_execution = self.supports_automatic_execution.value

        has_variables = self.has_variables
        required_agent_technologies: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.required_agent_technologies, Unset):
            if self.required_agent_technologies is None:
                required_agent_technologies = None
            else:
                required_agent_technologies = []
                for required_agent_technologies_item_data in self.required_agent_technologies:
                    required_agent_technologies_item = required_agent_technologies_item_data.value

                    required_agent_technologies.append(required_agent_technologies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Id": id,
                "Name": name,
            }
        )
        if test_case_accessibility is not UNSET:
            field_dict["TestCaseAccessibility"] = test_case_accessibility
        if last_modified is not UNSET:
            field_dict["LastModified"] = last_modified
        if supports_automatic_execution is not UNSET:
            field_dict["SupportsAutomaticExecution"] = supports_automatic_execution
        if has_variables is not UNSET:
            field_dict["HasVariables"] = has_variables
        if required_agent_technologies is not UNSET:
            field_dict["RequiredAgentTechnologies"] = required_agent_technologies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_date_time import ApiFieldValueDateTime

        d = src_dict.copy()
        id = d.pop("Id")

        name = d.pop("Name")

        _test_case_accessibility = d.pop("TestCaseAccessibility", UNSET)
        test_case_accessibility: Union[Unset, ApiBaseItemAccessibility]
        if isinstance(_test_case_accessibility, Unset):
            test_case_accessibility = UNSET
        else:
            test_case_accessibility = ApiBaseItemAccessibility(_test_case_accessibility)

        _last_modified = d.pop("LastModified", UNSET)
        last_modified: Union[Unset, None, ApiFieldValueDateTime]
        if _last_modified is None:
            last_modified = None
        elif isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = ApiFieldValueDateTime.from_dict(_last_modified)

        _supports_automatic_execution = d.pop("SupportsAutomaticExecution", UNSET)
        supports_automatic_execution: Union[Unset, ApiAutomaticExecutionSupport]
        if isinstance(_supports_automatic_execution, Unset):
            supports_automatic_execution = UNSET
        else:
            supports_automatic_execution = ApiAutomaticExecutionSupport(_supports_automatic_execution)

        has_variables = d.pop("HasVariables", UNSET)

        required_agent_technologies = []
        _required_agent_technologies = d.pop("RequiredAgentTechnologies", UNSET)
        for required_agent_technologies_item_data in _required_agent_technologies or []:
            required_agent_technologies_item = ApiAutomationTechnology(required_agent_technologies_item_data)

            required_agent_technologies.append(required_agent_technologies_item)

        api_test_case_job_info = cls(
            id=id,
            name=name,
            test_case_accessibility=test_case_accessibility,
            last_modified=last_modified,
            supports_automatic_execution=supports_automatic_execution,
            has_variables=has_variables,
            required_agent_technologies=required_agent_technologies,
        )

        return api_test_case_job_info
