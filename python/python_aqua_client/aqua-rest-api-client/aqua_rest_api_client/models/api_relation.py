from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..models.api_relation_type import ApiRelationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_identifier import ApiItemIdentifier
    from ..models.i_api_relation_item_extra import IApiRelationItemExtra


T = TypeVar("T", bound="ApiRelation")


@attr.s(auto_attribs=True)
class ApiRelation:
    """Represents a relation between to items. These items might belong
    either to aqua or to an external system.

       Attributes:
           id (Union[Unset, None, str]): The id of the relation itself.
           type (Union[Unset, ApiRelationType]): Identifies the type of relation.
               This enum has the following values:
                 - `AffectsExecution` The item affects an execution.
               This is the reverse of ExecutionAffectedBy.
                 - `AlternativeTo` This item is an alternative to the other item
                 - `ConflictsWith` This item conflicts with the other item.
                 - `DependsOn` This item depends on the other item.
               This is the reverse of HasDependentItem.
                 - `Details` This item details the other item.
               This is the reverse of IsDetailedBy.
                 - `Duplicates` This item duplicates the other item.
                 - `ExecutionAffectedBy` The item (which is an execution) is affected by the other item.
               This is the reverse of AffectsExecution.
                 - `HasDependentItem` The other item depends on this item.
               This is the reverse of DependsOn.
                 - `HasNewerVersion` This item has a new version which is the other item.
               This is the reverse of IsNewerVersionOf.
                 - `HasPrecondition` This item has the other item as a precondition.
               This is the reverse of IsPreconditionOf.
                 - `IsCopyOf` This item is a copy of the other item.
               This is the reverse of WasCopiedBy.
                 - `IsDetailedBy` This item is detailed by the other item meaning
               that the other item contains additional details for this item.
               This is the reverse of Details.
                 - `IsNestedIn` This item (test case) is nested in another item (another test case).
               This is the reverse of Nests.
                 - `IsNewerVersionOf` This item is a newer version of the other item.
               This is the reverse of HasNewerVersion.
                 - `IsPreconditionOf` This item is a precondition of the other item.
               This is the reverse of HasPrecondition.
                 - `IsUtilityScriptOf` This item is a utility script of the other item.
               This is the reverse of UsesUtilityScript.
                 - `IsVerifiedBy` This item is verified by the other item.
               This is the reverse of Verifies.
                 - `Nests` This item (test case) nestst the other item (test case).
               This is the reverse of IsNestedIn.
                 - `ReferencesTestCaseTestData` This item (test case) references test data from the other item (test case).
               This is the reverse of SharesTestDataWith.
                 - `RelatedTo` This item is related to the other item.
                 - `SharesTestDataWith` This item (test case) shares its test data with another item (another test case).
               This is the reverse of ReferencesTestCaseTestData.
                 - `UsesUtilityScript` This item uses the other item as a utility script.
               This is the reverse of IsUtilityScriptOf.
                 - `Verifies` This item verifies the other item.
               This is the reverse of IsVerifiedBy.
                 - `WasCopiedTo` This item was copied to the other item.
               This is the reverse of IsCopyOf.
           item (Union[Unset, None, ApiItemIdentifier]):
           item_extra (Union[Unset, None, IApiRelationItemExtra]): Holds additional, relation-specific data for one side of
               a relation.
           other_item (Union[Unset, None, ApiItemIdentifier]):
           other_item_extra (Union[Unset, None, IApiRelationItemExtra]): Holds additional, relation-specific data for one
               side of a relation.
           other_item_can_view (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
               This enum has the following values:
                 - `Denied` The given permission is deined, although is included in the license.
                 - `Granted` The given permission is granted.
                 - `NotLicensed` The given permission is not even licensed (so denied).
    """

    id: Union[Unset, None, str] = UNSET
    type: Union[Unset, ApiRelationType] = UNSET
    item: Union[Unset, None, "ApiItemIdentifier"] = UNSET
    item_extra: Union[Unset, None, "IApiRelationItemExtra"] = UNSET
    other_item: Union[Unset, None, "ApiItemIdentifier"] = UNSET
    other_item_extra: Union[Unset, None, "IApiRelationItemExtra"] = UNSET
    other_item_can_view: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict() if self.item else None

        item_extra: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.item_extra, Unset):
            item_extra = self.item_extra.to_dict() if self.item_extra else None

        other_item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.other_item, Unset):
            other_item = self.other_item.to_dict() if self.other_item else None

        other_item_extra: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.other_item_extra, Unset):
            other_item_extra = self.other_item_extra.to_dict() if self.other_item_extra else None

        other_item_can_view: Union[Unset, str] = UNSET
        if not isinstance(self.other_item_can_view, Unset):
            other_item_can_view = self.other_item_can_view.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if type is not UNSET:
            field_dict["Type"] = type
        if item is not UNSET:
            field_dict["Item"] = item
        if item_extra is not UNSET:
            field_dict["ItemExtra"] = item_extra
        if other_item is not UNSET:
            field_dict["OtherItem"] = other_item
        if other_item_extra is not UNSET:
            field_dict["OtherItemExtra"] = other_item_extra
        if other_item_can_view is not UNSET:
            field_dict["OtherItemCanView"] = other_item_can_view

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_identifier import ApiItemIdentifier
        from ..models.i_api_relation_item_extra import IApiRelationItemExtra

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiRelationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiRelationType(_type)

        _item = d.pop("Item", UNSET)
        item: Union[Unset, None, ApiItemIdentifier]
        if _item is None:
            item = None
        elif isinstance(_item, Unset):
            item = UNSET
        else:
            item = ApiItemIdentifier.from_dict(_item)

        _item_extra = d.pop("ItemExtra", UNSET)
        item_extra: Union[Unset, None, IApiRelationItemExtra]
        if _item_extra is None:
            item_extra = None
        elif isinstance(_item_extra, Unset):
            item_extra = UNSET
        else:
            item_extra = IApiRelationItemExtra.from_dict(_item_extra)

        _other_item = d.pop("OtherItem", UNSET)
        other_item: Union[Unset, None, ApiItemIdentifier]
        if _other_item is None:
            other_item = None
        elif isinstance(_other_item, Unset):
            other_item = UNSET
        else:
            other_item = ApiItemIdentifier.from_dict(_other_item)

        _other_item_extra = d.pop("OtherItemExtra", UNSET)
        other_item_extra: Union[Unset, None, IApiRelationItemExtra]
        if _other_item_extra is None:
            other_item_extra = None
        elif isinstance(_other_item_extra, Unset):
            other_item_extra = UNSET
        else:
            other_item_extra = IApiRelationItemExtra.from_dict(_other_item_extra)

        _other_item_can_view = d.pop("OtherItemCanView", UNSET)
        other_item_can_view: Union[Unset, ApiPermissionResult]
        if isinstance(_other_item_can_view, Unset):
            other_item_can_view = UNSET
        else:
            other_item_can_view = ApiPermissionResult(_other_item_can_view)

        api_relation = cls(
            id=id,
            type=type,
            item=item,
            item_extra=item_extra,
            other_item=other_item,
            other_item_extra=other_item_extra,
            other_item_can_view=other_item_can_view,
        )

        return api_relation
