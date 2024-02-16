from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_value_header_value import NameValueHeaderValue


T = TypeVar("T", bound="TransferCodingHeaderValue")


@attr.s(auto_attribs=True)
class TransferCodingHeaderValue:
    """
    Attributes:
        value (Union[Unset, None, str]):
        parameters (Union[Unset, None, List['NameValueHeaderValue']]):
    """

    value: Union[Unset, None, str] = UNSET
    parameters: Union[Unset, None, List["NameValueHeaderValue"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        parameters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            if self.parameters is None:
                parameters = None
            else:
                parameters = []
                for parameters_item_data in self.parameters:
                    parameters_item = parameters_item_data.to_dict()

                    parameters.append(parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["Value"] = value
        if parameters is not UNSET:
            field_dict["Parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.name_value_header_value import NameValueHeaderValue

        d = src_dict.copy()
        value = d.pop("Value", UNSET)

        parameters = []
        _parameters = d.pop("Parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = NameValueHeaderValue.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        transfer_coding_header_value = cls(
            value=value,
            parameters=parameters,
        )

        return transfer_coding_header_value
