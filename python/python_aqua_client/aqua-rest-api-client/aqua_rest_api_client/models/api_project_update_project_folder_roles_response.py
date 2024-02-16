from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_error_information import ApiErrorInformation


T = TypeVar("T", bound="ApiProjectUpdateProjectFolderRolesResponse")


@attr.s(auto_attribs=True)
class ApiProjectUpdateProjectFolderRolesResponse:
    """Contains information about update on the project folder roles.

    Attributes:
        error_occurred (Union[Unset, bool]): Indicates if an error occurred during the update.
        error_list (Union[Unset, None, List['ApiErrorInformation']]): The error list.
    """

    error_occurred: Union[Unset, bool] = UNSET
    error_list: Union[Unset, None, List["ApiErrorInformation"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        error_occurred = self.error_occurred
        error_list: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.error_list, Unset):
            if self.error_list is None:
                error_list = None
            else:
                error_list = []
                for error_list_item_data in self.error_list:
                    error_list_item = error_list_item_data.to_dict()

                    error_list.append(error_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if error_occurred is not UNSET:
            field_dict["ErrorOccurred"] = error_occurred
        if error_list is not UNSET:
            field_dict["ErrorList"] = error_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_error_information import ApiErrorInformation

        d = src_dict.copy()
        error_occurred = d.pop("ErrorOccurred", UNSET)

        error_list = []
        _error_list = d.pop("ErrorList", UNSET)
        for error_list_item_data in _error_list or []:
            error_list_item = ApiErrorInformation.from_dict(error_list_item_data)

            error_list.append(error_list_item)

        api_project_update_project_folder_roles_response = cls(
            error_occurred=error_occurred,
            error_list=error_list,
        )

        return api_project_update_project_folder_roles_response
