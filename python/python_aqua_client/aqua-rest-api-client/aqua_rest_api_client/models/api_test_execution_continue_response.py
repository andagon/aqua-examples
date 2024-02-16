from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_location import ApiItemLocation
    from ..models.api_test_execution_extended_info import ApiTestExecutionExtendedInfo


T = TypeVar("T", bound="ApiTestExecutionContinueResponse")


@attr.s(auto_attribs=True)
class ApiTestExecutionContinueResponse:
    """Represents the test execution continue response.

    Attributes:
        test_executions (List['ApiTestExecutionExtendedInfo']): Testexecution list.
        require_actual_result (Union[Unset, bool]): If true, then 'Actual Results' field is mandatory when manually
            executing.
        can_finalize_test_execution (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        location (Union[Unset, None, ApiItemLocation]): Specifies the location (project and folder) of an item
    """

    test_executions: List["ApiTestExecutionExtendedInfo"]
    require_actual_result: Union[Unset, bool] = UNSET
    can_finalize_test_execution: Union[Unset, ApiPermissionResult] = UNSET
    location: Union[Unset, None, "ApiItemLocation"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        test_executions = []
        for test_executions_item_data in self.test_executions:
            test_executions_item = test_executions_item_data.to_dict()

            test_executions.append(test_executions_item)

        require_actual_result = self.require_actual_result
        can_finalize_test_execution: Union[Unset, str] = UNSET
        if not isinstance(self.can_finalize_test_execution, Unset):
            can_finalize_test_execution = self.can_finalize_test_execution.value

        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "TestExecutions": test_executions,
            }
        )
        if require_actual_result is not UNSET:
            field_dict["RequireActualResult"] = require_actual_result
        if can_finalize_test_execution is not UNSET:
            field_dict["CanFinalizeTestExecution"] = can_finalize_test_execution
        if location is not UNSET:
            field_dict["Location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_location import ApiItemLocation
        from ..models.api_test_execution_extended_info import ApiTestExecutionExtendedInfo

        d = src_dict.copy()
        test_executions = []
        _test_executions = d.pop("TestExecutions")
        for test_executions_item_data in _test_executions:
            test_executions_item = ApiTestExecutionExtendedInfo.from_dict(test_executions_item_data)

            test_executions.append(test_executions_item)

        require_actual_result = d.pop("RequireActualResult", UNSET)

        _can_finalize_test_execution = d.pop("CanFinalizeTestExecution", UNSET)
        can_finalize_test_execution: Union[Unset, ApiPermissionResult]
        if isinstance(_can_finalize_test_execution, Unset):
            can_finalize_test_execution = UNSET
        else:
            can_finalize_test_execution = ApiPermissionResult(_can_finalize_test_execution)

        _location = d.pop("Location", UNSET)
        location: Union[Unset, None, ApiItemLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = ApiItemLocation.from_dict(_location)

        api_test_execution_continue_response = cls(
            test_executions=test_executions,
            require_actual_result=require_actual_result,
            can_finalize_test_execution=can_finalize_test_execution,
            location=location,
        )

        return api_test_execution_continue_response
