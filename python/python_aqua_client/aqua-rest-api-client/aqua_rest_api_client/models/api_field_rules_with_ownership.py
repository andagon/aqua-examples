from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_rule import ApiFieldRule
    from ..models.api_project_id_name import ApiProjectIdName


T = TypeVar("T", bound="ApiFieldRulesWithOwnership")


@attr.s(auto_attribs=True)
class ApiFieldRulesWithOwnership:
    """
    Attributes:
        item_type (ApiItemType): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        rules (List['ApiFieldRule']): The list of rules. Rules can be only one of the following types:
              - DependentValues: rules of this type restrict the possible values
                of a certain field based on the current value of another field.
              - Workflow: rules of this type specify actions which are executed when
                the value of a dictionary field is changed to a certain value.
                These actions include setting a field readonly, changing
                the value of a field, etc.
        project (ApiProjectIdName): Holds the id and the name of a project.
        is_shared (bool): Indicates whether the project configuration is shared with
            a different project.
        is_owned (bool): Indicates whether the project configuration is owned by the
            project for which this part of the configuration was requested.
        owning_project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
    """

    item_type: ApiItemType
    rules: List["ApiFieldRule"]
    project: "ApiProjectIdName"
    is_shared: bool
    is_owned: bool
    owning_project: Union[Unset, None, "ApiProjectIdName"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_type = self.item_type.value

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()

            rules.append(rules_item)

        project = self.project.to_dict()

        is_shared = self.is_shared
        is_owned = self.is_owned
        owning_project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owning_project, Unset):
            owning_project = self.owning_project.to_dict() if self.owning_project else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ItemType": item_type,
                "Rules": rules,
                "Project": project,
                "IsShared": is_shared,
                "IsOwned": is_owned,
            }
        )
        if owning_project is not UNSET:
            field_dict["OwningProject"] = owning_project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_rule import ApiFieldRule
        from ..models.api_project_id_name import ApiProjectIdName

        d = src_dict.copy()
        item_type = ApiItemType(d.pop("ItemType"))

        rules = []
        _rules = d.pop("Rules")
        for rules_item_data in _rules:
            rules_item = ApiFieldRule.from_dict(rules_item_data)

            rules.append(rules_item)

        project = ApiProjectIdName.from_dict(d.pop("Project"))

        is_shared = d.pop("IsShared")

        is_owned = d.pop("IsOwned")

        _owning_project = d.pop("OwningProject", UNSET)
        owning_project: Union[Unset, None, ApiProjectIdName]
        if _owning_project is None:
            owning_project = None
        elif isinstance(_owning_project, Unset):
            owning_project = UNSET
        else:
            owning_project = ApiProjectIdName.from_dict(_owning_project)

        api_field_rules_with_ownership = cls(
            item_type=item_type,
            rules=rules,
            project=project,
            is_shared=is_shared,
            is_owned=is_owned,
            owning_project=owning_project,
        )

        api_field_rules_with_ownership.additional_properties = d
        return api_field_rules_with_ownership

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
