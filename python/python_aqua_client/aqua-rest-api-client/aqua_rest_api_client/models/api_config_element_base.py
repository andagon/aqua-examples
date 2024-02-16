from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiConfigElementBase")


@attr.s(auto_attribs=True)
class ApiConfigElementBase:
    """Base class for models representing config elements.

    Attributes:
        data_path (Union[Unset, None, str]): Path of the config element. Lowercase letters divided by dots are expected
            here
            e.g. "this.is.sample.path".
        locked (Union[Unset, bool]): True if the config element is locked.
            The flag is considered only for non-user entries (project or global).
        project_id (Union[Unset, None, int]): Id of the project this config element belongs to.
            Can be null - then represents global configuration (system-wide).
        user_id (Union[Unset, None, int]): Id of the owner user. Can be null, then represents a default
            configuration (either project or global level).
    """

    data_path: Union[Unset, None, str] = UNSET
    locked: Union[Unset, bool] = UNSET
    project_id: Union[Unset, None, int] = UNSET
    user_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        data_path = self.data_path
        locked = self.locked
        project_id = self.project_id
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if data_path is not UNSET:
            field_dict["DataPath"] = data_path
        if locked is not UNSET:
            field_dict["Locked"] = locked
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_path = d.pop("DataPath", UNSET)

        locked = d.pop("Locked", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        user_id = d.pop("UserId", UNSET)

        api_config_element_base = cls(
            data_path=data_path,
            locked=locked,
            project_id=project_id,
            user_id=user_id,
        )

        return api_config_element_base
