from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_pdf_changing_permissions import ApiPdfChangingPermissions
from ..models.api_pdf_printing_permissions import ApiPdfPrintingPermissions
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPdfPermissionsOptions")


@attr.s(auto_attribs=True)
class ApiPdfPermissionsOptions:
    """
    Attributes:
        changing_permissions (Union[Unset, ApiPdfChangingPermissions]):
            This enum has the following values:
              - `AnyExceptExtractingPages` Permits any changes for the PDF document, except extracting its pages.
              - `CommentingFillingSigning` Permits commenting, filling in form fields, and signing existing signature fields
            for the PDF document.
              - `FillingSigning` Permits filling in form fields and signing existing signature fields for the PDF document.
              - `InsertingDeletingRotating` Permits inserting, deleting and rotating the PDF document’s pages.
              - `None` No changes are permitted to the PDF document.
             Default: ApiPdfChangingPermissions.NONE.
        printing_permissions (Union[Unset, ApiPdfPrintingPermissions]):
            This enum has the following values:
              - `HighResolution` Permits the PDF document’s printing in high resolution only
              - `LowResolution` Permits the PDF document’s printing in low resolution only (150 dpi)
              - `None` Forbids printing of the PDF document
             Default: ApiPdfPrintingPermissions.NONE.
        enable_screen_readers (Union[Unset, bool]): Permissions for screen readers access to the exported PDF document
            Default: True.
        enable_copying (Union[Unset, bool]): Permissions for copying the content of the exported PDF document.
    """

    changing_permissions: Union[Unset, ApiPdfChangingPermissions] = ApiPdfChangingPermissions.NONE
    printing_permissions: Union[Unset, ApiPdfPrintingPermissions] = ApiPdfPrintingPermissions.NONE
    enable_screen_readers: Union[Unset, bool] = True
    enable_copying: Union[Unset, bool] = False

    def to_dict(self) -> Dict[str, Any]:
        changing_permissions: Union[Unset, str] = UNSET
        if not isinstance(self.changing_permissions, Unset):
            changing_permissions = self.changing_permissions.value

        printing_permissions: Union[Unset, str] = UNSET
        if not isinstance(self.printing_permissions, Unset):
            printing_permissions = self.printing_permissions.value

        enable_screen_readers = self.enable_screen_readers
        enable_copying = self.enable_copying

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if changing_permissions is not UNSET:
            field_dict["ChangingPermissions"] = changing_permissions
        if printing_permissions is not UNSET:
            field_dict["PrintingPermissions"] = printing_permissions
        if enable_screen_readers is not UNSET:
            field_dict["EnableScreenReaders"] = enable_screen_readers
        if enable_copying is not UNSET:
            field_dict["EnableCopying"] = enable_copying

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _changing_permissions = d.pop("ChangingPermissions", UNSET)
        changing_permissions: Union[Unset, ApiPdfChangingPermissions]
        if isinstance(_changing_permissions, Unset):
            changing_permissions = UNSET
        else:
            changing_permissions = ApiPdfChangingPermissions(_changing_permissions)

        _printing_permissions = d.pop("PrintingPermissions", UNSET)
        printing_permissions: Union[Unset, ApiPdfPrintingPermissions]
        if isinstance(_printing_permissions, Unset):
            printing_permissions = UNSET
        else:
            printing_permissions = ApiPdfPrintingPermissions(_printing_permissions)

        enable_screen_readers = d.pop("EnableScreenReaders", UNSET)

        enable_copying = d.pop("EnableCopying", UNSET)

        api_pdf_permissions_options = cls(
            changing_permissions=changing_permissions,
            printing_permissions=printing_permissions,
            enable_screen_readers=enable_screen_readers,
            enable_copying=enable_copying,
        )

        return api_pdf_permissions_options
