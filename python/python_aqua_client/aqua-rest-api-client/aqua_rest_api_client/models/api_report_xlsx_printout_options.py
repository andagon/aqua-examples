from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_report_printout_default_boolean import ApiReportPrintoutDefaultBoolean
from ..models.api_report_printout_export_mode import ApiReportPrintoutExportMode
from ..models.api_report_printout_text_export_mode import ApiReportPrintoutTextExportMode
from ..models.api_xls_ignore_errors import ApiXlsIgnoreErrors
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_report_xl_printout_document_options import ApiReportXlPrintoutDocumentOptions
    from ..models.api_report_xl_printout_encryption_options import ApiReportXlPrintoutEncryptionOptions


T = TypeVar("T", bound="ApiReportXlsxPrintoutOptions")


@attr.s(auto_attribs=True)
class ApiReportXlsxPrintoutOptions:
    """
    Attributes:
        export_mode (Union[Unset, ApiReportPrintoutExportMode]):
            This enum has the following values:
              - `SingleFile`
              - `SingleFilePageByPage`
             Default: ApiReportPrintoutExportMode.SINGLEFILE.
        page_range (Union[Unset, None, str]): The page range to be exported. Ranges are comma separated. e.g.
            “1,4,7-10”.
            Invalid page numbers are ignored, if all page numbers are invalid, all pages are exported. Default: ''.
        rasterization_resolution (Union[Unset, int]): The resolution (in DPI) used to rasterize vector images. Default:
            96.
        text_export_mode (Union[Unset, ApiReportPrintoutTextExportMode]):
            This enum has the following values:
              - `Text`
              - `Value`
             Default: ApiReportPrintoutTextExportMode.VALUE.
        export_hyperlinks (Union[Unset, bool]): Whether hyperlinks should be exported Default: True.
        raw_data_mode (Union[Unset, bool]): Enables the mode that produces simple tabular data without graphic elements,
            style and appearance settings.
        sheet_name (Union[Unset, None, str]): Name of the sheet in the created excel document Default: 'Sheet'.
        show_grid_lines (Union[Unset, bool]): Whether worksheet gridlines are visible
        rasterize_images (Union[Unset, bool]): If vector images should be rasterized to the corresponding document
            format. Default: True.
        fit_to_printed_page_width (Union[Unset, bool]): If the output document should be fit to the page width when
            printed.
        fit_to_printed_page_height (Union[Unset, bool]): If the output document should be fit to the page height when
            printed.
        ignore_errors (Union[Unset, ApiXlsIgnoreErrors]):
            This enum has the following values:
              - `None` No document errors are ignored in a resulting Excel file.
              - `NumberStoredAsText` Values stored as text are ignored in a resulting Excel file.
             Default: ApiXlsIgnoreErrors.NONE.
        right_to_left_document (Union[Unset, ApiReportPrintoutDefaultBoolean]):
            This enum has the following values:
              - `Default`
              - `False`
              - `True`
             Default: ApiReportPrintoutDefaultBoolean.DEFAULT.
        encryption_options (Union[Unset, None, ApiReportXlPrintoutEncryptionOptions]):
        document_options (Union[Unset, None, ApiReportXlPrintoutDocumentOptions]):
    """

    export_mode: Union[Unset, ApiReportPrintoutExportMode] = ApiReportPrintoutExportMode.SINGLEFILE
    page_range: Union[Unset, None, str] = ""
    rasterization_resolution: Union[Unset, int] = 96
    text_export_mode: Union[Unset, ApiReportPrintoutTextExportMode] = ApiReportPrintoutTextExportMode.VALUE
    export_hyperlinks: Union[Unset, bool] = True
    raw_data_mode: Union[Unset, bool] = False
    sheet_name: Union[Unset, None, str] = "Sheet"
    show_grid_lines: Union[Unset, bool] = False
    rasterize_images: Union[Unset, bool] = True
    fit_to_printed_page_width: Union[Unset, bool] = False
    fit_to_printed_page_height: Union[Unset, bool] = False
    ignore_errors: Union[Unset, ApiXlsIgnoreErrors] = ApiXlsIgnoreErrors.NONE
    right_to_left_document: Union[Unset, ApiReportPrintoutDefaultBoolean] = ApiReportPrintoutDefaultBoolean.DEFAULT
    encryption_options: Union[Unset, None, "ApiReportXlPrintoutEncryptionOptions"] = UNSET
    document_options: Union[Unset, None, "ApiReportXlPrintoutDocumentOptions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        export_mode: Union[Unset, str] = UNSET
        if not isinstance(self.export_mode, Unset):
            export_mode = self.export_mode.value

        page_range = self.page_range
        rasterization_resolution = self.rasterization_resolution
        text_export_mode: Union[Unset, str] = UNSET
        if not isinstance(self.text_export_mode, Unset):
            text_export_mode = self.text_export_mode.value

        export_hyperlinks = self.export_hyperlinks
        raw_data_mode = self.raw_data_mode
        sheet_name = self.sheet_name
        show_grid_lines = self.show_grid_lines
        rasterize_images = self.rasterize_images
        fit_to_printed_page_width = self.fit_to_printed_page_width
        fit_to_printed_page_height = self.fit_to_printed_page_height
        ignore_errors: Union[Unset, str] = UNSET
        if not isinstance(self.ignore_errors, Unset):
            ignore_errors = self.ignore_errors.value

        right_to_left_document: Union[Unset, str] = UNSET
        if not isinstance(self.right_to_left_document, Unset):
            right_to_left_document = self.right_to_left_document.value

        encryption_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.encryption_options, Unset):
            encryption_options = self.encryption_options.to_dict() if self.encryption_options else None

        document_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.document_options, Unset):
            document_options = self.document_options.to_dict() if self.document_options else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if export_mode is not UNSET:
            field_dict["ExportMode"] = export_mode
        if page_range is not UNSET:
            field_dict["PageRange"] = page_range
        if rasterization_resolution is not UNSET:
            field_dict["RasterizationResolution"] = rasterization_resolution
        if text_export_mode is not UNSET:
            field_dict["TextExportMode"] = text_export_mode
        if export_hyperlinks is not UNSET:
            field_dict["ExportHyperlinks"] = export_hyperlinks
        if raw_data_mode is not UNSET:
            field_dict["RawDataMode"] = raw_data_mode
        if sheet_name is not UNSET:
            field_dict["SheetName"] = sheet_name
        if show_grid_lines is not UNSET:
            field_dict["ShowGridLines"] = show_grid_lines
        if rasterize_images is not UNSET:
            field_dict["RasterizeImages"] = rasterize_images
        if fit_to_printed_page_width is not UNSET:
            field_dict["FitToPrintedPageWidth"] = fit_to_printed_page_width
        if fit_to_printed_page_height is not UNSET:
            field_dict["FitToPrintedPageHeight"] = fit_to_printed_page_height
        if ignore_errors is not UNSET:
            field_dict["IgnoreErrors"] = ignore_errors
        if right_to_left_document is not UNSET:
            field_dict["RightToLeftDocument"] = right_to_left_document
        if encryption_options is not UNSET:
            field_dict["EncryptionOptions"] = encryption_options
        if document_options is not UNSET:
            field_dict["DocumentOptions"] = document_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_report_xl_printout_document_options import ApiReportXlPrintoutDocumentOptions
        from ..models.api_report_xl_printout_encryption_options import ApiReportXlPrintoutEncryptionOptions

        d = src_dict.copy()
        _export_mode = d.pop("ExportMode", UNSET)
        export_mode: Union[Unset, ApiReportPrintoutExportMode]
        if isinstance(_export_mode, Unset):
            export_mode = UNSET
        else:
            export_mode = ApiReportPrintoutExportMode(_export_mode)

        page_range = d.pop("PageRange", UNSET)

        rasterization_resolution = d.pop("RasterizationResolution", UNSET)

        _text_export_mode = d.pop("TextExportMode", UNSET)
        text_export_mode: Union[Unset, ApiReportPrintoutTextExportMode]
        if isinstance(_text_export_mode, Unset):
            text_export_mode = UNSET
        else:
            text_export_mode = ApiReportPrintoutTextExportMode(_text_export_mode)

        export_hyperlinks = d.pop("ExportHyperlinks", UNSET)

        raw_data_mode = d.pop("RawDataMode", UNSET)

        sheet_name = d.pop("SheetName", UNSET)

        show_grid_lines = d.pop("ShowGridLines", UNSET)

        rasterize_images = d.pop("RasterizeImages", UNSET)

        fit_to_printed_page_width = d.pop("FitToPrintedPageWidth", UNSET)

        fit_to_printed_page_height = d.pop("FitToPrintedPageHeight", UNSET)

        _ignore_errors = d.pop("IgnoreErrors", UNSET)
        ignore_errors: Union[Unset, ApiXlsIgnoreErrors]
        if isinstance(_ignore_errors, Unset):
            ignore_errors = UNSET
        else:
            ignore_errors = ApiXlsIgnoreErrors(_ignore_errors)

        _right_to_left_document = d.pop("RightToLeftDocument", UNSET)
        right_to_left_document: Union[Unset, ApiReportPrintoutDefaultBoolean]
        if isinstance(_right_to_left_document, Unset):
            right_to_left_document = UNSET
        else:
            right_to_left_document = ApiReportPrintoutDefaultBoolean(_right_to_left_document)

        _encryption_options = d.pop("EncryptionOptions", UNSET)
        encryption_options: Union[Unset, None, ApiReportXlPrintoutEncryptionOptions]
        if _encryption_options is None:
            encryption_options = None
        elif isinstance(_encryption_options, Unset):
            encryption_options = UNSET
        else:
            encryption_options = ApiReportXlPrintoutEncryptionOptions.from_dict(_encryption_options)

        _document_options = d.pop("DocumentOptions", UNSET)
        document_options: Union[Unset, None, ApiReportXlPrintoutDocumentOptions]
        if _document_options is None:
            document_options = None
        elif isinstance(_document_options, Unset):
            document_options = UNSET
        else:
            document_options = ApiReportXlPrintoutDocumentOptions.from_dict(_document_options)

        api_report_xlsx_printout_options = cls(
            export_mode=export_mode,
            page_range=page_range,
            rasterization_resolution=rasterization_resolution,
            text_export_mode=text_export_mode,
            export_hyperlinks=export_hyperlinks,
            raw_data_mode=raw_data_mode,
            sheet_name=sheet_name,
            show_grid_lines=show_grid_lines,
            rasterize_images=rasterize_images,
            fit_to_printed_page_width=fit_to_printed_page_width,
            fit_to_printed_page_height=fit_to_printed_page_height,
            ignore_errors=ignore_errors,
            right_to_left_document=right_to_left_document,
            encryption_options=encryption_options,
            document_options=document_options,
        )

        return api_report_xlsx_printout_options
