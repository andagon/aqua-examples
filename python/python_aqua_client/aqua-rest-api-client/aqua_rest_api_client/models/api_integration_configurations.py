from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_integration_config_base import ApiIntegrationConfigBase


T = TypeVar("T", bound="ApiIntegrationConfigurations")


@attr.s(auto_attribs=True)
class ApiIntegrationConfigurations:
    """Contains the integration configurations together with necessary meta data.

    Attributes:
        configurations (Union[Unset, None, List['ApiIntegrationConfigBase']]): Holds the configurations for the
            different integrations.
        can_edit (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
    """

    configurations: Union[Unset, None, List["ApiIntegrationConfigBase"]] = UNSET
    can_edit: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        configurations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.configurations, Unset):
            if self.configurations is None:
                configurations = None
            else:
                configurations = []
                for configurations_item_data in self.configurations:
                    configurations_item = configurations_item_data.to_dict()

                    configurations.append(configurations_item)

        can_edit: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit, Unset):
            can_edit = self.can_edit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if configurations is not UNSET:
            field_dict["Configurations"] = configurations
        if can_edit is not UNSET:
            field_dict["CanEdit"] = can_edit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_integration_config_base import ApiIntegrationConfigBase

        d = src_dict.copy()
        configurations = []
        _configurations = d.pop("Configurations", UNSET)
        for configurations_item_data in _configurations or []:
            configurations_item = ApiIntegrationConfigBase.from_dict(configurations_item_data)

            configurations.append(configurations_item)

        _can_edit = d.pop("CanEdit", UNSET)
        can_edit: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit, Unset):
            can_edit = UNSET
        else:
            can_edit = ApiPermissionResult(_can_edit)

        api_integration_configurations = cls(
            configurations=configurations,
            can_edit=can_edit,
        )

        return api_integration_configurations
