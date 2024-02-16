from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..models.api_relation_type import ApiRelationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRelationNew")


@attr.s(auto_attribs=True)
class ApiRelationNew:
    """Contains the data necessary to create a new relation.

    Attributes:
        item_extra (Union[Unset, Any]): Contains relation-specific data for the source item of
            the new relation.
        other_item_id (Union[Unset, None, str]): The id of the target of the new relation.
        other_item_type (Union[Unset, ApiItemType]): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        other_item_extra (Union[Unset, Any]): Contains relation-specific data for the target item of
            the new relation.
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
    """

    item_extra: Union[Unset, Any] = UNSET
    other_item_id: Union[Unset, None, str] = UNSET
    other_item_type: Union[Unset, ApiItemType] = UNSET
    other_item_extra: Union[Unset, Any] = UNSET
    type: Union[Unset, ApiRelationType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_extra = self.item_extra
        other_item_id = self.other_item_id
        other_item_type: Union[Unset, str] = UNSET
        if not isinstance(self.other_item_type, Unset):
            other_item_type = self.other_item_type.value

        other_item_extra = self.other_item_extra
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_extra is not UNSET:
            field_dict["ItemExtra"] = item_extra
        if other_item_id is not UNSET:
            field_dict["OtherItemId"] = other_item_id
        if other_item_type is not UNSET:
            field_dict["OtherItemType"] = other_item_type
        if other_item_extra is not UNSET:
            field_dict["OtherItemExtra"] = other_item_extra
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_extra = d.pop("ItemExtra", UNSET)

        other_item_id = d.pop("OtherItemId", UNSET)

        _other_item_type = d.pop("OtherItemType", UNSET)
        other_item_type: Union[Unset, ApiItemType]
        if isinstance(_other_item_type, Unset):
            other_item_type = UNSET
        else:
            other_item_type = ApiItemType(_other_item_type)

        other_item_extra = d.pop("OtherItemExtra", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiRelationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiRelationType(_type)

        api_relation_new = cls(
            item_extra=item_extra,
            other_item_id=other_item_id,
            other_item_type=other_item_type,
            other_item_extra=other_item_extra,
            type=type,
        )

        return api_relation_new
