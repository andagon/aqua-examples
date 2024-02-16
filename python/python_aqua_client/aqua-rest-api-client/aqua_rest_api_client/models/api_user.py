from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_user_status import ApiUserStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_license_profile import ApiLicenseProfile
    from ..models.api_user_license_assignment import ApiUserLicenseAssignment
    from ..models.api_user_project_assignment import ApiUserProjectAssignment


T = TypeVar("T", bound="ApiUser")


@attr.s(auto_attribs=True)
class ApiUser:
    """
    Attributes:
        id (Union[Unset, int]): The id of the user
        user_name (Union[Unset, None, str]): The username of the user
        first_name (Union[Unset, None, str]): The first name of the user
        surname (Union[Unset, None, str]): The surname / last name of the user
        fullname (Union[Unset, None, str]): The full name of the user. This string is correctly formatted and
            should be used when displaying a user e.g. in a list.
        email (Union[Unset, None, str]): The email address of the user
        phone (Union[Unset, None, str]): The phone number of the user
        position (Union[Unset, None, str]): The position of the user in the company
        picture_url (Union[Unset, None, str]): The absolute url of the user's picture. Might be null, if
            the user does not have a picture assigned.
        server_administrator (Union[Unset, bool]): Indicates if the user is server administrator or not.
        status (Union[Unset, ApiUserStatus]): Identifies the user status.
            This enum has the following values:
              - `Activated` The user is activated.
              - `Deactivated` The user is deactivated.
              - `LicenseDeactivated` The license is deactivated.
        projects (Union[Unset, None, List['ApiUserProjectAssignment']]): List of projects with roles assigned to the
            user.
        licenses (Union[Unset, None, List['ApiUserLicenseAssignment']]): List of licenses assigned to the user.
        license_profiles (Union[Unset, None, List['ApiLicenseProfile']]): List of license profiles
    """

    id: Union[Unset, int] = UNSET
    user_name: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    surname: Union[Unset, None, str] = UNSET
    fullname: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, str] = UNSET
    picture_url: Union[Unset, None, str] = UNSET
    server_administrator: Union[Unset, bool] = UNSET
    status: Union[Unset, ApiUserStatus] = UNSET
    projects: Union[Unset, None, List["ApiUserProjectAssignment"]] = UNSET
    licenses: Union[Unset, None, List["ApiUserLicenseAssignment"]] = UNSET
    license_profiles: Union[Unset, None, List["ApiLicenseProfile"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_name = self.user_name
        first_name = self.first_name
        surname = self.surname
        fullname = self.fullname
        email = self.email
        phone = self.phone
        position = self.position
        picture_url = self.picture_url
        server_administrator = self.server_administrator
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        projects: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            if self.projects is None:
                projects = None
            else:
                projects = []
                for projects_item_data in self.projects:
                    projects_item = projects_item_data.to_dict()

                    projects.append(projects_item)

        licenses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licenses, Unset):
            if self.licenses is None:
                licenses = None
            else:
                licenses = []
                for licenses_item_data in self.licenses:
                    licenses_item = licenses_item_data.to_dict()

                    licenses.append(licenses_item)

        license_profiles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.license_profiles, Unset):
            if self.license_profiles is None:
                license_profiles = None
            else:
                license_profiles = []
                for license_profiles_item_data in self.license_profiles:
                    license_profiles_item = license_profiles_item_data.to_dict()

                    license_profiles.append(license_profiles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if surname is not UNSET:
            field_dict["Surname"] = surname
        if fullname is not UNSET:
            field_dict["Fullname"] = fullname
        if email is not UNSET:
            field_dict["Email"] = email
        if phone is not UNSET:
            field_dict["Phone"] = phone
        if position is not UNSET:
            field_dict["Position"] = position
        if picture_url is not UNSET:
            field_dict["PictureUrl"] = picture_url
        if server_administrator is not UNSET:
            field_dict["ServerAdministrator"] = server_administrator
        if status is not UNSET:
            field_dict["Status"] = status
        if projects is not UNSET:
            field_dict["Projects"] = projects
        if licenses is not UNSET:
            field_dict["Licenses"] = licenses
        if license_profiles is not UNSET:
            field_dict["LicenseProfiles"] = license_profiles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_license_profile import ApiLicenseProfile
        from ..models.api_user_license_assignment import ApiUserLicenseAssignment
        from ..models.api_user_project_assignment import ApiUserProjectAssignment

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        user_name = d.pop("UserName", UNSET)

        first_name = d.pop("FirstName", UNSET)

        surname = d.pop("Surname", UNSET)

        fullname = d.pop("Fullname", UNSET)

        email = d.pop("Email", UNSET)

        phone = d.pop("Phone", UNSET)

        position = d.pop("Position", UNSET)

        picture_url = d.pop("PictureUrl", UNSET)

        server_administrator = d.pop("ServerAdministrator", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ApiUserStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiUserStatus(_status)

        projects = []
        _projects = d.pop("Projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = ApiUserProjectAssignment.from_dict(projects_item_data)

            projects.append(projects_item)

        licenses = []
        _licenses = d.pop("Licenses", UNSET)
        for licenses_item_data in _licenses or []:
            licenses_item = ApiUserLicenseAssignment.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        license_profiles = []
        _license_profiles = d.pop("LicenseProfiles", UNSET)
        for license_profiles_item_data in _license_profiles or []:
            license_profiles_item = ApiLicenseProfile.from_dict(license_profiles_item_data)

            license_profiles.append(license_profiles_item)

        api_user = cls(
            id=id,
            user_name=user_name,
            first_name=first_name,
            surname=surname,
            fullname=fullname,
            email=email,
            phone=phone,
            position=position,
            picture_url=picture_url,
            server_administrator=server_administrator,
            status=status,
            projects=projects,
            licenses=licenses,
            license_profiles=license_profiles,
        )

        api_user.additional_properties = d
        return api_user

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
