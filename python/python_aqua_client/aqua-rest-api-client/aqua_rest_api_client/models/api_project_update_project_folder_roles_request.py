from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_delete_project_folder_role import ApiDeleteProjectFolderRole
    from ..models.api_update_project_folder_role import ApiUpdateProjectFolderRole


T = TypeVar("T", bound="ApiProjectUpdateProjectFolderRolesRequest")


@attr.s(auto_attribs=True)
class ApiProjectUpdateProjectFolderRolesRequest:
    """Contains information about update for the project roles.

    Attributes:
        add_roles (Union[Unset, None, List['ApiUpdateProjectFolderRole']]): The list of roles wich should be added or
            modified.
        delete_roles (Union[Unset, None, List['ApiDeleteProjectFolderRole']]): The list of roles wich should be deleted.
    """

    add_roles: Union[Unset, None, List["ApiUpdateProjectFolderRole"]] = UNSET
    delete_roles: Union[Unset, None, List["ApiDeleteProjectFolderRole"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        add_roles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.add_roles, Unset):
            if self.add_roles is None:
                add_roles = None
            else:
                add_roles = []
                for add_roles_item_data in self.add_roles:
                    add_roles_item = add_roles_item_data.to_dict()

                    add_roles.append(add_roles_item)

        delete_roles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.delete_roles, Unset):
            if self.delete_roles is None:
                delete_roles = None
            else:
                delete_roles = []
                for delete_roles_item_data in self.delete_roles:
                    delete_roles_item = delete_roles_item_data.to_dict()

                    delete_roles.append(delete_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if add_roles is not UNSET:
            field_dict["AddRoles"] = add_roles
        if delete_roles is not UNSET:
            field_dict["DeleteRoles"] = delete_roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_delete_project_folder_role import ApiDeleteProjectFolderRole
        from ..models.api_update_project_folder_role import ApiUpdateProjectFolderRole

        d = src_dict.copy()
        add_roles = []
        _add_roles = d.pop("AddRoles", UNSET)
        for add_roles_item_data in _add_roles or []:
            add_roles_item = ApiUpdateProjectFolderRole.from_dict(add_roles_item_data)

            add_roles.append(add_roles_item)

        delete_roles = []
        _delete_roles = d.pop("DeleteRoles", UNSET)
        for delete_roles_item_data in _delete_roles or []:
            delete_roles_item = ApiDeleteProjectFolderRole.from_dict(delete_roles_item_data)

            delete_roles.append(delete_roles_item)

        api_project_update_project_folder_roles_request = cls(
            add_roles=add_roles,
            delete_roles=delete_roles,
        )

        return api_project_update_project_folder_roles_request
