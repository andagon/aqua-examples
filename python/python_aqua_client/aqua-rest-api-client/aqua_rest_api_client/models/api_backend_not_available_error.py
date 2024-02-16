from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBackendNotAvailableError")


@attr.s(auto_attribs=True)
class ApiBackendNotAvailableError:
    """
    Attributes:
        message (str): A human-readable description of the error.
        code (str): The error code to be used for tracking the error a the server side.
        type (str):
        further_info (Union[Unset, None, str]): Further information about the error as unstructured text. This text is
            not localized.
        error_data (Union[Unset, Any]): Additional data about the error (if any). Depends on actual error type.
    """

    message: str
    code: str
    type: str
    further_info: Union[Unset, None, str] = UNSET
    error_data: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        code = self.code
        type = self.type
        further_info = self.further_info
        error_data = self.error_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Message": message,
                "Code": code,
                "Type": type,
            }
        )
        if further_info is not UNSET:
            field_dict["FurtherInfo"] = further_info
        if error_data is not UNSET:
            field_dict["ErrorData"] = error_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("Message")

        code = d.pop("Code")

        type = d.pop("Type")

        further_info = d.pop("FurtherInfo", UNSET)

        error_data = d.pop("ErrorData", UNSET)

        api_backend_not_available_error = cls(
            message=message,
            code=code,
            type=type,
            further_info=further_info,
            error_data=error_data,
        )

        api_backend_not_available_error.additional_properties = d
        return api_backend_not_available_error

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
