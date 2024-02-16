from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiIntegrationConfigVerifyBase")


@attr.s(auto_attribs=True)
class ApiIntegrationConfigVerifyBase:
    """Base class for integration configuration update classes

    Attributes:
        integration_type (str):
    """

    integration_type: str

    def to_dict(self) -> Dict[str, Any]:
        integration_type = self.integration_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "IntegrationType": integration_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        integration_type = d.pop("IntegrationType")

        api_integration_config_verify_base = cls(
            integration_type=integration_type,
        )

        return api_integration_config_verify_base
