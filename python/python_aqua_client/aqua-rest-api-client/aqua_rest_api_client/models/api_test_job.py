from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_agent_id_and_name import ApiAgentIdAndName
    from ..models.api_field_value_user import ApiFieldValueUser
    from ..models.api_field_with_value import ApiFieldWithValue
    from ..models.api_label_reference import ApiLabelReference
    from ..models.api_last_execution_info import ApiLastExecutionInfo
    from ..models.api_run_dependency_entry import ApiRunDependencyEntry
    from ..models.api_test_case_execution_history import ApiTestCaseExecutionHistory
    from ..models.api_test_case_job_info import ApiTestCaseJobInfo
    from ..models.api_test_data_referenced_value_set_info import ApiTestDataReferencedValueSetInfo


T = TypeVar("T", bound="ApiTestJob")


@attr.s(auto_attribs=True)
class ApiTestJob:
    """Contains the test job information.

    Attributes:
        id (int): Id of the test job.
        index (int): Index of the test job in test scenario.
        tested_version (Union[Unset, None, str]): Tested version id.
        run_dependency (Union[Unset, None, List['ApiRunDependencyEntry']]): Run dependencies as list with more
            information.
        test_case_info (Union[Unset, None, ApiTestCaseJobInfo]):
        agent_to_use (Union[Unset, None, ApiAgentIdAndName]): Some minimal identifying information for an agent.
        selected_value_set (Union[Unset, None, ApiTestDataReferencedValueSetInfo]): Contains the meta data of certain
            value set which is referenced
            somewhere (e.g. test step or test job).
        labels (Union[Unset, None, List['ApiLabelReference']]): Contains labels attached to this execution
        last_execution_info (Union[Unset, None, ApiLastExecutionInfo]): Contains information about the last execution.
        execution_history (Union[Unset, None, ApiTestCaseExecutionHistory]): Historic information regarding the last
            executions
            of a test case or test job.
        tester (Union[Unset, None, ApiFieldValueUser]):
        custom_fields (Union[Unset, None, List['ApiFieldWithValue']]): Contains the execution custom fields for this
            test job
    """

    id: int
    index: int
    tested_version: Union[Unset, None, str] = UNSET
    run_dependency: Union[Unset, None, List["ApiRunDependencyEntry"]] = UNSET
    test_case_info: Union[Unset, None, "ApiTestCaseJobInfo"] = UNSET
    agent_to_use: Union[Unset, None, "ApiAgentIdAndName"] = UNSET
    selected_value_set: Union[Unset, None, "ApiTestDataReferencedValueSetInfo"] = UNSET
    labels: Union[Unset, None, List["ApiLabelReference"]] = UNSET
    last_execution_info: Union[Unset, None, "ApiLastExecutionInfo"] = UNSET
    execution_history: Union[Unset, None, "ApiTestCaseExecutionHistory"] = UNSET
    tester: Union[Unset, None, "ApiFieldValueUser"] = UNSET
    custom_fields: Union[Unset, None, List["ApiFieldWithValue"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        index = self.index
        tested_version = self.tested_version
        run_dependency: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.run_dependency, Unset):
            if self.run_dependency is None:
                run_dependency = None
            else:
                run_dependency = []
                for run_dependency_item_data in self.run_dependency:
                    run_dependency_item = run_dependency_item_data.to_dict()

                    run_dependency.append(run_dependency_item)

        test_case_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.test_case_info, Unset):
            test_case_info = self.test_case_info.to_dict() if self.test_case_info else None

        agent_to_use: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.agent_to_use, Unset):
            agent_to_use = self.agent_to_use.to_dict() if self.agent_to_use else None

        selected_value_set: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.selected_value_set, Unset):
            selected_value_set = self.selected_value_set.to_dict() if self.selected_value_set else None

        labels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            if self.labels is None:
                labels = None
            else:
                labels = []
                for labels_item_data in self.labels:
                    labels_item = labels_item_data.to_dict()

                    labels.append(labels_item)

        last_execution_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_execution_info, Unset):
            last_execution_info = self.last_execution_info.to_dict() if self.last_execution_info else None

        execution_history: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_history, Unset):
            execution_history = self.execution_history.to_dict() if self.execution_history else None

        tester: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.tester, Unset):
            tester = self.tester.to_dict() if self.tester else None

        custom_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            if self.custom_fields is None:
                custom_fields = None
            else:
                custom_fields = []
                for custom_fields_item_data in self.custom_fields:
                    custom_fields_item = custom_fields_item_data.to_dict()

                    custom_fields.append(custom_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Id": id,
                "Index": index,
            }
        )
        if tested_version is not UNSET:
            field_dict["TestedVersion"] = tested_version
        if run_dependency is not UNSET:
            field_dict["RunDependency"] = run_dependency
        if test_case_info is not UNSET:
            field_dict["TestCaseInfo"] = test_case_info
        if agent_to_use is not UNSET:
            field_dict["AgentToUse"] = agent_to_use
        if selected_value_set is not UNSET:
            field_dict["SelectedValueSet"] = selected_value_set
        if labels is not UNSET:
            field_dict["Labels"] = labels
        if last_execution_info is not UNSET:
            field_dict["LastExecutionInfo"] = last_execution_info
        if execution_history is not UNSET:
            field_dict["ExecutionHistory"] = execution_history
        if tester is not UNSET:
            field_dict["Tester"] = tester
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_agent_id_and_name import ApiAgentIdAndName
        from ..models.api_field_value_user import ApiFieldValueUser
        from ..models.api_field_with_value import ApiFieldWithValue
        from ..models.api_label_reference import ApiLabelReference
        from ..models.api_last_execution_info import ApiLastExecutionInfo
        from ..models.api_run_dependency_entry import ApiRunDependencyEntry
        from ..models.api_test_case_execution_history import ApiTestCaseExecutionHistory
        from ..models.api_test_case_job_info import ApiTestCaseJobInfo
        from ..models.api_test_data_referenced_value_set_info import ApiTestDataReferencedValueSetInfo

        d = src_dict.copy()
        id = d.pop("Id")

        index = d.pop("Index")

        tested_version = d.pop("TestedVersion", UNSET)

        run_dependency = []
        _run_dependency = d.pop("RunDependency", UNSET)
        for run_dependency_item_data in _run_dependency or []:
            run_dependency_item = ApiRunDependencyEntry.from_dict(run_dependency_item_data)

            run_dependency.append(run_dependency_item)

        _test_case_info = d.pop("TestCaseInfo", UNSET)
        test_case_info: Union[Unset, None, ApiTestCaseJobInfo]
        if _test_case_info is None:
            test_case_info = None
        elif isinstance(_test_case_info, Unset):
            test_case_info = UNSET
        else:
            test_case_info = ApiTestCaseJobInfo.from_dict(_test_case_info)

        _agent_to_use = d.pop("AgentToUse", UNSET)
        agent_to_use: Union[Unset, None, ApiAgentIdAndName]
        if _agent_to_use is None:
            agent_to_use = None
        elif isinstance(_agent_to_use, Unset):
            agent_to_use = UNSET
        else:
            agent_to_use = ApiAgentIdAndName.from_dict(_agent_to_use)

        _selected_value_set = d.pop("SelectedValueSet", UNSET)
        selected_value_set: Union[Unset, None, ApiTestDataReferencedValueSetInfo]
        if _selected_value_set is None:
            selected_value_set = None
        elif isinstance(_selected_value_set, Unset):
            selected_value_set = UNSET
        else:
            selected_value_set = ApiTestDataReferencedValueSetInfo.from_dict(_selected_value_set)

        labels = []
        _labels = d.pop("Labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = ApiLabelReference.from_dict(labels_item_data)

            labels.append(labels_item)

        _last_execution_info = d.pop("LastExecutionInfo", UNSET)
        last_execution_info: Union[Unset, None, ApiLastExecutionInfo]
        if _last_execution_info is None:
            last_execution_info = None
        elif isinstance(_last_execution_info, Unset):
            last_execution_info = UNSET
        else:
            last_execution_info = ApiLastExecutionInfo.from_dict(_last_execution_info)

        _execution_history = d.pop("ExecutionHistory", UNSET)
        execution_history: Union[Unset, None, ApiTestCaseExecutionHistory]
        if _execution_history is None:
            execution_history = None
        elif isinstance(_execution_history, Unset):
            execution_history = UNSET
        else:
            execution_history = ApiTestCaseExecutionHistory.from_dict(_execution_history)

        _tester = d.pop("Tester", UNSET)
        tester: Union[Unset, None, ApiFieldValueUser]
        if _tester is None:
            tester = None
        elif isinstance(_tester, Unset):
            tester = UNSET
        else:
            tester = ApiFieldValueUser.from_dict(_tester)

        custom_fields = []
        _custom_fields = d.pop("CustomFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = ApiFieldWithValue.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        api_test_job = cls(
            id=id,
            index=index,
            tested_version=tested_version,
            run_dependency=run_dependency,
            test_case_info=test_case_info,
            agent_to_use=agent_to_use,
            selected_value_set=selected_value_set,
            labels=labels,
            last_execution_info=last_execution_info,
            execution_history=execution_history,
            tester=tester,
            custom_fields=custom_fields,
        )

        return api_test_job
