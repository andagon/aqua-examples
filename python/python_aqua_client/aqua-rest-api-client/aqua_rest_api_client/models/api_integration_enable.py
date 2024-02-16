from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiIntegrationEnable")


@attr.s(auto_attribs=True)
class ApiIntegrationEnable:
    """The body for the integration enable request

    Attributes:
        customer_id (Union[Unset, int]): The customer id of the integration
        project_id (Union[Unset, None, int]): The project id of the integration
        is_enabled (Union[Unset, bool]): A flag to indicate if the integration should be enabled
    """

    customer_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, None, int] = UNSET
    is_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
        project_id = self.project_id
        is_enabled = self.is_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["CustomerId"] = customer_id
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if is_enabled is not UNSET:
            field_dict["IsEnabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_id = d.pop("CustomerId", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        is_enabled = d.pop("IsEnabled", UNSET)

        api_integration_enable = cls(
            customer_id=customer_id,
            project_id=project_id,
            is_enabled=is_enabled,
        )

        return api_integration_enable
