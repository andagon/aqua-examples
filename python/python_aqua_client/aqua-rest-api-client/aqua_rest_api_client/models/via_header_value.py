from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViaHeaderValue")


@attr.s(auto_attribs=True)
class ViaHeaderValue:
    """
    Attributes:
        protocol_name (Union[Unset, None, str]):
        protocol_version (Union[Unset, None, str]):
        received_by (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
    """

    protocol_name: Union[Unset, None, str] = UNSET
    protocol_version: Union[Unset, None, str] = UNSET
    received_by: Union[Unset, None, str] = UNSET
    comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        protocol_name = self.protocol_name
        protocol_version = self.protocol_version
        received_by = self.received_by
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if protocol_name is not UNSET:
            field_dict["ProtocolName"] = protocol_name
        if protocol_version is not UNSET:
            field_dict["ProtocolVersion"] = protocol_version
        if received_by is not UNSET:
            field_dict["ReceivedBy"] = received_by
        if comment is not UNSET:
            field_dict["Comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocol_name = d.pop("ProtocolName", UNSET)

        protocol_version = d.pop("ProtocolVersion", UNSET)

        received_by = d.pop("ReceivedBy", UNSET)

        comment = d.pop("Comment", UNSET)

        via_header_value = cls(
            protocol_name=protocol_name,
            protocol_version=protocol_version,
            received_by=received_by,
            comment=comment,
        )

        return via_header_value
