from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_permission_result import ApiPermissionResult

T = TypeVar("T", bound="ApiItemPermissionsCanCreateDependentItem")


@attr.s(auto_attribs=True)
class ApiItemPermissionsCanCreateDependentItem:
    """Indicates whether the user is able to create a new dependent item of
    a certain type in the same folder as the current item is located in.

    """

    additional_properties: Dict[str, ApiPermissionResult] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_item_permissions_can_create_dependent_item = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ApiPermissionResult(prop_dict)

            additional_properties[prop_name] = additional_property

        api_item_permissions_can_create_dependent_item.additional_properties = additional_properties
        return api_item_permissions_can_create_dependent_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ApiPermissionResult:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ApiPermissionResult) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
