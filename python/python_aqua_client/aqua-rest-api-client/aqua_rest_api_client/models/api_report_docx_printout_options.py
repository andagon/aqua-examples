from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_report_printout_export_mode import ApiReportPrintoutExportMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_report_docx_printout_document_options import ApiReportDocxPrintoutDocumentOptions


T = TypeVar("T", bound="ApiReportDocxPrintoutOptions")


@attr.s(auto_attribs=True)
class ApiReportDocxPrintoutOptions:
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
        export_page_breaks (Union[Unset, bool]): True if pagebreaks should be included in the export Default: True.
        export_watermarks (Union[Unset, bool]): True if watermarks should be included in the export Default: True.
        table_layout (Union[Unset, bool]): Whether to use the table or frame layout in the resulting DOCX file.
        document_options (Union[Unset, None, ApiReportDocxPrintoutDocumentOptions]):
        rasterize_images (Union[Unset, bool]): If vector images should be rasterized to the corresponding document
            format. Default: True.
        keep_row_height (Union[Unset, bool]): Whether the height of table rows in a resulting document should have fixed
            values, or adding a new line of text to a cell’s content should increase the row height.
    """

    export_mode: Union[Unset, ApiReportPrintoutExportMode] = ApiReportPrintoutExportMode.SINGLEFILE
    page_range: Union[Unset, None, str] = ""
    rasterization_resolution: Union[Unset, int] = 96
    export_page_breaks: Union[Unset, bool] = True
    export_watermarks: Union[Unset, bool] = True
    table_layout: Union[Unset, bool] = False
    document_options: Union[Unset, None, "ApiReportDocxPrintoutDocumentOptions"] = UNSET
    rasterize_images: Union[Unset, bool] = True
    keep_row_height: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_mode: Union[Unset, str] = UNSET
        if not isinstance(self.export_mode, Unset):
            export_mode = self.export_mode.value

        page_range = self.page_range
        rasterization_resolution = self.rasterization_resolution
        export_page_breaks = self.export_page_breaks
        export_watermarks = self.export_watermarks
        table_layout = self.table_layout
        document_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.document_options, Unset):
            document_options = self.document_options.to_dict() if self.document_options else None

        rasterize_images = self.rasterize_images
        keep_row_height = self.keep_row_height

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_mode is not UNSET:
            field_dict["ExportMode"] = export_mode
        if page_range is not UNSET:
            field_dict["PageRange"] = page_range
        if rasterization_resolution is not UNSET:
            field_dict["RasterizationResolution"] = rasterization_resolution
        if export_page_breaks is not UNSET:
            field_dict["ExportPageBreaks"] = export_page_breaks
        if export_watermarks is not UNSET:
            field_dict["ExportWatermarks"] = export_watermarks
        if table_layout is not UNSET:
            field_dict["TableLayout"] = table_layout
        if document_options is not UNSET:
            field_dict["DocumentOptions"] = document_options
        if rasterize_images is not UNSET:
            field_dict["RasterizeImages"] = rasterize_images
        if keep_row_height is not UNSET:
            field_dict["KeepRowHeight"] = keep_row_height

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_report_docx_printout_document_options import ApiReportDocxPrintoutDocumentOptions

        d = src_dict.copy()
        _export_mode = d.pop("ExportMode", UNSET)
        export_mode: Union[Unset, ApiReportPrintoutExportMode]
        if isinstance(_export_mode, Unset):
            export_mode = UNSET
        else:
            export_mode = ApiReportPrintoutExportMode(_export_mode)

        page_range = d.pop("PageRange", UNSET)

        rasterization_resolution = d.pop("RasterizationResolution", UNSET)

        export_page_breaks = d.pop("ExportPageBreaks", UNSET)

        export_watermarks = d.pop("ExportWatermarks", UNSET)

        table_layout = d.pop("TableLayout", UNSET)

        _document_options = d.pop("DocumentOptions", UNSET)
        document_options: Union[Unset, None, ApiReportDocxPrintoutDocumentOptions]
        if _document_options is None:
            document_options = None
        elif isinstance(_document_options, Unset):
            document_options = UNSET
        else:
            document_options = ApiReportDocxPrintoutDocumentOptions.from_dict(_document_options)

        rasterize_images = d.pop("RasterizeImages", UNSET)

        keep_row_height = d.pop("KeepRowHeight", UNSET)

        api_report_docx_printout_options = cls(
            export_mode=export_mode,
            page_range=page_range,
            rasterization_resolution=rasterization_resolution,
            export_page_breaks=export_page_breaks,
            export_watermarks=export_watermarks,
            table_layout=table_layout,
            document_options=document_options,
            rasterize_images=rasterize_images,
            keep_row_height=keep_row_height,
        )

        api_report_docx_printout_options.additional_properties = d
        return api_report_docx_printout_options

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
