from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_automatic_execution_support import ApiAutomaticExecutionSupport
from ..models.api_automation_technology import ApiAutomationTechnology
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_data_value_set_info import ApiTestDataValueSetInfo


T = TypeVar("T", bound="ApiTestJobPreview")


@attr.s(auto_attribs=True)
class ApiTestJobPreview:
    """Contains the test job preview information.

    Attributes:
        project_id (int): The id of the project.
        folder_id (int): The id of the folder.
        test_case_id (int): The id of the test case.
        test_case_name (str): The name of the test case.
        supports_automatic_execution (Union[Unset, ApiAutomaticExecutionSupport]):
            This enum has the following values:
              - `Complete` Automatic execution complete supported.
              - `None` Automatic execution not supported.
              - `Partially` Automatic execution partially supported.
        has_variables (Union[Unset, bool]): If set, then test case contains test data.
        required_agent_technologies (Union[Unset, None, List[ApiAutomationTechnology]]): Contains the information about
            required agent technologies for the test job execution.
        default_value_set (Union[Unset, None, ApiTestDataValueSetInfo]): Contains the meta data of a certain value set
            in the test data.
    """

    project_id: int
    folder_id: int
    test_case_id: int
    test_case_name: str
    supports_automatic_execution: Union[Unset, ApiAutomaticExecutionSupport] = UNSET
    has_variables: Union[Unset, bool] = UNSET
    required_agent_technologies: Union[Unset, None, List[ApiAutomationTechnology]] = UNSET
    default_value_set: Union[Unset, None, "ApiTestDataValueSetInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        folder_id = self.folder_id
        test_case_id = self.test_case_id
        test_case_name = self.test_case_name
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

        default_value_set: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.default_value_set, Unset):
            default_value_set = self.default_value_set.to_dict() if self.default_value_set else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ProjectId": project_id,
                "FolderId": folder_id,
                "TestCaseId": test_case_id,
                "TestCaseName": test_case_name,
            }
        )
        if supports_automatic_execution is not UNSET:
            field_dict["SupportsAutomaticExecution"] = supports_automatic_execution
        if has_variables is not UNSET:
            field_dict["HasVariables"] = has_variables
        if required_agent_technologies is not UNSET:
            field_dict["RequiredAgentTechnologies"] = required_agent_technologies
        if default_value_set is not UNSET:
            field_dict["DefaultValueSet"] = default_value_set

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_data_value_set_info import ApiTestDataValueSetInfo

        d = src_dict.copy()
        project_id = d.pop("ProjectId")

        folder_id = d.pop("FolderId")

        test_case_id = d.pop("TestCaseId")

        test_case_name = d.pop("TestCaseName")

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

        _default_value_set = d.pop("DefaultValueSet", UNSET)
        default_value_set: Union[Unset, None, ApiTestDataValueSetInfo]
        if _default_value_set is None:
            default_value_set = None
        elif isinstance(_default_value_set, Unset):
            default_value_set = UNSET
        else:
            default_value_set = ApiTestDataValueSetInfo.from_dict(_default_value_set)

        api_test_job_preview = cls(
            project_id=project_id,
            folder_id=folder_id,
            test_case_id=test_case_id,
            test_case_name=test_case_name,
            supports_automatic_execution=supports_automatic_execution,
            has_variables=has_variables,
            required_agent_technologies=required_agent_technologies,
            default_value_set=default_value_set,
        )

        return api_test_job_preview
