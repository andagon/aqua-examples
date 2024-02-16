from enum import Enum


class ApiLicenseProfileUtilization(str, Enum):
    NOVALIDLICENSE = "NoValidLicense"
    LICENSEGRANTED = "LicenseGranted"
    FLOATINGLICENSENOTAVAILABLE = "FloatingLicenseNotAvailable"
    PROFILEDEACTIVATEDBYLICENSE = "ProfileDeactivatedByLicense"

    def __str__(self) -> str:
        return str(self.value)
