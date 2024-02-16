from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_id_name import ApiProjectIdName


T = TypeVar("T", bound="ApiProjectOptionsWithOwnership")


@attr.s(auto_attribs=True)
class ApiProjectOptionsWithOwnership:
    """
    Attributes:
        require_expected_results (Union[Unset, bool]): If set, then 'Expected Results' field is mandatory when defining
            a test case.
        require_actual_results (Union[Unset, bool]): If set, then 'Actual Results' field is mandatory when manually
            executing a test case.
        project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
        is_shared (Union[Unset, bool]): Indicates whether the project configuration is shared with
            a different project.
        is_owned (Union[Unset, bool]): Indicates whether the project configuration is owned by the
            project for which this part of the configuration was requested.
        owning_project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
        can_edit (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
    """

    require_expected_results: Union[Unset, bool] = UNSET
    require_actual_results: Union[Unset, bool] = UNSET
    project: Union[Unset, None, "ApiProjectIdName"] = UNSET
    is_shared: Union[Unset, bool] = UNSET
    is_owned: Union[Unset, bool] = UNSET
    owning_project: Union[Unset, None, "ApiProjectIdName"] = UNSET
    can_edit: Union[Unset, ApiPermissionResult] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        require_expected_results = self.require_expected_results
        require_actual_results = self.require_actual_results
        project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict() if self.project else None

        is_shared = self.is_shared
        is_owned = self.is_owned
        owning_project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owning_project, Unset):
            owning_project = self.owning_project.to_dict() if self.owning_project else None

        can_edit: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit, Unset):
            can_edit = self.can_edit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if require_expected_results is not UNSET:
            field_dict["RequireExpectedResults"] = require_expected_results
        if require_actual_results is not UNSET:
            field_dict["RequireActualResults"] = require_actual_results
        if project is not UNSET:
            field_dict["Project"] = project
        if is_shared is not UNSET:
            field_dict["IsShared"] = is_shared
        if is_owned is not UNSET:
            field_dict["IsOwned"] = is_owned
        if owning_project is not UNSET:
            field_dict["OwningProject"] = owning_project
        if can_edit is not UNSET:
            field_dict["CanEdit"] = can_edit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_id_name import ApiProjectIdName

        d = src_dict.copy()
        require_expected_results = d.pop("RequireExpectedResults", UNSET)

        require_actual_results = d.pop("RequireActualResults", UNSET)

        _project = d.pop("Project", UNSET)
        project: Union[Unset, None, ApiProjectIdName]
        if _project is None:
            project = None
        elif isinstance(_project, Unset):
            project = UNSET
        else:
            project = ApiProjectIdName.from_dict(_project)

        is_shared = d.pop("IsShared", UNSET)

        is_owned = d.pop("IsOwned", UNSET)

        _owning_project = d.pop("OwningProject", UNSET)
        owning_project: Union[Unset, None, ApiProjectIdName]
        if _owning_project is None:
            owning_project = None
        elif isinstance(_owning_project, Unset):
            owning_project = UNSET
        else:
            owning_project = ApiProjectIdName.from_dict(_owning_project)

        _can_edit = d.pop("CanEdit", UNSET)
        can_edit: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit, Unset):
            can_edit = UNSET
        else:
            can_edit = ApiPermissionResult(_can_edit)

        api_project_options_with_ownership = cls(
            require_expected_results=require_expected_results,
            require_actual_results=require_actual_results,
            project=project,
            is_shared=is_shared,
            is_owned=is_owned,
            owning_project=owning_project,
            can_edit=can_edit,
        )

        api_project_options_with_ownership.additional_properties = d
        return api_project_options_with_ownership

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
