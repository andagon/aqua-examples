from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_rules import ApiFieldRules
    from ..models.api_project_id_name import ApiProjectIdName


T = TypeVar("T", bound="ApiProjectFieldRules")


@attr.s(auto_attribs=True)
class ApiProjectFieldRules:
    """Contains the FieldRules for all item types for a certain project.

    Attributes:
        project (ApiProjectIdName): Holds the id and the name of a project.
        is_shared (bool): Indicates whether the project configuration is shared with
            a different project.
        is_owned (bool): Indicates whether the project configuration is owned by the
            project for which this part of the configuration was requested.
        rules (List['ApiFieldRules']): Contains the FieldRules for each item type.
        owning_project (Union[Unset, None, ApiProjectIdName]): Holds the id and the name of a project.
    """

    project: "ApiProjectIdName"
    is_shared: bool
    is_owned: bool
    rules: List["ApiFieldRules"]
    owning_project: Union[Unset, None, "ApiProjectIdName"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project = self.project.to_dict()

        is_shared = self.is_shared
        is_owned = self.is_owned
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()

            rules.append(rules_item)

        owning_project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owning_project, Unset):
            owning_project = self.owning_project.to_dict() if self.owning_project else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Project": project,
                "IsShared": is_shared,
                "IsOwned": is_owned,
                "Rules": rules,
            }
        )
        if owning_project is not UNSET:
            field_dict["OwningProject"] = owning_project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_rules import ApiFieldRules
        from ..models.api_project_id_name import ApiProjectIdName

        d = src_dict.copy()
        project = ApiProjectIdName.from_dict(d.pop("Project"))

        is_shared = d.pop("IsShared")

        is_owned = d.pop("IsOwned")

        rules = []
        _rules = d.pop("Rules")
        for rules_item_data in _rules:
            rules_item = ApiFieldRules.from_dict(rules_item_data)

            rules.append(rules_item)

        _owning_project = d.pop("OwningProject", UNSET)
        owning_project: Union[Unset, None, ApiProjectIdName]
        if _owning_project is None:
            owning_project = None
        elif isinstance(_owning_project, Unset):
            owning_project = UNSET
        else:
            owning_project = ApiProjectIdName.from_dict(_owning_project)

        api_project_field_rules = cls(
            project=project,
            is_shared=is_shared,
            is_owned=is_owned,
            rules=rules,
            owning_project=owning_project,
        )

        return api_project_field_rules
