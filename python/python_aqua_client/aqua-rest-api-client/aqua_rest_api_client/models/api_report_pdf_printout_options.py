from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_pdf_a_compatibility import ApiPdfACompatibility
from ..models.api_pdf_image_quality import ApiPdfImageQuality
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_pdf_password_security_options import ApiPdfPasswordSecurityOptions
    from ..models.api_report_pdf_printout_document_options import ApiReportPdfPrintoutDocumentOptions


T = TypeVar("T", bound="ApiReportPdfPrintoutOptions")


@attr.s(auto_attribs=True)
class ApiReportPdfPrintoutOptions:
    """
    Attributes:
        page_range (Union[Unset, None, str]): The page range to be exported. Ranges are comma separated. e.g.
            “1,4,7-10”.
            Invalid page numbers are ignored, if all page numbers are invalid, all pages are exported. Default: ''.
        rasterization_resolution (Union[Unset, int]): The resolution (in DPI) used to rasterize vector images. Default:
            96.
        convert_images_to_jpeg (Union[Unset, bool]): When True, contained images will be converted to jpg. Default:
            True.
        show_print_dialog_on_open (Union[Unset, bool]): When true the print dialog is displayed on opening the pdf
        never_embedded_fonts (Union[Unset, None, str]): Semicolon delimited list of fonts never to embed in the pdf
            Default: ''.
        export_editing_fields_to_acro_forms (Union[Unset, bool]): Specifies whether to convert editable fields to
            AcroForms fields on PDF export.
        image_quality (Union[Unset, ApiPdfImageQuality]):
            This enum has the following values:
              - `High`
              - `Highest`
              - `Low`
              - `Lowest`
              - `Medium`
             Default: ApiPdfImageQuality.HIGHEST.
        pdf_a_compatibility (Union[Unset, ApiPdfACompatibility]): PDF/A compatibility mode of a document.
            This enum has the following values:
              - `None` The document is not PDF/A-compatible and supports the ISO 32000-1:2005 specification.
              - `PdfA1a` The document supports the PDF/A-1a (Accessible) specification and contains tags
            that assistive technologies can use.

              - `PdfA1b` The document supports the PDF/A-1b (ISO 19005-1) specification.

              - `PdfA2a` The document supports the PDF/A-2a (Accessible) specification and contains tags
            that assistive technologies can use.

              - `PdfA2b` The document supports the PDF/A-2b (ISO 19005-2:2011) specification.

              - `PdfA3a` The document supports the PDF/A-3a (Accessible) specification and contains tags
            that assistive technologies can use.

              - `PdfA3b` The document supports the PDF/A-3b (ISO 19005-3:2012) specification.

             Default: ApiPdfACompatibility.NONE.
        password_security_options (Union[Unset, None, ApiPdfPasswordSecurityOptions]):
        document_options (Union[Unset, None, ApiReportPdfPrintoutDocumentOptions]):
    """

    page_range: Union[Unset, None, str] = ""
    rasterization_resolution: Union[Unset, int] = 96
    convert_images_to_jpeg: Union[Unset, bool] = True
    show_print_dialog_on_open: Union[Unset, bool] = False
    never_embedded_fonts: Union[Unset, None, str] = ""
    export_editing_fields_to_acro_forms: Union[Unset, bool] = False
    image_quality: Union[Unset, ApiPdfImageQuality] = ApiPdfImageQuality.HIGHEST
    pdf_a_compatibility: Union[Unset, ApiPdfACompatibility] = ApiPdfACompatibility.NONE
    password_security_options: Union[Unset, None, "ApiPdfPasswordSecurityOptions"] = UNSET
    document_options: Union[Unset, None, "ApiReportPdfPrintoutDocumentOptions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        page_range = self.page_range
        rasterization_resolution = self.rasterization_resolution
        convert_images_to_jpeg = self.convert_images_to_jpeg
        show_print_dialog_on_open = self.show_print_dialog_on_open
        never_embedded_fonts = self.never_embedded_fonts
        export_editing_fields_to_acro_forms = self.export_editing_fields_to_acro_forms
        image_quality: Union[Unset, str] = UNSET
        if not isinstance(self.image_quality, Unset):
            image_quality = self.image_quality.value

        pdf_a_compatibility: Union[Unset, str] = UNSET
        if not isinstance(self.pdf_a_compatibility, Unset):
            pdf_a_compatibility = self.pdf_a_compatibility.value

        password_security_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.password_security_options, Unset):
            password_security_options = (
                self.password_security_options.to_dict() if self.password_security_options else None
            )

        document_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.document_options, Unset):
            document_options = self.document_options.to_dict() if self.document_options else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if page_range is not UNSET:
            field_dict["PageRange"] = page_range
        if rasterization_resolution is not UNSET:
            field_dict["RasterizationResolution"] = rasterization_resolution
        if convert_images_to_jpeg is not UNSET:
            field_dict["ConvertImagesToJpeg"] = convert_images_to_jpeg
        if show_print_dialog_on_open is not UNSET:
            field_dict["ShowPrintDialogOnOpen"] = show_print_dialog_on_open
        if never_embedded_fonts is not UNSET:
            field_dict["NeverEmbeddedFonts"] = never_embedded_fonts
        if export_editing_fields_to_acro_forms is not UNSET:
            field_dict["ExportEditingFieldsToAcroForms"] = export_editing_fields_to_acro_forms
        if image_quality is not UNSET:
            field_dict["ImageQuality"] = image_quality
        if pdf_a_compatibility is not UNSET:
            field_dict["PdfACompatibility"] = pdf_a_compatibility
        if password_security_options is not UNSET:
            field_dict["PasswordSecurityOptions"] = password_security_options
        if document_options is not UNSET:
            field_dict["DocumentOptions"] = document_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_pdf_password_security_options import ApiPdfPasswordSecurityOptions
        from ..models.api_report_pdf_printout_document_options import ApiReportPdfPrintoutDocumentOptions

        d = src_dict.copy()
        page_range = d.pop("PageRange", UNSET)

        rasterization_resolution = d.pop("RasterizationResolution", UNSET)

        convert_images_to_jpeg = d.pop("ConvertImagesToJpeg", UNSET)

        show_print_dialog_on_open = d.pop("ShowPrintDialogOnOpen", UNSET)

        never_embedded_fonts = d.pop("NeverEmbeddedFonts", UNSET)

        export_editing_fields_to_acro_forms = d.pop("ExportEditingFieldsToAcroForms", UNSET)

        _image_quality = d.pop("ImageQuality", UNSET)
        image_quality: Union[Unset, ApiPdfImageQuality]
        if isinstance(_image_quality, Unset):
            image_quality = UNSET
        else:
            image_quality = ApiPdfImageQuality(_image_quality)

        _pdf_a_compatibility = d.pop("PdfACompatibility", UNSET)
        pdf_a_compatibility: Union[Unset, ApiPdfACompatibility]
        if isinstance(_pdf_a_compatibility, Unset):
            pdf_a_compatibility = UNSET
        else:
            pdf_a_compatibility = ApiPdfACompatibility(_pdf_a_compatibility)

        _password_security_options = d.pop("PasswordSecurityOptions", UNSET)
        password_security_options: Union[Unset, None, ApiPdfPasswordSecurityOptions]
        if _password_security_options is None:
            password_security_options = None
        elif isinstance(_password_security_options, Unset):
            password_security_options = UNSET
        else:
            password_security_options = ApiPdfPasswordSecurityOptions.from_dict(_password_security_options)

        _document_options = d.pop("DocumentOptions", UNSET)
        document_options: Union[Unset, None, ApiReportPdfPrintoutDocumentOptions]
        if _document_options is None:
            document_options = None
        elif isinstance(_document_options, Unset):
            document_options = UNSET
        else:
            document_options = ApiReportPdfPrintoutDocumentOptions.from_dict(_document_options)

        api_report_pdf_printout_options = cls(
            page_range=page_range,
            rasterization_resolution=rasterization_resolution,
            convert_images_to_jpeg=convert_images_to_jpeg,
            show_print_dialog_on_open=show_print_dialog_on_open,
            never_embedded_fonts=never_embedded_fonts,
            export_editing_fields_to_acro_forms=export_editing_fields_to_acro_forms,
            image_quality=image_quality,
            pdf_a_compatibility=pdf_a_compatibility,
            password_security_options=password_security_options,
            document_options=document_options,
        )

        return api_report_pdf_printout_options
