from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_report_printout_export_mode import ApiReportPrintoutExportMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportRtfPrintoutOptions")


@attr.s(auto_attribs=True)
class ApiReportRtfPrintoutOptions:
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
    """

    export_mode: Union[Unset, ApiReportPrintoutExportMode] = ApiReportPrintoutExportMode.SINGLEFILE
    page_range: Union[Unset, None, str] = ""
    rasterization_resolution: Union[Unset, int] = 96
    export_page_breaks: Union[Unset, bool] = True
    export_watermarks: Union[Unset, bool] = True

    def to_dict(self) -> Dict[str, Any]:
        export_mode: Union[Unset, str] = UNSET
        if not isinstance(self.export_mode, Unset):
            export_mode = self.export_mode.value

        page_range = self.page_range
        rasterization_resolution = self.rasterization_resolution
        export_page_breaks = self.export_page_breaks
        export_watermarks = self.export_watermarks

        field_dict: Dict[str, Any] = {}
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        api_report_rtf_printout_options = cls(
            export_mode=export_mode,
            page_range=page_range,
            rasterization_resolution=rasterization_resolution,
            export_page_breaks=export_page_breaks,
            export_watermarks=export_watermarks,
        )

        return api_report_rtf_printout_options
