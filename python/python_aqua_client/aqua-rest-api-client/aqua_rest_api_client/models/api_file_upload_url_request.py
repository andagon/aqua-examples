from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiFileUploadUrlRequest")


@attr.s(auto_attribs=True)
class ApiFileUploadUrlRequest:
    """Contains the necessary information for creating an upload URL.

    Attributes:
        file_name (str): The name of the file for which the upload URL is requested.
        file_size (int): The size (in bytes) of the file for which the upload URL is requested.
    """

    file_name: str
    file_size: int

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name
        file_size = self.file_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "FileName": file_name,
                "FileSize": file_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_name = d.pop("FileName")

        file_size = d.pop("FileSize")

        api_file_upload_url_request = cls(
            file_name=file_name,
            file_size=file_size,
        )

        return api_file_upload_url_request
