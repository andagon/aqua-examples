from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAutomationAttachedScriptFileInfo")


@attr.s(auto_attribs=True)
class ApiAutomationAttachedScriptFileInfo:
    """Meta information for an attached file (used in some types of automation e.g. in PowerShell)
    Contains e.g. file name and size. This structure does not contain the content of
    the attachment which must be requested separately.

        Attributes:
            id (Union[Unset, int]): The id of the attachment.
            filename (Union[Unset, None, str]): The full file name of the attachment including the file extension.
            file_extension (Union[Unset, None, str]): The file extension of the attachment.
            size (Union[Unset, int]): The size of the attachment in bytes.
            view_url (Union[Unset, None, str]): The url where the content of the attachment is located. For this url,
                the API will force browsers to display the content by setting the
                content-disposition header to inline.
            download_url (Union[Unset, None, str]): The url where the content of the attachment is located. For this url,
                the API will force browsers to download the file by setting the
                content-disposition header to attachment.
    """

    id: Union[Unset, int] = UNSET
    filename: Union[Unset, None, str] = UNSET
    file_extension: Union[Unset, None, str] = UNSET
    size: Union[Unset, int] = UNSET
    view_url: Union[Unset, None, str] = UNSET
    download_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        filename = self.filename
        file_extension = self.file_extension
        size = self.size
        view_url = self.view_url
        download_url = self.download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if filename is not UNSET:
            field_dict["Filename"] = filename
        if file_extension is not UNSET:
            field_dict["FileExtension"] = file_extension
        if size is not UNSET:
            field_dict["Size"] = size
        if view_url is not UNSET:
            field_dict["ViewUrl"] = view_url
        if download_url is not UNSET:
            field_dict["DownloadUrl"] = download_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        filename = d.pop("Filename", UNSET)

        file_extension = d.pop("FileExtension", UNSET)

        size = d.pop("Size", UNSET)

        view_url = d.pop("ViewUrl", UNSET)

        download_url = d.pop("DownloadUrl", UNSET)

        api_automation_attached_script_file_info = cls(
            id=id,
            filename=filename,
            file_extension=file_extension,
            size=size,
            view_url=view_url,
            download_url=download_url,
        )

        return api_automation_attached_script_file_info
