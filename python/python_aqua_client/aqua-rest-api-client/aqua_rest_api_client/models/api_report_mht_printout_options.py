from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_report_printout_export_mode import ApiReportPrintoutExportMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportMhtPrintoutOptions")


@attr.s(auto_attribs=True)
class ApiReportMhtPrintoutOptions:
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
        page_border_color (Union[Unset, None, str]): Color to be used (optional). HEX RGB string e.g. "0xffaabc"
        page_border_width (Union[Unset, int]): Width (in pixels) of page borders when a document is exported to HTML
            page-by-page. Default: 1.
        title (Union[Unset, None, str]): Title of the created HTML file Default: 'Document'.
        table_layout (Union[Unset, bool]): Determines whether to use the table or non-table layout in the resulting HTML
            file. Default: True.
        use_h_ref_hyperlinks (Union[Unset, bool]): Specifies whether or not the document navigation is implemented by
            using scripts.
        allow_jsur_ls (Union[Unset, bool]): Specifies whether the JavaScript code can be placed in URLs in the resulting
            HTML document.
        remove_secondary_symbols (Union[Unset, bool]): Specifies Gets or sets a value indicating whether secondary
            symbols should be removed from the resulting HTML file, to reduce its size.
        export_watermarks (Union[Unset, bool]): Specifies whether to export watermarks to HTML along with the rest of
            the document content. Default: True.
        character_set (Union[Unset, None, str]): A String﻿ representing the encoding name set in the HTML file (e.g.
            "utf-8"). Default: 'utf-8'.
    """

    export_mode: Union[Unset, ApiReportPrintoutExportMode] = ApiReportPrintoutExportMode.SINGLEFILE
    page_range: Union[Unset, None, str] = ""
    rasterization_resolution: Union[Unset, int] = 96
    page_border_color: Union[Unset, None, str] = UNSET
    page_border_width: Union[Unset, int] = 1
    title: Union[Unset, None, str] = "Document"
    table_layout: Union[Unset, bool] = True
    use_h_ref_hyperlinks: Union[Unset, bool] = False
    allow_jsur_ls: Union[Unset, bool] = False
    remove_secondary_symbols: Union[Unset, bool] = False
    export_watermarks: Union[Unset, bool] = True
    character_set: Union[Unset, None, str] = "utf-8"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_mode: Union[Unset, str] = UNSET
        if not isinstance(self.export_mode, Unset):
            export_mode = self.export_mode.value

        page_range = self.page_range
        rasterization_resolution = self.rasterization_resolution
        page_border_color = self.page_border_color
        page_border_width = self.page_border_width
        title = self.title
        table_layout = self.table_layout
        use_h_ref_hyperlinks = self.use_h_ref_hyperlinks
        allow_jsur_ls = self.allow_jsur_ls
        remove_secondary_symbols = self.remove_secondary_symbols
        export_watermarks = self.export_watermarks
        character_set = self.character_set

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_mode is not UNSET:
            field_dict["ExportMode"] = export_mode
        if page_range is not UNSET:
            field_dict["PageRange"] = page_range
        if rasterization_resolution is not UNSET:
            field_dict["RasterizationResolution"] = rasterization_resolution
        if page_border_color is not UNSET:
            field_dict["PageBorderColor"] = page_border_color
        if page_border_width is not UNSET:
            field_dict["PageBorderWidth"] = page_border_width
        if title is not UNSET:
            field_dict["Title"] = title
        if table_layout is not UNSET:
            field_dict["TableLayout"] = table_layout
        if use_h_ref_hyperlinks is not UNSET:
            field_dict["UseHRefHyperlinks"] = use_h_ref_hyperlinks
        if allow_jsur_ls is not UNSET:
            field_dict["AllowJSURLs"] = allow_jsur_ls
        if remove_secondary_symbols is not UNSET:
            field_dict["RemoveSecondarySymbols"] = remove_secondary_symbols
        if export_watermarks is not UNSET:
            field_dict["ExportWatermarks"] = export_watermarks
        if character_set is not UNSET:
            field_dict["CharacterSet"] = character_set

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

        page_border_color = d.pop("PageBorderColor", UNSET)

        page_border_width = d.pop("PageBorderWidth", UNSET)

        title = d.pop("Title", UNSET)

        table_layout = d.pop("TableLayout", UNSET)

        use_h_ref_hyperlinks = d.pop("UseHRefHyperlinks", UNSET)

        allow_jsur_ls = d.pop("AllowJSURLs", UNSET)

        remove_secondary_symbols = d.pop("RemoveSecondarySymbols", UNSET)

        export_watermarks = d.pop("ExportWatermarks", UNSET)

        character_set = d.pop("CharacterSet", UNSET)

        api_report_mht_printout_options = cls(
            export_mode=export_mode,
            page_range=page_range,
            rasterization_resolution=rasterization_resolution,
            page_border_color=page_border_color,
            page_border_width=page_border_width,
            title=title,
            table_layout=table_layout,
            use_h_ref_hyperlinks=use_h_ref_hyperlinks,
            allow_jsur_ls=allow_jsur_ls,
            remove_secondary_symbols=remove_secondary_symbols,
            export_watermarks=export_watermarks,
            character_set=character_set,
        )

        api_report_mht_printout_options.additional_properties = d
        return api_report_mht_printout_options

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
