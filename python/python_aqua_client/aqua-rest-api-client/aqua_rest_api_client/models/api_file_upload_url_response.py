from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_file_upload_url_type import ApiFileUploadUrlType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFileUploadUrlResponse")


@attr.s(auto_attribs=True)
class ApiFileUploadUrlResponse:
    """Contains a file upload URL and some corresponding metadata.

    Attributes:
        guid (Union[Unset, str]): The Guid which uniquely identifies the file upload.
        url_type (Union[Unset, ApiFileUploadUrlType]): The type of the upload URL.
            This enum has the following values:
              - `Aqua` The upload URL points to aqua itself. The upload should be
            performed with a PUT request.
              - `AzureBlobStorage` The upload URL points to Azure Blob Storage. The upload should be
            performed with a PUT request.The upload must contain the following
            custom header `x-ms-blob-type: BlockBlob`.
        upload_url (Union[Unset, None, str]): The URL to which the content of the file should be uploaded.
            This URL is only valid for a limited time.
        download_url (Union[Unset, None, str]): This URL can be used to download the content again after
            it was uploaded. This URL is only valid for a limited time.
    """

    guid: Union[Unset, str] = UNSET
    url_type: Union[Unset, ApiFileUploadUrlType] = UNSET
    upload_url: Union[Unset, None, str] = UNSET
    download_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        url_type: Union[Unset, str] = UNSET
        if not isinstance(self.url_type, Unset):
            url_type = self.url_type.value

        upload_url = self.upload_url
        download_url = self.download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if url_type is not UNSET:
            field_dict["UrlType"] = url_type
        if upload_url is not UNSET:
            field_dict["UploadUrl"] = upload_url
        if download_url is not UNSET:
            field_dict["DownloadUrl"] = download_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        _url_type = d.pop("UrlType", UNSET)
        url_type: Union[Unset, ApiFileUploadUrlType]
        if isinstance(_url_type, Unset):
            url_type = UNSET
        else:
            url_type = ApiFileUploadUrlType(_url_type)

        upload_url = d.pop("UploadUrl", UNSET)

        download_url = d.pop("DownloadUrl", UNSET)

        api_file_upload_url_response = cls(
            guid=guid,
            url_type=url_type,
            upload_url=upload_url,
            download_url=download_url,
        )

        return api_file_upload_url_response
