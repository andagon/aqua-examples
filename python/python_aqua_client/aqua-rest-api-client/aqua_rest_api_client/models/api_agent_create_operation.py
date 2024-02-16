from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiAgentCreateOperation")


@attr.s(auto_attribs=True)
class ApiAgentCreateOperation:
    """Represents data required to execute single agent - create operation.

    Attributes:
        create_operation (str):
    """

    create_operation: str

    def to_dict(self) -> Dict[str, Any]:
        create_operation = self.create_operation

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "CreateOperation": create_operation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        create_operation = d.pop("CreateOperation")

        api_agent_create_operation = cls(
            create_operation=create_operation,
        )

        return api_agent_create_operation
