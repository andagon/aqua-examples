from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_folder_item_type_permissions import ApiProjectFolderItemTypePermissions


T = TypeVar("T", bound="ApiProjectFolderPermissions")


@attr.s(auto_attribs=True)
class ApiProjectFolderPermissions:
    """Represents permissions in a project.

    Attributes:
        requirement (Union[Unset, None, ApiProjectFolderItemTypePermissions]): Represents item-type related permissions
            in a project folder.
        defect (Union[Unset, None, ApiProjectFolderItemTypePermissions]): Represents item-type related permissions in a
            project folder.
        test_case (Union[Unset, None, ApiProjectFolderItemTypePermissions]): Represents item-type related permissions in
            a project folder.
        test_scenario (Union[Unset, None, ApiProjectFolderItemTypePermissions]): Represents item-type related
            permissions in a project folder.
        script (Union[Unset, None, ApiProjectFolderItemTypePermissions]): Represents item-type related permissions in a
            project folder.
        can_manage_tree (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_import_items (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_export_items (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
    """

    requirement: Union[Unset, None, "ApiProjectFolderItemTypePermissions"] = UNSET
    defect: Union[Unset, None, "ApiProjectFolderItemTypePermissions"] = UNSET
    test_case: Union[Unset, None, "ApiProjectFolderItemTypePermissions"] = UNSET
    test_scenario: Union[Unset, None, "ApiProjectFolderItemTypePermissions"] = UNSET
    script: Union[Unset, None, "ApiProjectFolderItemTypePermissions"] = UNSET
    can_manage_tree: Union[Unset, ApiPermissionResult] = UNSET
    can_import_items: Union[Unset, ApiPermissionResult] = UNSET
    can_export_items: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        requirement: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.requirement, Unset):
            requirement = self.requirement.to_dict() if self.requirement else None

        defect: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.defect, Unset):
            defect = self.defect.to_dict() if self.defect else None

        test_case: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.test_case, Unset):
            test_case = self.test_case.to_dict() if self.test_case else None

        test_scenario: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.test_scenario, Unset):
            test_scenario = self.test_scenario.to_dict() if self.test_scenario else None

        script: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.script, Unset):
            script = self.script.to_dict() if self.script else None

        can_manage_tree: Union[Unset, str] = UNSET
        if not isinstance(self.can_manage_tree, Unset):
            can_manage_tree = self.can_manage_tree.value

        can_import_items: Union[Unset, str] = UNSET
        if not isinstance(self.can_import_items, Unset):
            can_import_items = self.can_import_items.value

        can_export_items: Union[Unset, str] = UNSET
        if not isinstance(self.can_export_items, Unset):
            can_export_items = self.can_export_items.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if requirement is not UNSET:
            field_dict["Requirement"] = requirement
        if defect is not UNSET:
            field_dict["Defect"] = defect
        if test_case is not UNSET:
            field_dict["TestCase"] = test_case
        if test_scenario is not UNSET:
            field_dict["TestScenario"] = test_scenario
        if script is not UNSET:
            field_dict["Script"] = script
        if can_manage_tree is not UNSET:
            field_dict["CanManageTree"] = can_manage_tree
        if can_import_items is not UNSET:
            field_dict["CanImportItems"] = can_import_items
        if can_export_items is not UNSET:
            field_dict["CanExportItems"] = can_export_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_project_folder_item_type_permissions import ApiProjectFolderItemTypePermissions

        d = src_dict.copy()
        _requirement = d.pop("Requirement", UNSET)
        requirement: Union[Unset, None, ApiProjectFolderItemTypePermissions]
        if _requirement is None:
            requirement = None
        elif isinstance(_requirement, Unset):
            requirement = UNSET
        else:
            requirement = ApiProjectFolderItemTypePermissions.from_dict(_requirement)

        _defect = d.pop("Defect", UNSET)
        defect: Union[Unset, None, ApiProjectFolderItemTypePermissions]
        if _defect is None:
            defect = None
        elif isinstance(_defect, Unset):
            defect = UNSET
        else:
            defect = ApiProjectFolderItemTypePermissions.from_dict(_defect)

        _test_case = d.pop("TestCase", UNSET)
        test_case: Union[Unset, None, ApiProjectFolderItemTypePermissions]
        if _test_case is None:
            test_case = None
        elif isinstance(_test_case, Unset):
            test_case = UNSET
        else:
            test_case = ApiProjectFolderItemTypePermissions.from_dict(_test_case)

        _test_scenario = d.pop("TestScenario", UNSET)
        test_scenario: Union[Unset, None, ApiProjectFolderItemTypePermissions]
        if _test_scenario is None:
            test_scenario = None
        elif isinstance(_test_scenario, Unset):
            test_scenario = UNSET
        else:
            test_scenario = ApiProjectFolderItemTypePermissions.from_dict(_test_scenario)

        _script = d.pop("Script", UNSET)
        script: Union[Unset, None, ApiProjectFolderItemTypePermissions]
        if _script is None:
            script = None
        elif isinstance(_script, Unset):
            script = UNSET
        else:
            script = ApiProjectFolderItemTypePermissions.from_dict(_script)

        _can_manage_tree = d.pop("CanManageTree", UNSET)
        can_manage_tree: Union[Unset, ApiPermissionResult]
        if isinstance(_can_manage_tree, Unset):
            can_manage_tree = UNSET
        else:
            can_manage_tree = ApiPermissionResult(_can_manage_tree)

        _can_import_items = d.pop("CanImportItems", UNSET)
        can_import_items: Union[Unset, ApiPermissionResult]
        if isinstance(_can_import_items, Unset):
            can_import_items = UNSET
        else:
            can_import_items = ApiPermissionResult(_can_import_items)

        _can_export_items = d.pop("CanExportItems", UNSET)
        can_export_items: Union[Unset, ApiPermissionResult]
        if isinstance(_can_export_items, Unset):
            can_export_items = UNSET
        else:
            can_export_items = ApiPermissionResult(_can_export_items)

        api_project_folder_permissions = cls(
            requirement=requirement,
            defect=defect,
            test_case=test_case,
            test_scenario=test_scenario,
            script=script,
            can_manage_tree=can_manage_tree,
            can_import_items=can_import_items,
            can_export_items=can_export_items,
        )

        return api_project_folder_permissions
