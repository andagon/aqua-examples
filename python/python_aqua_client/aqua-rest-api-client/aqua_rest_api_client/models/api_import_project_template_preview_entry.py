from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_diff_category_type import ApiDiffCategoryType
from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiImportProjectTemplatePreviewEntry")


@attr.s(auto_attribs=True)
class ApiImportProjectTemplatePreviewEntry:
    """
    Attributes:
        item_type (Union[Unset, None, ApiItemType]): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        description (Union[Unset, None, str]): The description of the future change.
        category (Union[Unset, ApiDiffCategoryType]): Identifies the type of item.
            This enum has the following values:
              - `FieldRules`
              - `Notification`
              - `Subtemplate`
              - `Template`
              - `Workflow`
        ready_to_import (Union[Unset, bool]): The flag which identifies if the future change can be done automatically.
        cause (Union[Unset, None, str]): The cause why the future change can not be done automatically.
    """

    item_type: Union[Unset, None, ApiItemType] = UNSET
    description: Union[Unset, None, str] = UNSET
    category: Union[Unset, ApiDiffCategoryType] = UNSET
    ready_to_import: Union[Unset, bool] = UNSET
    cause: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value if self.item_type else None

        description = self.description
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        ready_to_import = self.ready_to_import
        cause = self.cause

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if description is not UNSET:
            field_dict["Description"] = description
        if category is not UNSET:
            field_dict["Category"] = category
        if ready_to_import is not UNSET:
            field_dict["ReadyToImport"] = ready_to_import
        if cause is not UNSET:
            field_dict["Cause"] = cause

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, None, ApiItemType]
        if _item_type is None:
            item_type = None
        elif isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        description = d.pop("Description", UNSET)

        _category = d.pop("Category", UNSET)
        category: Union[Unset, ApiDiffCategoryType]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ApiDiffCategoryType(_category)

        ready_to_import = d.pop("ReadyToImport", UNSET)

        cause = d.pop("Cause", UNSET)

        api_import_project_template_preview_entry = cls(
            item_type=item_type,
            description=description,
            category=category,
            ready_to_import=ready_to_import,
            cause=cause,
        )

        return api_import_project_template_preview_entry
