from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.pdf_encryption_level import PdfEncryptionLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_pdf_permissions_options import ApiPdfPermissionsOptions


T = TypeVar("T", bound="ApiPdfPasswordSecurityOptions")


@attr.s(auto_attribs=True)
class ApiPdfPasswordSecurityOptions:
    """
    Attributes:
        open_password (Union[Unset, None, str]): password for opening the exported PDF document. Default: ''.
        encryption_level (Union[Unset, PdfEncryptionLevel]):
            This enum has the following values:
              - `AES128`
              - `AES256`
              - `ARC4`
             Default: PdfEncryptionLevel.AES128.
        permissions_password (Union[Unset, None, str]): the PDF permissions password for the document. Default: ''.
        permissions_options (Union[Unset, None, ApiPdfPermissionsOptions]):
    """

    open_password: Union[Unset, None, str] = ""
    encryption_level: Union[Unset, PdfEncryptionLevel] = PdfEncryptionLevel.AES128
    permissions_password: Union[Unset, None, str] = ""
    permissions_options: Union[Unset, None, "ApiPdfPermissionsOptions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        open_password = self.open_password
        encryption_level: Union[Unset, str] = UNSET
        if not isinstance(self.encryption_level, Unset):
            encryption_level = self.encryption_level.value

        permissions_password = self.permissions_password
        permissions_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions_options, Unset):
            permissions_options = self.permissions_options.to_dict() if self.permissions_options else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if open_password is not UNSET:
            field_dict["OpenPassword"] = open_password
        if encryption_level is not UNSET:
            field_dict["EncryptionLevel"] = encryption_level
        if permissions_password is not UNSET:
            field_dict["PermissionsPassword"] = permissions_password
        if permissions_options is not UNSET:
            field_dict["PermissionsOptions"] = permissions_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_pdf_permissions_options import ApiPdfPermissionsOptions

        d = src_dict.copy()
        open_password = d.pop("OpenPassword", UNSET)

        _encryption_level = d.pop("EncryptionLevel", UNSET)
        encryption_level: Union[Unset, PdfEncryptionLevel]
        if isinstance(_encryption_level, Unset):
            encryption_level = UNSET
        else:
            encryption_level = PdfEncryptionLevel(_encryption_level)

        permissions_password = d.pop("PermissionsPassword", UNSET)

        _permissions_options = d.pop("PermissionsOptions", UNSET)
        permissions_options: Union[Unset, None, ApiPdfPermissionsOptions]
        if _permissions_options is None:
            permissions_options = None
        elif isinstance(_permissions_options, Unset):
            permissions_options = UNSET
        else:
            permissions_options = ApiPdfPermissionsOptions.from_dict(_permissions_options)

        api_pdf_password_security_options = cls(
            open_password=open_password,
            encryption_level=encryption_level,
            permissions_password=permissions_password,
            permissions_options=permissions_options,
        )

        return api_pdf_password_security_options
