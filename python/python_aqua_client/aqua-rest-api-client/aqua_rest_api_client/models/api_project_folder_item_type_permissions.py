from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_permission_result import ApiPermissionResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectFolderItemTypePermissions")


@attr.s(auto_attribs=True)
class ApiProjectFolderItemTypePermissions:
    """Represents item-type related permissions in a project folder.

    Attributes:
        can_view_item (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_create_item (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_view_item_any_subfolder (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_edit_item_any_subfolder (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_cut_item_any_subfolder (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_batch_edit_item_any_subfolder (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
            check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_create_item_any_subfolder (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
            check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_delete_item_any_subfolder (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
            check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_execute_test_case_automated (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
            check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_execute_test_case_manual (Union[Unset, ApiPermissionResult]): Defined possible results of a permission
            check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
        can_finalize_test_execution (Union[Unset, ApiPermissionResult]): Defined possible results of a permission check.
            This enum has the following values:
              - `Denied` The given permission is deined, although is included in the license.
              - `Granted` The given permission is granted.
              - `NotLicensed` The given permission is not even licensed (so denied).
    """

    can_view_item: Union[Unset, ApiPermissionResult] = UNSET
    can_create_item: Union[Unset, ApiPermissionResult] = UNSET
    can_view_item_any_subfolder: Union[Unset, ApiPermissionResult] = UNSET
    can_edit_item_any_subfolder: Union[Unset, ApiPermissionResult] = UNSET
    can_cut_item_any_subfolder: Union[Unset, ApiPermissionResult] = UNSET
    can_batch_edit_item_any_subfolder: Union[Unset, ApiPermissionResult] = UNSET
    can_create_item_any_subfolder: Union[Unset, ApiPermissionResult] = UNSET
    can_delete_item_any_subfolder: Union[Unset, ApiPermissionResult] = UNSET
    can_execute_test_case_automated: Union[Unset, ApiPermissionResult] = UNSET
    can_execute_test_case_manual: Union[Unset, ApiPermissionResult] = UNSET
    can_finalize_test_execution: Union[Unset, ApiPermissionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_view_item: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_item, Unset):
            can_view_item = self.can_view_item.value

        can_create_item: Union[Unset, str] = UNSET
        if not isinstance(self.can_create_item, Unset):
            can_create_item = self.can_create_item.value

        can_view_item_any_subfolder: Union[Unset, str] = UNSET
        if not isinstance(self.can_view_item_any_subfolder, Unset):
            can_view_item_any_subfolder = self.can_view_item_any_subfolder.value

        can_edit_item_any_subfolder: Union[Unset, str] = UNSET
        if not isinstance(self.can_edit_item_any_subfolder, Unset):
            can_edit_item_any_subfolder = self.can_edit_item_any_subfolder.value

        can_cut_item_any_subfolder: Union[Unset, str] = UNSET
        if not isinstance(self.can_cut_item_any_subfolder, Unset):
            can_cut_item_any_subfolder = self.can_cut_item_any_subfolder.value

        can_batch_edit_item_any_subfolder: Union[Unset, str] = UNSET
        if not isinstance(self.can_batch_edit_item_any_subfolder, Unset):
            can_batch_edit_item_any_subfolder = self.can_batch_edit_item_any_subfolder.value

        can_create_item_any_subfolder: Union[Unset, str] = UNSET
        if not isinstance(self.can_create_item_any_subfolder, Unset):
            can_create_item_any_subfolder = self.can_create_item_any_subfolder.value

        can_delete_item_any_subfolder: Union[Unset, str] = UNSET
        if not isinstance(self.can_delete_item_any_subfolder, Unset):
            can_delete_item_any_subfolder = self.can_delete_item_any_subfolder.value

        can_execute_test_case_automated: Union[Unset, str] = UNSET
        if not isinstance(self.can_execute_test_case_automated, Unset):
            can_execute_test_case_automated = self.can_execute_test_case_automated.value

        can_execute_test_case_manual: Union[Unset, str] = UNSET
        if not isinstance(self.can_execute_test_case_manual, Unset):
            can_execute_test_case_manual = self.can_execute_test_case_manual.value

        can_finalize_test_execution: Union[Unset, str] = UNSET
        if not isinstance(self.can_finalize_test_execution, Unset):
            can_finalize_test_execution = self.can_finalize_test_execution.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_view_item is not UNSET:
            field_dict["CanViewItem"] = can_view_item
        if can_create_item is not UNSET:
            field_dict["CanCreateItem"] = can_create_item
        if can_view_item_any_subfolder is not UNSET:
            field_dict["CanViewItemAnySubfolder"] = can_view_item_any_subfolder
        if can_edit_item_any_subfolder is not UNSET:
            field_dict["CanEditItemAnySubfolder"] = can_edit_item_any_subfolder
        if can_cut_item_any_subfolder is not UNSET:
            field_dict["CanCutItemAnySubfolder"] = can_cut_item_any_subfolder
        if can_batch_edit_item_any_subfolder is not UNSET:
            field_dict["CanBatchEditItemAnySubfolder"] = can_batch_edit_item_any_subfolder
        if can_create_item_any_subfolder is not UNSET:
            field_dict["CanCreateItemAnySubfolder"] = can_create_item_any_subfolder
        if can_delete_item_any_subfolder is not UNSET:
            field_dict["CanDeleteItemAnySubfolder"] = can_delete_item_any_subfolder
        if can_execute_test_case_automated is not UNSET:
            field_dict["CanExecuteTestCaseAutomated"] = can_execute_test_case_automated
        if can_execute_test_case_manual is not UNSET:
            field_dict["CanExecuteTestCaseManual"] = can_execute_test_case_manual
        if can_finalize_test_execution is not UNSET:
            field_dict["CanFinalizeTestExecution"] = can_finalize_test_execution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _can_view_item = d.pop("CanViewItem", UNSET)
        can_view_item: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_item, Unset):
            can_view_item = UNSET
        else:
            can_view_item = ApiPermissionResult(_can_view_item)

        _can_create_item = d.pop("CanCreateItem", UNSET)
        can_create_item: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create_item, Unset):
            can_create_item = UNSET
        else:
            can_create_item = ApiPermissionResult(_can_create_item)

        _can_view_item_any_subfolder = d.pop("CanViewItemAnySubfolder", UNSET)
        can_view_item_any_subfolder: Union[Unset, ApiPermissionResult]
        if isinstance(_can_view_item_any_subfolder, Unset):
            can_view_item_any_subfolder = UNSET
        else:
            can_view_item_any_subfolder = ApiPermissionResult(_can_view_item_any_subfolder)

        _can_edit_item_any_subfolder = d.pop("CanEditItemAnySubfolder", UNSET)
        can_edit_item_any_subfolder: Union[Unset, ApiPermissionResult]
        if isinstance(_can_edit_item_any_subfolder, Unset):
            can_edit_item_any_subfolder = UNSET
        else:
            can_edit_item_any_subfolder = ApiPermissionResult(_can_edit_item_any_subfolder)

        _can_cut_item_any_subfolder = d.pop("CanCutItemAnySubfolder", UNSET)
        can_cut_item_any_subfolder: Union[Unset, ApiPermissionResult]
        if isinstance(_can_cut_item_any_subfolder, Unset):
            can_cut_item_any_subfolder = UNSET
        else:
            can_cut_item_any_subfolder = ApiPermissionResult(_can_cut_item_any_subfolder)

        _can_batch_edit_item_any_subfolder = d.pop("CanBatchEditItemAnySubfolder", UNSET)
        can_batch_edit_item_any_subfolder: Union[Unset, ApiPermissionResult]
        if isinstance(_can_batch_edit_item_any_subfolder, Unset):
            can_batch_edit_item_any_subfolder = UNSET
        else:
            can_batch_edit_item_any_subfolder = ApiPermissionResult(_can_batch_edit_item_any_subfolder)

        _can_create_item_any_subfolder = d.pop("CanCreateItemAnySubfolder", UNSET)
        can_create_item_any_subfolder: Union[Unset, ApiPermissionResult]
        if isinstance(_can_create_item_any_subfolder, Unset):
            can_create_item_any_subfolder = UNSET
        else:
            can_create_item_any_subfolder = ApiPermissionResult(_can_create_item_any_subfolder)

        _can_delete_item_any_subfolder = d.pop("CanDeleteItemAnySubfolder", UNSET)
        can_delete_item_any_subfolder: Union[Unset, ApiPermissionResult]
        if isinstance(_can_delete_item_any_subfolder, Unset):
            can_delete_item_any_subfolder = UNSET
        else:
            can_delete_item_any_subfolder = ApiPermissionResult(_can_delete_item_any_subfolder)

        _can_execute_test_case_automated = d.pop("CanExecuteTestCaseAutomated", UNSET)
        can_execute_test_case_automated: Union[Unset, ApiPermissionResult]
        if isinstance(_can_execute_test_case_automated, Unset):
            can_execute_test_case_automated = UNSET
        else:
            can_execute_test_case_automated = ApiPermissionResult(_can_execute_test_case_automated)

        _can_execute_test_case_manual = d.pop("CanExecuteTestCaseManual", UNSET)
        can_execute_test_case_manual: Union[Unset, ApiPermissionResult]
        if isinstance(_can_execute_test_case_manual, Unset):
            can_execute_test_case_manual = UNSET
        else:
            can_execute_test_case_manual = ApiPermissionResult(_can_execute_test_case_manual)

        _can_finalize_test_execution = d.pop("CanFinalizeTestExecution", UNSET)
        can_finalize_test_execution: Union[Unset, ApiPermissionResult]
        if isinstance(_can_finalize_test_execution, Unset):
            can_finalize_test_execution = UNSET
        else:
            can_finalize_test_execution = ApiPermissionResult(_can_finalize_test_execution)

        api_project_folder_item_type_permissions = cls(
            can_view_item=can_view_item,
            can_create_item=can_create_item,
            can_view_item_any_subfolder=can_view_item_any_subfolder,
            can_edit_item_any_subfolder=can_edit_item_any_subfolder,
            can_cut_item_any_subfolder=can_cut_item_any_subfolder,
            can_batch_edit_item_any_subfolder=can_batch_edit_item_any_subfolder,
            can_create_item_any_subfolder=can_create_item_any_subfolder,
            can_delete_item_any_subfolder=can_delete_item_any_subfolder,
            can_execute_test_case_automated=can_execute_test_case_automated,
            can_execute_test_case_manual=can_execute_test_case_manual,
            can_finalize_test_execution=can_finalize_test_execution,
        )

        return api_project_folder_item_type_permissions
