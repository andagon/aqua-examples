from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_execution_create_meta import ApiTestExecutionCreateMeta
    from ..models.api_test_execution_new import ApiTestExecutionNew


T = TypeVar("T", bound="ApiTestScenarioExecutionPreviewResponse")


@attr.s(auto_attribs=True)
class ApiTestScenarioExecutionPreviewResponse:
    """Represents the test scenario execution preview response, containing a testexecution preview and further information.

    Attributes:
        new_test_executions (List['ApiTestExecutionNew']): Testexecution preview list.
        create_meta (ApiTestExecutionCreateMeta): Contains the metadata which is necessary for creating a new execution.
        require_actual_result (Union[Unset, bool]): If true, then 'Actual Results' field is mandatory when manually
            executing.
        can_finalize_test_execution (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
    """

    new_test_executions: List["ApiTestExecutionNew"]
    create_meta: "ApiTestExecutionCreateMeta"
    require_actual_result: Union[Unset, bool] = UNSET
    can_finalize_test_execution: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        new_test_executions = []
        for new_test_executions_item_data in self.new_test_executions:
            new_test_executions_item = new_test_executions_item_data.to_dict()

            new_test_executions.append(new_test_executions_item)

        create_meta = self.create_meta.to_dict()

        require_actual_result = self.require_actual_result
        can_finalize_test_execution: Union[Unset, str] = UNSET
        if not isinstance(self.can_finalize_test_execution, Unset):
            can_finalize_test_execution = self.can_finalize_test_execution.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "NewTestExecutions": new_test_executions,
                "CreateMeta": create_meta,
            }
        )
        if require_actual_result is not UNSET:
            field_dict["RequireActualResult"] = require_actual_result
        if can_finalize_test_execution is not UNSET:
            field_dict["CanFinalizeTestExecution"] = can_finalize_test_execution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_execution_create_meta import ApiTestExecutionCreateMeta
        from ..models.api_test_execution_new import ApiTestExecutionNew

        d = src_dict.copy()
        new_test_executions = []
        _new_test_executions = d.pop("NewTestExecutions")
        for new_test_executions_item_data in _new_test_executions:
            new_test_executions_item = ApiTestExecutionNew.from_dict(new_test_executions_item_data)

            new_test_executions.append(new_test_executions_item)

        create_meta = ApiTestExecutionCreateMeta.from_dict(d.pop("CreateMeta"))

        require_actual_result = d.pop("RequireActualResult", UNSET)

        _can_finalize_test_execution = d.pop("CanFinalizeTestExecution", UNSET)
        can_finalize_test_execution: Union[Unset, ApiPermissionResult]
        if isinstance(_can_finalize_test_execution, Unset):
            can_finalize_test_execution = UNSET
        else:
            can_finalize_test_execution = ApiPermissionResult(_can_finalize_test_execution)

        api_test_scenario_execution_preview_response = cls(
            new_test_executions=new_test_executions,
            create_meta=create_meta,
            require_actual_result=require_actual_result,
            can_finalize_test_execution=can_finalize_test_execution,
        )

        return api_test_scenario_execution_preview_response
