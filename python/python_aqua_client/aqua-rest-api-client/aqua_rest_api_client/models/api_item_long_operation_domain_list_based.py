from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemLongOperationDomainListBased")


@attr.s(auto_attribs=True)
class ApiItemLongOperationDomainListBased:
    """
    Attributes:
        type (str):
        project_id (Union[Unset, int]): Project where to look in.
        items (Union[Unset, None, List[int]]): List of ids of items
    """

    type: str
    project_id: Union[Unset, int] = UNSET
    items: Union[Unset, None, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        project_id = self.project_id
        items: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.items, Unset):
            if self.items is None:
                items = None
            else:
                items = self.items

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Type": type,
            }
        )
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if items is not UNSET:
            field_dict["Items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("Type")

        project_id = d.pop("ProjectId", UNSET)

        items = cast(List[int], d.pop("Items", UNSET))

        api_item_long_operation_domain_list_based = cls(
            type=type,
            project_id=project_id,
            items=items,
        )

        api_item_long_operation_domain_list_based.additional_properties = d
        return api_item_long_operation_domain_list_based

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
