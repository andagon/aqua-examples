from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_integration_config_update_base import ApiIntegrationConfigUpdateBase


T = TypeVar("T", bound="ApiIntegrationConfigurationsUpdate")


@attr.s(auto_attribs=True)
class ApiIntegrationConfigurationsUpdate:
    """Encapsulates the update of the integrations configuration.

    Attributes:
        configurations (Union[Unset, None, List['ApiIntegrationConfigUpdateBase']]): Holds the configurations for the
            different integrations.
    """

    configurations: Union[Unset, None, List["ApiIntegrationConfigUpdateBase"]] = UNSET

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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if configurations is not UNSET:
            field_dict["Configurations"] = configurations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_integration_config_update_base import ApiIntegrationConfigUpdateBase

        d = src_dict.copy()
        configurations = []
        _configurations = d.pop("Configurations", UNSET)
        for configurations_item_data in _configurations or []:
            configurations_item = ApiIntegrationConfigUpdateBase.from_dict(configurations_item_data)

            configurations.append(configurations_item)

        api_integration_configurations_update = cls(
            configurations=configurations,
        )

        return api_integration_configurations_update
