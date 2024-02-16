import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_value_header_value import NameValueHeaderValue


T = TypeVar("T", bound="ContentDispositionHeaderValue")


@attr.s(auto_attribs=True)
class ContentDispositionHeaderValue:
    """
    Attributes:
        disposition_type (Union[Unset, None, str]):
        parameters (Union[Unset, None, List['NameValueHeaderValue']]):
        name (Union[Unset, None, str]):
        file_name (Union[Unset, None, str]):
        file_name_star (Union[Unset, None, str]):
        creation_date (Union[Unset, None, datetime.datetime]):
        modification_date (Union[Unset, None, datetime.datetime]):
        read_date (Union[Unset, None, datetime.datetime]):
        size (Union[Unset, None, int]):
    """

    disposition_type: Union[Unset, None, str] = UNSET
    parameters: Union[Unset, None, List["NameValueHeaderValue"]] = UNSET
    name: Union[Unset, None, str] = UNSET
    file_name: Union[Unset, None, str] = UNSET
    file_name_star: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, None, datetime.datetime] = UNSET
    modification_date: Union[Unset, None, datetime.datetime] = UNSET
    read_date: Union[Unset, None, datetime.datetime] = UNSET
    size: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        disposition_type = self.disposition_type
        parameters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            if self.parameters is None:
                parameters = None
            else:
                parameters = []
                for parameters_item_data in self.parameters:
                    parameters_item = parameters_item_data.to_dict()

                    parameters.append(parameters_item)

        name = self.name
        file_name = self.file_name
        file_name_star = self.file_name_star
        creation_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat() if self.creation_date else None

        modification_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modification_date, Unset):
            modification_date = self.modification_date.isoformat() if self.modification_date else None

        read_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.read_date, Unset):
            read_date = self.read_date.isoformat() if self.read_date else None

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if disposition_type is not UNSET:
            field_dict["DispositionType"] = disposition_type
        if parameters is not UNSET:
            field_dict["Parameters"] = parameters
        if name is not UNSET:
            field_dict["Name"] = name
        if file_name is not UNSET:
            field_dict["FileName"] = file_name
        if file_name_star is not UNSET:
            field_dict["FileNameStar"] = file_name_star
        if creation_date is not UNSET:
            field_dict["CreationDate"] = creation_date
        if modification_date is not UNSET:
            field_dict["ModificationDate"] = modification_date
        if read_date is not UNSET:
            field_dict["ReadDate"] = read_date
        if size is not UNSET:
            field_dict["Size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.name_value_header_value import NameValueHeaderValue

        d = src_dict.copy()
        disposition_type = d.pop("DispositionType", UNSET)

        parameters = []
        _parameters = d.pop("Parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = NameValueHeaderValue.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        name = d.pop("Name", UNSET)

        file_name = d.pop("FileName", UNSET)

        file_name_star = d.pop("FileNameStar", UNSET)

        _creation_date = d.pop("CreationDate", UNSET)
        creation_date: Union[Unset, None, datetime.datetime]
        if _creation_date is None:
            creation_date = None
        elif isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _modification_date = d.pop("ModificationDate", UNSET)
        modification_date: Union[Unset, None, datetime.datetime]
        if _modification_date is None:
            modification_date = None
        elif isinstance(_modification_date, Unset):
            modification_date = UNSET
        else:
            modification_date = isoparse(_modification_date)

        _read_date = d.pop("ReadDate", UNSET)
        read_date: Union[Unset, None, datetime.datetime]
        if _read_date is None:
            read_date = None
        elif isinstance(_read_date, Unset):
            read_date = UNSET
        else:
            read_date = isoparse(_read_date)

        size = d.pop("Size", UNSET)

        content_disposition_header_value = cls(
            disposition_type=disposition_type,
            parameters=parameters,
            name=name,
            file_name=file_name,
            file_name_star=file_name_star,
            creation_date=creation_date,
            modification_date=modification_date,
            read_date=read_date,
            size=size,
        )

        return content_disposition_header_value
