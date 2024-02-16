from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_report_xls_printout_encryption_type import ApiReportXlsPrintoutEncryptionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiReportXlPrintoutEncryptionOptions")


@attr.s(auto_attribs=True)
class ApiReportXlPrintoutEncryptionOptions:
    """
    Attributes:
        password (Union[Unset, None, str]): Password to open the file Default: ''.
        type (Union[Unset, ApiReportXlsPrintoutEncryptionType]):
            This enum has the following values:
              - `Compatible`
              - `Strong`
             Default: ApiReportXlsPrintoutEncryptionType.STRONG.
    """

    password: Union[Unset, None, str] = ""
    type: Union[Unset, ApiReportXlsPrintoutEncryptionType] = ApiReportXlsPrintoutEncryptionType.STRONG

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if password is not UNSET:
            field_dict["Password"] = password
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("Password", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiReportXlsPrintoutEncryptionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiReportXlsPrintoutEncryptionType(_type)

        api_report_xl_printout_encryption_options = cls(
            password=password,
            type=type,
        )

        return api_report_xl_printout_encryption_options
