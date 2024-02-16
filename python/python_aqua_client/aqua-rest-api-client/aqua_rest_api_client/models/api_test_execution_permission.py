from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestExecutionPermission")


@attr.s(auto_attribs=True)
class ApiTestExecutionPermission:
    """Represents permissions of an test execution. Intended to be subclassed
    by classes with more fine-grained permission set for given context.

        Attributes:
            can_create (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_create_dependency (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
            can_create_execution_log (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
                This enum has the following values:
                  - `Denied` The given permission is deined, although is included in the license.
                  - `Granted` The given permission is granted.
                  - `NotLicensed` The given permission is not even licensed (so denied).
    """

    can_create: Union[Unset, ApiPermissionResult] = UNSET
    can_create_dependency: Union[Unset, ApiPermissionResult] = UNSET
    can_create_execution_log: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_create: Union[Unset, str] = UNSET
        if not isinstance(self.can_create, Unset):
            can_create = self.can_create.value

        can_create_dependency: Union[Unset, str] = UNSET
        if not isinstance(self.can_create_dependency, Unset):
            can_create_dependency = self.can_create_dependency.value

        can_create_execution_log: Union[Unset, str] = UNSET
        if not isinstance(self.can_create_execution_log, Unset):
            can_create_execution_log = self.can_create_execution_log.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_create is not UNSET:
            field_dict["CanCreate"] = can_create
        if can_create_dependency is not UNSET:
            field_dict["CanCreateDependency"] = can_create_dependency
        if can_create_execution_log is not UNSET:
            field_dict["CanCreateExecutionLog"] = can_create_execution_log

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _can_create = d.pop("CanCreate", UNSET)
        can_create: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create, Unset):
            can_create = UNSET
        else:
            can_create = ApiPermissionResult(_can_create)

        _can_create_dependency = d.pop("CanCreateDependency", UNSET)
        can_create_dependency: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create_dependency, Unset):
            can_create_dependency = UNSET
        else:
            can_create_dependency = ApiPermissionResult(_can_create_dependency)

        _can_create_execution_log = d.pop("CanCreateExecutionLog", UNSET)
        can_create_execution_log: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create_execution_log, Unset):
            can_create_execution_log = UNSET
        else:
            can_create_execution_log = ApiPermissionResult(_can_create_execution_log)

        api_test_execution_permission = cls(
            can_create=can_create,
            can_create_dependency=can_create_dependency,
            can_create_execution_log=can_create_execution_log,
        )

        return api_test_execution_permission
