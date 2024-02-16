from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportDocxPrintoutDocumentOptions")


@attr.s(auto_attribs=True)
class ApiReportDocxPrintoutDocumentOptions:
    """
    Attributes:
        author (Union[Unset, None, str]): Author property of the resulting document Default: ''.
        title (Union[Unset, None, str]): Title property of the resulting document Default: ''.
        subject (Union[Unset, None, str]): Subject property of the resulting document Default: ''.
        keywords (Union[Unset, None, str]): Keywords property of the resulting document Default: ''.
        category (Union[Unset, None, str]): Category property of the resulting document Default: ''.
        comments (Union[Unset, None, str]): Comments property of the resulting document Default: ''.
    """

    author: Union[Unset, None, str] = ""
    title: Union[Unset, None, str] = ""
    subject: Union[Unset, None, str] = ""
    keywords: Union[Unset, None, str] = ""
    category: Union[Unset, None, str] = ""
    comments: Union[Unset, None, str] = ""

    def to_dict(self) -> Dict[str, Any]:
        author = self.author
        title = self.title
        subject = self.subject
        keywords = self.keywords
        category = self.category
        comments = self.comments

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if author is not UNSET:
            field_dict["Author"] = author
        if title is not UNSET:
            field_dict["Title"] = title
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if keywords is not UNSET:
            field_dict["Keywords"] = keywords
        if category is not UNSET:
            field_dict["Category"] = category
        if comments is not UNSET:
            field_dict["Comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        author = d.pop("Author", UNSET)

        title = d.pop("Title", UNSET)

        subject = d.pop("Subject", UNSET)

        keywords = d.pop("Keywords", UNSET)

        category = d.pop("Category", UNSET)

        comments = d.pop("Comments", UNSET)

        api_report_docx_printout_document_options = cls(
            author=author,
            title=title,
            subject=subject,
            keywords=keywords,
            category=category,
            comments=comments,
        )

        return api_report_docx_printout_document_options
