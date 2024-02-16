from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAttachmentNew")


@attr.s(auto_attribs=True)
class ApiAttachmentNew:
    """An attachment which should be created as part of a list of attachment
    changes for a certain item. The file attach must have been uploaded to
    /File beforehand.

        Attributes:
            guid (Union[Unset, str]): The GUID which uniquely identifies the uploaded file.
                The file should be uploaded to the endpoint
                [UploadFile](#operation/File_UploadFile)
                or
                [UploadFileWithGuid](#operation/File_UploadFileWithGuid)
                first.
    """

    guid: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        api_attachment_new = cls(
            guid=guid,
        )

        return api_attachment_new
