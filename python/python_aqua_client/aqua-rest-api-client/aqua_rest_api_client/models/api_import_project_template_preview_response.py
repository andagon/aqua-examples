from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_import_project_template_preview_entry import ApiImportProjectTemplatePreviewEntry


T = TypeVar("T", bound="ApiImportProjectTemplatePreviewResponse")


@attr.s(auto_attribs=True)
class ApiImportProjectTemplatePreviewResponse:
    """Represents the preview for the import of project configuration.

    Attributes:
        list_of_changes (Union[Unset, None, List['ApiImportProjectTemplatePreviewEntry']]): Represents the list of
            changes which need to be applied.
    """

    list_of_changes: Union[Unset, None, List["ApiImportProjectTemplatePreviewEntry"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        list_of_changes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.list_of_changes, Unset):
            if self.list_of_changes is None:
                list_of_changes = None
            else:
                list_of_changes = []
                for list_of_changes_item_data in self.list_of_changes:
                    list_of_changes_item = list_of_changes_item_data.to_dict()

                    list_of_changes.append(list_of_changes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if list_of_changes is not UNSET:
            field_dict["ListOfChanges"] = list_of_changes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_import_project_template_preview_entry import ApiImportProjectTemplatePreviewEntry

        d = src_dict.copy()
        list_of_changes = []
        _list_of_changes = d.pop("ListOfChanges", UNSET)
        for list_of_changes_item_data in _list_of_changes or []:
            list_of_changes_item = ApiImportProjectTemplatePreviewEntry.from_dict(list_of_changes_item_data)

            list_of_changes.append(list_of_changes_item)

        api_import_project_template_preview_response = cls(
            list_of_changes=list_of_changes,
        )

        return api_import_project_template_preview_response
