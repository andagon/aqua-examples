import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLicense")


@attr.s(auto_attribs=True)
class ApiLicense:
    """
    Attributes:
        code (Union[Unset, None, str]): The code of the license.
        name (Union[Unset, None, str]): The name of the license.
        max_named_licenses_available (Union[Unset, int]): The maximal number of named licenses.
        max_floating_licenses_available (Union[Unset, int]): The maximal number of floating licenses.
        start_time (Union[Unset, datetime.datetime]): The start date of the license.
        expiry_time (Union[Unset, datetime.datetime]): The expire date of the license.
    """

    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    max_named_licenses_available: Union[Unset, int] = UNSET
    max_floating_licenses_available: Union[Unset, int] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    expiry_time: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        max_named_licenses_available = self.max_named_licenses_available
        max_floating_licenses_available = self.max_floating_licenses_available
        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        expiry_time: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_time, Unset):
            expiry_time = self.expiry_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if code is not UNSET:
            field_dict["Code"] = code
        if name is not UNSET:
            field_dict["Name"] = name
        if max_named_licenses_available is not UNSET:
            field_dict["MaxNamedLicensesAvailable"] = max_named_licenses_available
        if max_floating_licenses_available is not UNSET:
            field_dict["MaxFloatingLicensesAvailable"] = max_floating_licenses_available
        if start_time is not UNSET:
            field_dict["StartTime"] = start_time
        if expiry_time is not UNSET:
            field_dict["ExpiryTime"] = expiry_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("Code", UNSET)

        name = d.pop("Name", UNSET)

        max_named_licenses_available = d.pop("MaxNamedLicensesAvailable", UNSET)

        max_floating_licenses_available = d.pop("MaxFloatingLicensesAvailable", UNSET)

        _start_time = d.pop("StartTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _expiry_time = d.pop("ExpiryTime", UNSET)
        expiry_time: Union[Unset, datetime.datetime]
        if isinstance(_expiry_time, Unset):
            expiry_time = UNSET
        else:
            expiry_time = isoparse(_expiry_time)

        api_license = cls(
            code=code,
            name=name,
            max_named_licenses_available=max_named_licenses_available,
            max_floating_licenses_available=max_floating_licenses_available,
            start_time=start_time,
            expiry_time=expiry_time,
        )

        return api_license
