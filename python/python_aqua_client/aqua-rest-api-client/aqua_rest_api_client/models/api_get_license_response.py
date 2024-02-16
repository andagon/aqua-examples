from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_license import ApiLicense


T = TypeVar("T", bound="ApiGetLicenseResponse")


@attr.s(auto_attribs=True)
class ApiGetLicenseResponse:
    """Represents the get license response.

    Attributes:
        licenses (Union[Unset, None, List['ApiLicense']]): The list of licenses.
    """

    licenses: Union[Unset, None, List["ApiLicense"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        licenses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licenses, Unset):
            if self.licenses is None:
                licenses = None
            else:
                licenses = []
                for licenses_item_data in self.licenses:
                    licenses_item = licenses_item_data.to_dict()

                    licenses.append(licenses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if licenses is not UNSET:
            field_dict["Licenses"] = licenses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_license import ApiLicense

        d = src_dict.copy()
        licenses = []
        _licenses = d.pop("Licenses", UNSET)
        for licenses_item_data in _licenses or []:
            licenses_item = ApiLicense.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        api_get_license_response = cls(
            licenses=licenses,
        )

        return api_get_license_response
