from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_id_name import ApiProjectIdName


T = TypeVar("T", bound="ApiProjectConfigInfo")


@attr.s(auto_attribs=True)
class ApiProjectConfigInfo:
    """Some basic information regarding the project configuration
    (template, etc.).

        Attributes:
            is_owned (Union[Unset, bool]): Indicates whether the current project owns the project configuration.
            is_shared (Union[Unset, bool]): Indicates whether this project configuration is shared between
                multiple projects.
            owning_project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
    """

    is_owned: Union[Unset, bool] = UNSET
    is_shared: Union[Unset, bool] = UNSET
    owning_project: Union[Unset, None, "ApiProjectIdName"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_owned = self.is_owned
        is_shared = self.is_shared
        owning_project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owning_project, Unset):
            owning_project = self.owning_project.to_dict() if self.owning_project else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_owned is not UNSET:
            field_dict["IsOwned"] = is_owned
        if is_shared is not UNSET:
            field_dict["IsShared"] = is_shared
        if owning_project is not UNSET:
            field_dict["OwningProject"] = owning_project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_id_name import ApiProjectIdName

        d = src_dict.copy()
        is_owned = d.pop("IsOwned", UNSET)

        is_shared = d.pop("IsShared", UNSET)

        _owning_project = d.pop("OwningProject", UNSET)
        owning_project: Union[Unset, None, ApiProjectIdName]
        if _owning_project is None:
            owning_project = None
        elif isinstance(_owning_project, Unset):
            owning_project = UNSET
        else:
            owning_project = ApiProjectIdName.from_dict(_owning_project)

        api_project_config_info = cls(
            is_owned=is_owned,
            is_shared=is_shared,
            owning_project=owning_project,
        )

        return api_project_config_info
