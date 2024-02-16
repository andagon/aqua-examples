from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_dependency_type import ApiDependencyType
from ..models.api_history_dependency_change_type import ApiHistoryDependencyChangeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHistoryDependencyChanged")


@attr.s(auto_attribs=True)
class ApiHistoryDependencyChanged:
    """Contains information on the dependency which changed.

    Attributes:
        change_type (Union[Unset, ApiHistoryDependencyChangeType]): Indicates the type of change which occurred to a
            certain dependency
            This enum has the following values:
              - `Added` The dependency has been added
              - `Removed` The depencency has been removed
              - `TypeChanged` The type of the dependency has been changed
        item_name (Union[Unset, None, str]): The name of the current item at the time when the dependency
            has been modified
        other_item_name (Union[Unset, None, str]): The name of the other item which is part of this dependency
        dependency_type (Union[Unset, None, ApiDependencyType]): Identifies the type of dependency.
            This enum has the following values:
              - `AlternativeTo` This item is an alternative to the other item
              - `ConflictsWith` This item conflicts with the other item.
              - `DependsOn` This item depends on the other item.
            This is the reverse of HasDependentItem.
              - `Details` This item details the other item.
            This is the reverse of IsDetailedBy.
              - `Duplicates` This item duplicates the other item.
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
        old_dependency_type (Union[Unset, None, ApiDependencyType]): Identifies the type of dependency.
            This enum has the following values:
              - `AlternativeTo` This item is an alternative to the other item
              - `ConflictsWith` This item conflicts with the other item.
              - `DependsOn` This item depends on the other item.
            This is the reverse of HasDependentItem.
              - `Details` This item details the other item.
            This is the reverse of IsDetailedBy.
              - `Duplicates` This item duplicates the other item.
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

    change_type: Union[Unset, ApiHistoryDependencyChangeType] = UNSET
    item_name: Union[Unset, None, str] = UNSET
    other_item_name: Union[Unset, None, str] = UNSET
    dependency_type: Union[Unset, None, ApiDependencyType] = UNSET
    old_dependency_type: Union[Unset, None, ApiDependencyType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        change_type: Union[Unset, str] = UNSET
        if not isinstance(self.change_type, Unset):
            change_type = self.change_type.value

        item_name = self.item_name
        other_item_name = self.other_item_name
        dependency_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.dependency_type, Unset):
            dependency_type = self.dependency_type.value if self.dependency_type else None

        old_dependency_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.old_dependency_type, Unset):
            old_dependency_type = self.old_dependency_type.value if self.old_dependency_type else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if change_type is not UNSET:
            field_dict["ChangeType"] = change_type
        if item_name is not UNSET:
            field_dict["ItemName"] = item_name
        if other_item_name is not UNSET:
            field_dict["OtherItemName"] = other_item_name
        if dependency_type is not UNSET:
            field_dict["DependencyType"] = dependency_type
        if old_dependency_type is not UNSET:
            field_dict["OldDependencyType"] = old_dependency_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _change_type = d.pop("ChangeType", UNSET)
        change_type: Union[Unset, ApiHistoryDependencyChangeType]
        if isinstance(_change_type, Unset):
            change_type = UNSET
        else:
            change_type = ApiHistoryDependencyChangeType(_change_type)

        item_name = d.pop("ItemName", UNSET)

        other_item_name = d.pop("OtherItemName", UNSET)

        _dependency_type = d.pop("DependencyType", UNSET)
        dependency_type: Union[Unset, None, ApiDependencyType]
        if _dependency_type is None:
            dependency_type = None
        elif isinstance(_dependency_type, Unset):
            dependency_type = UNSET
        else:
            dependency_type = ApiDependencyType(_dependency_type)

        _old_dependency_type = d.pop("OldDependencyType", UNSET)
        old_dependency_type: Union[Unset, None, ApiDependencyType]
        if _old_dependency_type is None:
            old_dependency_type = None
        elif isinstance(_old_dependency_type, Unset):
            old_dependency_type = UNSET
        else:
            old_dependency_type = ApiDependencyType(_old_dependency_type)

        api_history_dependency_changed = cls(
            change_type=change_type,
            item_name=item_name,
            other_item_name=other_item_name,
            dependency_type=dependency_type,
            old_dependency_type=old_dependency_type,
        )

        return api_history_dependency_changed
