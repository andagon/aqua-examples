from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportXlPrintoutDocumentOptions")


@attr.s(auto_attribs=True)
class ApiReportXlPrintoutDocumentOptions:
    """
    Attributes:
        author (Union[Unset, None, str]): Author property of the resulting excel file Default: ''.
        application (Union[Unset, None, str]): Application property of the resulting excel file Default: ''.
        title (Union[Unset, None, str]): Title property of the resulting excel file Default: ''.
        subject (Union[Unset, None, str]): Subject property of the resulting excel file Default: ''.
        tags (Union[Unset, None, str]): Tags property of the resulting excel file Default: ''.
        category (Union[Unset, None, str]): Category property of the resulting excel file Default: ''.
        comments (Union[Unset, None, str]): Comments property of the resulting excel file Default: ''.
        company (Union[Unset, None, str]): Company property of the resulting excel file Default: ''.
    """

    author: Union[Unset, None, str] = ""
    application: Union[Unset, None, str] = ""
    title: Union[Unset, None, str] = ""
    subject: Union[Unset, None, str] = ""
    tags: Union[Unset, None, str] = ""
    category: Union[Unset, None, str] = ""
    comments: Union[Unset, None, str] = ""
    company: Union[Unset, None, str] = ""

    def to_dict(self) -> Dict[str, Any]:
        author = self.author
        application = self.application
        title = self.title
        subject = self.subject
        tags = self.tags
        category = self.category
        comments = self.comments
        company = self.company

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
        if tags is not UNSET:
            field_dict["Tags"] = tags
        if category is not UNSET:
            field_dict["Category"] = category
        if comments is not UNSET:
            field_dict["Comments"] = comments
        if company is not UNSET:
            field_dict["Company"] = company

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        author = d.pop("Author", UNSET)

        application = d.pop("Application", UNSET)

        title = d.pop("Title", UNSET)

        subject = d.pop("Subject", UNSET)

        tags = d.pop("Tags", UNSET)

        category = d.pop("Category", UNSET)

        comments = d.pop("Comments", UNSET)

        company = d.pop("Company", UNSET)

        api_report_xl_printout_document_options = cls(
            author=author,
            application=application,
            title=title,
            subject=subject,
            tags=tags,
            category=category,
            comments=comments,
            company=company,
        )

        return api_report_xl_printout_document_options
