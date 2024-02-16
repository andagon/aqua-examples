from enum import Enum


class ApiLoginIncidentReason(str, Enum):
    UNKNOWN = "Unknown"
    FLOATINGLICENSENOTAVAILABLE = "FloatingLicenseNotAvailable"
    NOLICENSEASSIGNMENT = "NoLicenseAssignment"
    NOACTIVELICENSEASSIGNMENT = "NoActiveLicenseAssignment"
    NOLOGINPERMISSION = "NoLoginPermission"
    AUTHENTICATIONFAILURE = "AuthenticationFailure"
    USERDEACTIVATED = "UserDeactivated"
    USERDELETED = "UserDeleted"
    NOTMEMBEROFCUSTOMER = "NotMemberOfCustomer"
    CUSTOMERDEACTIVATED = "CustomerDeactivated"
    USERNAMENOTUNIQUE = "UsernameNotUnique"

    def __str__(self) -> str:
        return str(self.value)
