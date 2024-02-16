from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportPdfPrintoutDocumentOptions")


@attr.s(auto_attribs=True)
class ApiReportPdfPrintoutDocumentOptions:
    """
    Attributes:
        author (Union[Unset, None, str]): Author property of the resulting document Default: ''.
        application (Union[Unset, None, str]): Application property of the resulting document Default: ''.
        title (Union[Unset, None, str]): Title property of the resulting document Default: ''.
        subject (Union[Unset, None, str]): Subject property of the resulting document Default: ''.
        keywords (Union[Unset, None, str]): Keywords property of the resulting document Default: ''.
    """

    author: Union[Unset, None, str] = ""
    application: Union[Unset, None, str] = ""
    title: Union[Unset, None, str] = ""
    subject: Union[Unset, None, str] = ""
    keywords: Union[Unset, None, str] = ""

    def to_dict(self) -> Dict[str, Any]:
        author = self.author
        application = self.application
        title = self.title
        subject = self.subject
        keywords = self.keywords

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if author is not UNSET:
            field_dict["Author"] = author
        if application is not UNSET:
            field_dict["Application"] = application
        if title is not UNSET:
            field_dict["Title"] = title
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if keywords is not UNSET:
            field_dict["Keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        author = d.pop("Author", UNSET)

        application = d.pop("Application", UNSET)

        title = d.pop("Title", UNSET)

        subject = d.pop("Subject", UNSET)

        keywords = d.pop("Keywords", UNSET)

        api_report_pdf_printout_document_options = cls(
            author=author,
            application=application,
            title=title,
            subject=subject,
            keywords=keywords,
        )

        return api_report_pdf_printout_document_options
