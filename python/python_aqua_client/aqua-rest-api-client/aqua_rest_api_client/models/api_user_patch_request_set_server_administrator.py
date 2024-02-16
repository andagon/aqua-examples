from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUserPatchRequestSetServerAdministrator")


@attr.s(auto_attribs=True)
class ApiUserPatchRequestSetServerAdministrator:
    """
    Attributes:
        operation_type (str):
        server_administrator (Union[Unset, bool]): Server administrator flag.
    """

    operation_type: str
    server_administrator: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        server_administrator = self.server_administrator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if server_administrator is not UNSET:
            field_dict["ServerAdministrator"] = server_administrator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        server_administrator = d.pop("ServerAdministrator", UNSET)

        api_user_patch_request_set_server_administrator = cls(
            operation_type=operation_type,
            server_administrator=server_administrator,
        )

        api_user_patch_request_set_server_administrator.additional_properties = d
        return api_user_patch_request_set_server_administrator

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
