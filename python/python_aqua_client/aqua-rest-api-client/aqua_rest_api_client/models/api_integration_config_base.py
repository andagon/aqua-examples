from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiIntegrationConfigBase")


@attr.s(auto_attribs=True)
class ApiIntegrationConfigBase:
    """Base class for integration configuration classes

    Attributes:
        integration_type (str):
        supports_lookup (Union[Unset, bool]): Indicates whether this configuration supports remote lookup.
            Requires support from "technology" (currently JIRA only) but also needs the proper configuration.
            Note: the flag is properly set even if config has been "obfuscated" from sensitive data.
            This flag is ignored during save (doesn't have to be provided at all).
        is_enabled (Union[Unset, bool]):
        customer_id (Union[Unset, int]):
        project_id (Union[Unset, None, int]):
    """

    integration_type: str
    supports_lookup: Union[Unset, bool] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    customer_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        integration_type = self.integration_type
        supports_lookup = self.supports_lookup
        is_enabled = self.is_enabled
        customer_id = self.customer_id
        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "IntegrationType": integration_type,
            }
        )
        if supports_lookup is not UNSET:
            field_dict["SupportsLookup"] = supports_lookup
        if is_enabled is not UNSET:
            field_dict["IsEnabled"] = is_enabled
        if customer_id is not UNSET:
            field_dict["CustomerId"] = customer_id
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        integration_type = d.pop("IntegrationType")

        supports_lookup = d.pop("SupportsLookup", UNSET)

        is_enabled = d.pop("IsEnabled", UNSET)

        customer_id = d.pop("CustomerId", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        api_integration_config_base = cls(
            integration_type=integration_type,
            supports_lookup=supports_lookup,
            is_enabled=is_enabled,
            customer_id=customer_id,
            project_id=project_id,
        )

        return api_integration_config_base
