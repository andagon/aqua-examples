from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_relation_create_meta_allowed_types import ApiRelationCreateMetaAllowedTypes


T = TypeVar("T", bound="ApiRelationCreateMeta")


@attr.s(auto_attribs=True)
class ApiRelationCreateMeta:
    """The necessary metadata to create new relations for a
    certain item.

        Attributes:
            allowed_types (Union[Unset, None, ApiRelationCreateMetaAllowedTypes]): Contains for each item type the list of
                relations types which are allowed between
                the source item and items of the given item type.
    """

    allowed_types: Union[Unset, None, "ApiRelationCreateMetaAllowedTypes"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        allowed_types: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.allowed_types, Unset):
            allowed_types = self.allowed_types.to_dict() if self.allowed_types else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if allowed_types is not UNSET:
            field_dict["AllowedTypes"] = allowed_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_relation_create_meta_allowed_types import ApiRelationCreateMetaAllowedTypes

        d = src_dict.copy()
        _allowed_types = d.pop("AllowedTypes", UNSET)
        allowed_types: Union[Unset, None, ApiRelationCreateMetaAllowedTypes]
        if _allowed_types is None:
            allowed_types = None
        elif isinstance(_allowed_types, Unset):
            allowed_types = UNSET
        else:
            allowed_types = ApiRelationCreateMetaAllowedTypes.from_dict(_allowed_types)

        api_relation_create_meta = cls(
            allowed_types=allowed_types,
        )

        return api_relation_create_meta
