from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiImageInfo")


@attr.s(auto_attribs=True)
class ApiImageInfo:
    """The metadata of an image. The content of the image is not included.

    Attributes:
        id (Union[Unset, int]): The id of the image
        checksum (Union[Unset, None, str]): The checksum of the image's content
        file_extension (Union[Unset, None, str]): The file extension of the image. Can be used to identify the type
            of image. The extension .rtf is used for images included
            in rich text.
    """

    id: Union[Unset, int] = UNSET
    checksum: Union[Unset, None, str] = UNSET
    file_extension: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        checksum = self.checksum
        file_extension = self.file_extension

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if checksum is not UNSET:
            field_dict["Checksum"] = checksum
        if file_extension is not UNSET:
            field_dict["FileExtension"] = file_extension

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        checksum = d.pop("Checksum", UNSET)

        file_extension = d.pop("FileExtension", UNSET)

        api_image_info = cls(
            id=id,
            checksum=checksum,
            file_extension=file_extension,
        )

        return api_image_info
