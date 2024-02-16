from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiUploadedFile")


@attr.s(auto_attribs=True)
class ApiUploadedFile:
    """Represents a file upload to the REST API. You do not need to provide a JSON
    structure. Instead just send the content of the file you would like to upload.
    The content can be sent directly as the request body or inside a multipart form
    data.

        Attributes:
            content (Union[Unset, None, str]): The content of the uploaded file. The content can be sent either directly
                as the request body or in a multipart form .
            name (Union[Unset, None, str]): When the file is uploaded using a multipart form, the file name is taken from
                the ContentDisposition header. Otherwise, the name is null. The name must include the file extension otherwise
                the request will be rejected.
    """

    content: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if content is not UNSET:
            field_dict["Content"] = content
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("Content", UNSET)

        name = d.pop("Name", UNSET)

        api_uploaded_file = cls(
            content=content,
            name=name,
        )

        return api_uploaded_file
