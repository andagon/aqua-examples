from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiIntegrationConfigOtrs")


@attr.s(auto_attribs=True)
class ApiIntegrationConfigOtrs:
    """
    Attributes:
        integration_type (str):
        supports_lookup (Union[Unset, bool]): Indicates whether this configuration supports remote lookup.
            Requires support from "technology" (currently JIRA only) but also needs the proper configuration.
            Note: the flag is properly set even if config has been "obfuscated" from sensitive data.
            This flag is ignored during save (doesn't have to be provided at all).
        is_enabled (Union[Unset, bool]):
        customer_id (Union[Unset, int]):
        project_id (Union[Unset, None, int]):
        item_view_url_pattern (Union[Unset, None, str]):
    """

    integration_type: str
    supports_lookup: Union[Unset, bool] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    customer_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, None, int] = UNSET
    item_view_url_pattern: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        integration_type = self.integration_type
        supports_lookup = self.supports_lookup
        is_enabled = self.is_enabled
        customer_id = self.customer_id
        project_id = self.project_id
        item_view_url_pattern = self.item_view_url_pattern

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if item_view_url_pattern is not UNSET:
            field_dict["ItemViewURLPattern"] = item_view_url_pattern

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        integration_type = d.pop("IntegrationType")

        supports_lookup = d.pop("SupportsLookup", UNSET)

        is_enabled = d.pop("IsEnabled", UNSET)

        customer_id = d.pop("CustomerId", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        item_view_url_pattern = d.pop("ItemViewURLPattern", UNSET)

        api_integration_config_otrs = cls(
            integration_type=integration_type,
            supports_lookup=supports_lookup,
            is_enabled=is_enabled,
            customer_id=customer_id,
            project_id=project_id,
            item_view_url_pattern=item_view_url_pattern,
        )

        api_integration_config_otrs.additional_properties = d
        return api_integration_config_otrs

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
