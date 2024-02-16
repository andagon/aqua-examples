from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectSubfoldersBatchCreate")


@attr.s(auto_attribs=True)
class ApiProjectSubfoldersBatchCreate:
    """
    Attributes:
        operation_type (str):
        path_separator (Union[Unset, None, str]): Path separator. Expected to be single character.
        subfolders (Union[Unset, None, List[str]]): List of subfolders to be created. Each entry is a full path of the
            folder (relative to the origin parent folder).
            For example, the following list:

            /a
            /a/b
            /a/b/c
            /a/b/d

            would create a tree structure:

            * project
              - parent folder
                - a
                  - b
                    - c
                    - d

            WARNING! folders needs to be included on the list in order that guarantee parent folder is before its children.
    """

    operation_type: str
    path_separator: Union[Unset, None, str] = UNSET
    subfolders: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type
        path_separator = self.path_separator
        subfolders: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.subfolders, Unset):
            if self.subfolders is None:
                subfolders = None
            else:
                subfolders = self.subfolders

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OperationType": operation_type,
            }
        )
        if path_separator is not UNSET:
            field_dict["PathSeparator"] = path_separator
        if subfolders is not UNSET:
            field_dict["Subfolders"] = subfolders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_type = d.pop("OperationType")

        path_separator = d.pop("PathSeparator", UNSET)

        subfolders = cast(List[str], d.pop("Subfolders", UNSET))

        api_project_subfolders_batch_create = cls(
            operation_type=operation_type,
            path_separator=path_separator,
            subfolders=subfolders,
        )

        api_project_subfolders_batch_create.additional_properties = d
        return api_project_subfolders_batch_create

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
