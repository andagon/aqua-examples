from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiImageUploadInfo")


@attr.s(auto_attribs=True)
class ApiImageUploadInfo:
    """Contains metadata for an uploaded image.

    Attributes:
        checksum (Union[Unset, None, str]): The checksum of the image
        url (Union[Unset, None, str]): The absolute url which can be used to reference the image
    """

    checksum: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        checksum = self.checksum
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if checksum is not UNSET:
            field_dict["Checksum"] = checksum
        if url is not UNSET:
            field_dict["Url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        checksum = d.pop("Checksum", UNSET)

        url = d.pop("Url", UNSET)

        api_image_upload_info = cls(
            checksum=checksum,
            url=url,
        )

        return api_image_upload_info
