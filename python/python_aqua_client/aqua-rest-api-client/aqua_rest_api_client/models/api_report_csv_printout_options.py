from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_report_printout_text_export_mode import ApiReportPrintoutTextExportMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportCsvPrintoutOptions")


@attr.s(auto_attribs=True)
class ApiReportCsvPrintoutOptions:
    """
    Attributes:
        encoding (Union[Unset, None, str]): Encoding to be used in printout  Default: 'utf-8'.
        text_export_mode (Union[Unset, ApiReportPrintoutTextExportMode]):
            This enum has the following values:
              - `Text`
              - `Value`
             Default: ApiReportPrintoutTextExportMode.TEXT.
        quote_strings (Union[Unset, bool]): If a string should be quoted when it contains the seperator Default: True.
        seperator (Union[Unset, None, str]): The character(s) used to separate elements Default: '\\t'.
        skip_empty_rows (Union[Unset, bool]): If empty rows should be skipped Default: True.
        skip_empty_columns (Union[Unset, bool]): If empty columns should be skipped Default: True.
    """

    encoding: Union[Unset, None, str] = "utf-8"
    text_export_mode: Union[Unset, ApiReportPrintoutTextExportMode] = ApiReportPrintoutTextExportMode.TEXT
    quote_strings: Union[Unset, bool] = True
    seperator: Union[Unset, None, str] = "\\t"
    skip_empty_rows: Union[Unset, bool] = True
    skip_empty_columns: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encoding = self.encoding
        text_export_mode: Union[Unset, str] = UNSET
        if not isinstance(self.text_export_mode, Unset):
            text_export_mode = self.text_export_mode.value

        quote_strings = self.quote_strings
        seperator = self.seperator
        skip_empty_rows = self.skip_empty_rows
        skip_empty_columns = self.skip_empty_columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encoding is not UNSET:
            field_dict["Encoding"] = encoding
        if text_export_mode is not UNSET:
            field_dict["TextExportMode"] = text_export_mode
        if quote_strings is not UNSET:
            field_dict["QuoteStrings"] = quote_strings
        if seperator is not UNSET:
            field_dict["Seperator"] = seperator
        if skip_empty_rows is not UNSET:
            field_dict["SkipEmptyRows"] = skip_empty_rows
        if skip_empty_columns is not UNSET:
            field_dict["SkipEmptyColumns"] = skip_empty_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encoding = d.pop("Encoding", UNSET)

        _text_export_mode = d.pop("TextExportMode", UNSET)
        text_export_mode: Union[Unset, ApiReportPrintoutTextExportMode]
        if isinstance(_text_export_mode, Unset):
            text_export_mode = UNSET
        else:
            text_export_mode = ApiReportPrintoutTextExportMode(_text_export_mode)

        quote_strings = d.pop("QuoteStrings", UNSET)

        seperator = d.pop("Seperator", UNSET)

        skip_empty_rows = d.pop("SkipEmptyRows", UNSET)

        skip_empty_columns = d.pop("SkipEmptyColumns", UNSET)

        api_report_csv_printout_options = cls(
            encoding=encoding,
            text_export_mode=text_export_mode,
            quote_strings=quote_strings,
            seperator=seperator,
            skip_empty_rows=skip_empty_rows,
            skip_empty_columns=skip_empty_columns,
        )

        api_report_csv_printout_options.additional_properties = d
        return api_report_csv_printout_options

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
