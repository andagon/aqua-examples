from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiConfigElementPatchOperationDelete")


@attr.s(auto_attribs=True)
class ApiConfigElementPatchOperationDelete:
    """
    Attributes:
        operation_type (str):
        data_path (Union[Unset, None, str]): Path of the considered config elements. Lowercase letters divided by dots
            are expected here
            e.g. "this.is.sample.path".
        project_id (Union[Unset, None, int]): Id of the project where config element belongs to.
            Can be null - then represents global configurations (system-wide).
        user_id (Union[Unset, None, int]): Id of the owner user. Can be null, then represents a default
            configurations (either project or global level).
    """

    operation_type: str
    data_path: Union[Unset, None, str] = UNSET
    project_id: Union[Unset, None, int] = UNSET
    user_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        data_path = self.data_path
        project_id = self.project_id
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if data_path is not UNSET:
            field_dict["DataPath"] = data_path
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        data_path = d.pop("DataPath", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        user_id = d.pop("UserId", UNSET)

        api_config_element_patch_operation_delete = cls(
            operation_type=operation_type,
            data_path=data_path,
            project_id=project_id,
            user_id=user_id,
        )

        api_config_element_patch_operation_delete.additional_properties = d
        return api_config_element_patch_operation_delete

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
