from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAutomationAttachedScriptFileNew")


@attr.s(auto_attribs=True)
class ApiAutomationAttachedScriptFileNew:
    """An attachment which should be created as part of a list of attachment
    changes for a certain item. The file attach must have been uploaded to
    /File beforehand.The InsertAt property indicates where on the list
    the new attachment should be located.

        Attributes:
            guid (Union[Unset, str]): The ID of the temporary upload which should be added as the new
                attachment. The temporary upload can be created with the
                [UploadFile](#operation/File_UploadFile)
                endpoint.
            insert_at (Union[Unset, int]): Location where to insert the new file.
    """

    guid: Union[Unset, str] = UNSET
    insert_at: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        insert_at = self.insert_at

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if insert_at is not UNSET:
            field_dict["InsertAt"] = insert_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        insert_at = d.pop("InsertAt", UNSET)

        api_automation_attached_script_file_new = cls(
            guid=guid,
            insert_at=insert_at,
        )

        return api_automation_attached_script_file_new
