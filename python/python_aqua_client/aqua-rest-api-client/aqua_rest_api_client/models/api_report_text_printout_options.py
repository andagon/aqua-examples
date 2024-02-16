from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_report_printout_text_export_mode import ApiReportPrintoutTextExportMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportTextPrintoutOptions")


@attr.s(auto_attribs=True)
class ApiReportTextPrintoutOptions:
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
    """

    encoding: Union[Unset, None, str] = "utf-8"
    text_export_mode: Union[Unset, ApiReportPrintoutTextExportMode] = ApiReportPrintoutTextExportMode.TEXT
    quote_strings: Union[Unset, bool] = True
    seperator: Union[Unset, None, str] = "\\t"

    def to_dict(self) -> Dict[str, Any]:
        encoding = self.encoding
        text_export_mode: Union[Unset, str] = UNSET
        if not isinstance(self.text_export_mode, Unset):
            text_export_mode = self.text_export_mode.value

        quote_strings = self.quote_strings
        seperator = self.seperator

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if encoding is not UNSET:
            field_dict["Encoding"] = encoding
        if text_export_mode is not UNSET:
            field_dict["TextExportMode"] = text_export_mode
        if quote_strings is not UNSET:
            field_dict["QuoteStrings"] = quote_strings
        if seperator is not UNSET:
            field_dict["Seperator"] = seperator

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

        api_report_text_printout_options = cls(
            encoding=encoding,
            text_export_mode=text_export_mode,
            quote_strings=quote_strings,
            seperator=seperator,
        )

        return api_report_text_printout_options
