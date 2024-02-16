from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeatureInfo")


@attr.s(auto_attribs=True)
class ApiFeatureInfo:
    """The detail about a given feature

    Attributes:
        is_enabled (Union[Unset, bool]): If the feature is enabled or not
    """

    is_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_enabled = self.is_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["IsEnabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_enabled = d.pop("IsEnabled", UNSET)

        api_feature_info = cls(
            is_enabled=is_enabled,
        )

        return api_feature_info
