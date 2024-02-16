from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNavigationDependencyResponse")


@attr.s(auto_attribs=True)
class ApiNavigationDependencyResponse:
    """
    Attributes:
        dependent_item_ids (Union[Unset, None, List[int]]): The list of dependet item ids.
    """

    dependent_item_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        dependent_item_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.dependent_item_ids, Unset):
            if self.dependent_item_ids is None:
                dependent_item_ids = None
            else:
                dependent_item_ids = self.dependent_item_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if dependent_item_ids is not UNSET:
            field_dict["DependentItemIds"] = dependent_item_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dependent_item_ids = cast(List[int], d.pop("DependentItemIds", UNSET))

        api_navigation_dependency_response = cls(
            dependent_item_ids=dependent_item_ids,
        )

        return api_navigation_dependency_response
