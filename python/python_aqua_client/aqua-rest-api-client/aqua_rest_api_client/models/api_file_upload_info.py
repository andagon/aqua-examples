from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFileUploadInfo")


@attr.s(auto_attribs=True)
class ApiFileUploadInfo:
    """Contains metadata for an uploaded image.

    Attributes:
        guid (Union[Unset, str]): The GUID which identifies this file upload.
        url (Union[Unset, None, str]): The URL which allows you to download the temporarily uploaded file again.
    """

    guid: Union[Unset, str] = UNSET
    url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if url is not UNSET:
            field_dict["Url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        url = d.pop("Url", UNSET)

        api_file_upload_info = cls(
            guid=guid,
            url=url,
        )

        return api_file_upload_info
