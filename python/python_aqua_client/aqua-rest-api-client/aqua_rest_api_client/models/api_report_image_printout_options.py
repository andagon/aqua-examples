from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_report_printout_export_image_type import ApiReportPrintoutExportImageType
from ..models.api_report_printout_export_mode import ApiReportPrintoutExportMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportImagePrintoutOptions")


@attr.s(auto_attribs=True)
class ApiReportImagePrintoutOptions:
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
        resolution (Union[Unset, int]): The resolution (in DPI)  Default: 96.
        page_border_color (Union[Unset, None, str]): Color to be used (optional). HEX RGB string e.g. "0xffaabc"
        page_border_width (Union[Unset, int]): Width (in pixels) of page borders when a document is exported to HTML
            page-by-page. Default: 1.
        format_ (Union[Unset, ApiReportPrintoutExportImageType]):
            This enum has the following values:
              - `gif`
              - `jpeg`
              - `png`
             Default: ApiReportPrintoutExportImageType.PNG.
    """

    export_mode: Union[Unset, ApiReportPrintoutExportMode] = ApiReportPrintoutExportMode.SINGLEFILE
    page_range: Union[Unset, None, str] = ""
    resolution: Union[Unset, int] = 96
    page_border_color: Union[Unset, None, str] = UNSET
    page_border_width: Union[Unset, int] = 1
    format_: Union[Unset, ApiReportPrintoutExportImageType] = ApiReportPrintoutExportImageType.PNG

    def to_dict(self) -> Dict[str, Any]:
        export_mode: Union[Unset, str] = UNSET
        if not isinstance(self.export_mode, Unset):
            export_mode = self.export_mode.value

        page_range = self.page_range
        resolution = self.resolution
        page_border_color = self.page_border_color
        page_border_width = self.page_border_width
        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if export_mode is not UNSET:
            field_dict["ExportMode"] = export_mode
        if page_range is not UNSET:
            field_dict["PageRange"] = page_range
        if resolution is not UNSET:
            field_dict["Resolution"] = resolution
        if page_border_color is not UNSET:
            field_dict["PageBorderColor"] = page_border_color
        if page_border_width is not UNSET:
            field_dict["PageBorderWidth"] = page_border_width
        if format_ is not UNSET:
            field_dict["Format"] = format_

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

        resolution = d.pop("Resolution", UNSET)

        page_border_color = d.pop("PageBorderColor", UNSET)

        page_border_width = d.pop("PageBorderWidth", UNSET)

        _format_ = d.pop("Format", UNSET)
        format_: Union[Unset, ApiReportPrintoutExportImageType]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ApiReportPrintoutExportImageType(_format_)

        api_report_image_printout_options = cls(
            export_mode=export_mode,
            page_range=page_range,
            resolution=resolution,
            page_border_color=page_border_color,
            page_border_width=page_border_width,
            format_=format_,
        )

        return api_report_image_printout_options
