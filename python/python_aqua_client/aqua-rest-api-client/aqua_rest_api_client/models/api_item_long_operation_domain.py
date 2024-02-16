from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemLongOperationDomain")


@attr.s(auto_attribs=True)
class ApiItemLongOperationDomain:
    """Defines set of items to be processed.

    Attributes:
        type (str):
        project_id (Union[Unset, int]): Project where to look in.
    """

    type: str
    project_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Type": type,
            }
        )
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("Type")

        project_id = d.pop("ProjectId", UNSET)

        api_item_long_operation_domain = cls(
            type=type,
            project_id=project_id,
        )

        return api_item_long_operation_domain
