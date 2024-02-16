from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_identifier import ApiItemIdentifier
    from ..models.api_relation import ApiRelation


T = TypeVar("T", bound="ApiRelations")


@attr.s(auto_attribs=True)
class ApiRelations:
    """Contains the requested relations together with some information
    on the item for which the relations were requested.

        Attributes:
            item (Union[Unset, None, ApiItemIdentifier]):
            depth (Union[Unset, int]): The depth (number of levels) for which the relations
                were requested.
            relations (Union[Unset, None, List['ApiRelation']]): The relations of the items. Might contain several
                levels of relations depending on the requested depth.
    """

    item: Union[Unset, None, "ApiItemIdentifier"] = UNSET
    depth: Union[Unset, int] = UNSET
    relations: Union[Unset, None, List["ApiRelation"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict() if self.item else None

        depth = self.depth
        relations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relations, Unset):
            if self.relations is None:
                relations = None
            else:
                relations = []
                for relations_item_data in self.relations:
                    relations_item = relations_item_data.to_dict()

                    relations.append(relations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item is not UNSET:
            field_dict["Item"] = item
        if depth is not UNSET:
            field_dict["Depth"] = depth
        if relations is not UNSET:
            field_dict["Relations"] = relations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_identifier import ApiItemIdentifier
        from ..models.api_relation import ApiRelation

        d = src_dict.copy()
        _item = d.pop("Item", UNSET)
        item: Union[Unset, None, ApiItemIdentifier]
        if _item is None:
            item = None
        elif isinstance(_item, Unset):
            item = UNSET
        else:
            item = ApiItemIdentifier.from_dict(_item)

        depth = d.pop("Depth", UNSET)

        relations = []
        _relations = d.pop("Relations", UNSET)
        for relations_item_data in _relations or []:
            relations_item = ApiRelation.from_dict(relations_item_data)

            relations.append(relations_item)

        api_relations = cls(
            item=item,
            depth=depth,
            relations=relations,
        )

        return api_relations
