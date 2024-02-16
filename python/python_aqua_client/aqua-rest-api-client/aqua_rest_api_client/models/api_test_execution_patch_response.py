from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_test_execution_modifying_status import ApiTestExecutionModifyingStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestExecutionPatchResponse")


@attr.s(auto_attribs=True)
class ApiTestExecutionPatchResponse:
    """
    Attributes:
        guid (Union[Unset, None, str]): The guid of long running task.
        modifying_status (Union[Unset, ApiTestExecutionModifyingStatus]): Represents current modifying status of an test
            execution.
            This enum has the following values:
              - `Executing`
              - `Finished`
    """

    guid: Union[Unset, None, str] = UNSET
    modifying_status: Union[Unset, ApiTestExecutionModifyingStatus] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        modifying_status: Union[Unset, str] = UNSET
        if not isinstance(self.modifying_status, Unset):
            modifying_status = self.modifying_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if modifying_status is not UNSET:
            field_dict["ModifyingStatus"] = modifying_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        _modifying_status = d.pop("ModifyingStatus", UNSET)
        modifying_status: Union[Unset, ApiTestExecutionModifyingStatus]
        if isinstance(_modifying_status, Unset):
            modifying_status = UNSET
        else:
            modifying_status = ApiTestExecutionModifyingStatus(_modifying_status)

        api_test_execution_patch_response = cls(
            guid=guid,
            modifying_status=modifying_status,
        )

        return api_test_execution_patch_response
