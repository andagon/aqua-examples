import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_aqua_client_type import ApiAquaClientType
from ..models.api_user_session_state import ApiUserSessionState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_license_profile_utilization_info import ApiLicenseProfileUtilizationInfo
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiUserLastActivityInfo")


@attr.s(auto_attribs=True)
class ApiUserLastActivityInfo:
    """
    Attributes:
        last_activity (Union[Unset, None, datetime.datetime]):
        license_usage (Union[Unset, None, List['ApiLicenseProfileUtilizationInfo']]):
        client_id (Union[Unset, None, str]):
        user (Union[Unset, None, ApiUserInfo]): The user information
        state (Union[Unset, ApiUserSessionState]):
            This enum has the following values:
              - `Active`
              - `Inactive`
              - `Unknown`
        client_type (Union[Unset, ApiAquaClientType]):
            This enum has the following values:
              - `API` API Client
              - `Offline` Offline Desktop Client (Depricated)
              - `Rich` Desktop Client
              - `Unknown` Unknown or invalid client
              - `Web` Web Client
    """

    last_activity: Union[Unset, None, datetime.datetime] = UNSET
    license_usage: Union[Unset, None, List["ApiLicenseProfileUtilizationInfo"]] = UNSET
    client_id: Union[Unset, None, str] = UNSET
    user: Union[Unset, None, "ApiUserInfo"] = UNSET
    state: Union[Unset, ApiUserSessionState] = UNSET
    client_type: Union[Unset, ApiAquaClientType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        last_activity: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_activity, Unset):
            last_activity = self.last_activity.isoformat() if self.last_activity else None

        license_usage: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.license_usage, Unset):
            if self.license_usage is None:
                license_usage = None
            else:
                license_usage = []
                for license_usage_item_data in self.license_usage:
                    license_usage_item = license_usage_item_data.to_dict()

                    license_usage.append(license_usage_item)

        client_id = self.client_id
        user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict() if self.user else None

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        client_type: Union[Unset, str] = UNSET
        if not isinstance(self.client_type, Unset):
            client_type = self.client_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if last_activity is not UNSET:
            field_dict["LastActivity"] = last_activity
        if license_usage is not UNSET:
            field_dict["LicenseUsage"] = license_usage
        if client_id is not UNSET:
            field_dict["ClientId"] = client_id
        if user is not UNSET:
            field_dict["User"] = user
        if state is not UNSET:
            field_dict["State"] = state
        if client_type is not UNSET:
            field_dict["ClientType"] = client_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_license_profile_utilization_info import ApiLicenseProfileUtilizationInfo
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        _last_activity = d.pop("LastActivity", UNSET)
        last_activity: Union[Unset, None, datetime.datetime]
        if _last_activity is None:
            last_activity = None
        elif isinstance(_last_activity, Unset):
            last_activity = UNSET
        else:
            last_activity = isoparse(_last_activity)

        license_usage = []
        _license_usage = d.pop("LicenseUsage", UNSET)
        for license_usage_item_data in _license_usage or []:
            license_usage_item = ApiLicenseProfileUtilizationInfo.from_dict(license_usage_item_data)

            license_usage.append(license_usage_item)

        client_id = d.pop("ClientId", UNSET)

        _user = d.pop("User", UNSET)
        user: Union[Unset, None, ApiUserInfo]
        if _user is None:
            user = None
        elif isinstance(_user, Unset):
            user = UNSET
        else:
            user = ApiUserInfo.from_dict(_user)

        _state = d.pop("State", UNSET)
        state: Union[Unset, ApiUserSessionState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ApiUserSessionState(_state)

        _client_type = d.pop("ClientType", UNSET)
        client_type: Union[Unset, ApiAquaClientType]
        if isinstance(_client_type, Unset):
            client_type = UNSET
        else:
            client_type = ApiAquaClientType(_client_type)

        api_user_last_activity_info = cls(
            last_activity=last_activity,
            license_usage=license_usage,
            client_id=client_id,
            user=user,
            state=state,
            client_type=client_type,
        )

        return api_user_last_activity_info
