from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiIntegrationConfigVerifyJira")


@attr.s(auto_attribs=True)
class ApiIntegrationConfigVerifyJira:
    """
    Attributes:
        integration_type (str):
        api_base_url (Union[Unset, None, str]):
        api_user (Union[Unset, None, str]):
        api_password (Union[Unset, None, str]):
    """

    integration_type: str
    api_base_url: Union[Unset, None, str] = UNSET
    api_user: Union[Unset, None, str] = UNSET
    api_password: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        integration_type = self.integration_type
        api_base_url = self.api_base_url
        api_user = self.api_user
        api_password = self.api_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "IntegrationType": integration_type,
            }
        )
        if api_base_url is not UNSET:
            field_dict["APIBaseURL"] = api_base_url
        if api_user is not UNSET:
            field_dict["APIUser"] = api_user
        if api_password is not UNSET:
            field_dict["APIPassword"] = api_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        integration_type = d.pop("IntegrationType")

        api_base_url = d.pop("APIBaseURL", UNSET)

        api_user = d.pop("APIUser", UNSET)

        api_password = d.pop("APIPassword", UNSET)

        api_integration_config_verify_jira = cls(
            integration_type=integration_type,
            api_base_url=api_base_url,
            api_user=api_user,
            api_password=api_password,
        )

        api_integration_config_verify_jira.additional_properties = d
        return api_integration_config_verify_jira

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
