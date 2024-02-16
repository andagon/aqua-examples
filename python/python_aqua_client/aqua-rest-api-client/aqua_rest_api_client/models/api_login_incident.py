import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_aqua_client_type import ApiAquaClientType
from ..models.api_login_incident_reason import ApiLoginIncidentReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiLoginIncident")


@attr.s(auto_attribs=True)
class ApiLoginIncident:
    """
    Attributes:
        customer_id (Union[Unset, None, int]):
        login_successfull (Union[Unset, bool]):
        occurrence_date (Union[Unset, datetime.datetime]):
        reason_code (Union[Unset, ApiLoginIncidentReason]):
            This enum has the following values:
              - `AuthenticationFailure` User not authenticated (neither by external module, if any, nor by our mechanism;
            usually means invalid username or password).
              - `CustomerDeactivated` The customer is deactivated.
              - `FloatingLicenseNotAvailable` Not possible to obtain a floating license (all in use).
              - `NoActiveLicenseAssignment` User is assigned with a license(s) but all assignments are deactivated.
              - `NoLicenseAssignment` User is not assigned with any license.
              - `NoLoginPermission` User is assigned with some valid licenses, but they does not include a login permission
            for given client type.
              - `NotMemberOfCustomer` The user is not a member of the current customer.
              - `Unknown` unknown reason (or no reason).
              - `UserDeactivated` User is deactivated.
              - `UserDeleted` User is deleted.
              - `UsernameNotUnique` Indicates that the username is not unique. This might happen
            when different users have the same username in different capitalizations.
        reason_data (Union[Unset, None, str]):
        client_type (Union[Unset, ApiAquaClientType]):
            This enum has the following values:
              - `API` API Client
              - `Offline` Offline Desktop Client (Depricated)
              - `Rich` Desktop Client
              - `Unknown` Unknown or invalid client
              - `Web` Web Client
        client_id (Union[Unset, None, str]):
        relogin (Union[Unset, bool]):
        user (Union[Unset, None, ApiUserInfo]): The user information
    """

    customer_id: Union[Unset, None, int] = UNSET
    login_successfull: Union[Unset, bool] = UNSET
    occurrence_date: Union[Unset, datetime.datetime] = UNSET
    reason_code: Union[Unset, ApiLoginIncidentReason] = UNSET
    reason_data: Union[Unset, None, str] = UNSET
    client_type: Union[Unset, ApiAquaClientType] = UNSET
    client_id: Union[Unset, None, str] = UNSET
    relogin: Union[Unset, bool] = UNSET
    user: Union[Unset, None, "ApiUserInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
        login_successfull = self.login_successfull
        occurrence_date: Union[Unset, str] = UNSET
        if not isinstance(self.occurrence_date, Unset):
            occurrence_date = self.occurrence_date.isoformat()

        reason_code: Union[Unset, str] = UNSET
        if not isinstance(self.reason_code, Unset):
            reason_code = self.reason_code.value

        reason_data = self.reason_data
        client_type: Union[Unset, str] = UNSET
        if not isinstance(self.client_type, Unset):
            client_type = self.client_type.value

        client_id = self.client_id
        relogin = self.relogin
        user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict() if self.user else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["CustomerId"] = customer_id
        if login_successfull is not UNSET:
            field_dict["LoginSuccessfull"] = login_successfull
        if occurrence_date is not UNSET:
            field_dict["OccurrenceDate"] = occurrence_date
        if reason_code is not UNSET:
            field_dict["ReasonCode"] = reason_code
        if reason_data is not UNSET:
            field_dict["ReasonData"] = reason_data
        if client_type is not UNSET:
            field_dict["ClientType"] = client_type
        if client_id is not UNSET:
            field_dict["ClientId"] = client_id
        if relogin is not UNSET:
            field_dict["Relogin"] = relogin
        if user is not UNSET:
            field_dict["User"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        customer_id = d.pop("CustomerId", UNSET)

        login_successfull = d.pop("LoginSuccessfull", UNSET)

        _occurrence_date = d.pop("OccurrenceDate", UNSET)
        occurrence_date: Union[Unset, datetime.datetime]
        if isinstance(_occurrence_date, Unset):
            occurrence_date = UNSET
        else:
            occurrence_date = isoparse(_occurrence_date)

        _reason_code = d.pop("ReasonCode", UNSET)
        reason_code: Union[Unset, ApiLoginIncidentReason]
        if isinstance(_reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = ApiLoginIncidentReason(_reason_code)

        reason_data = d.pop("ReasonData", UNSET)

        _client_type = d.pop("ClientType", UNSET)
        client_type: Union[Unset, ApiAquaClientType]
        if isinstance(_client_type, Unset):
            client_type = UNSET
        else:
            client_type = ApiAquaClientType(_client_type)

        client_id = d.pop("ClientId", UNSET)

        relogin = d.pop("Relogin", UNSET)

        _user = d.pop("User", UNSET)
        user: Union[Unset, None, ApiUserInfo]
        if _user is None:
            user = None
        elif isinstance(_user, Unset):
            user = UNSET
        else:
            user = ApiUserInfo.from_dict(_user)

        api_login_incident = cls(
            customer_id=customer_id,
            login_successfull=login_successfull,
            occurrence_date=occurrence_date,
            reason_code=reason_code,
            reason_data=reason_data,
            client_type=client_type,
            client_id=client_id,
            relogin=relogin,
            user=user,
        )

        return api_login_incident
