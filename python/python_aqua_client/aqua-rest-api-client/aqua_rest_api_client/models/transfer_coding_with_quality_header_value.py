from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_value_header_value import NameValueHeaderValue


T = TypeVar("T", bound="TransferCodingWithQualityHeaderValue")


@attr.s(auto_attribs=True)
class TransferCodingWithQualityHeaderValue:
    """
    Attributes:
        value (Union[Unset, None, str]):
        parameters (Union[Unset, None, List['NameValueHeaderValue']]):
        quality (Union[Unset, None, float]):
    """

    value: Union[Unset, None, str] = UNSET
    parameters: Union[Unset, None, List["NameValueHeaderValue"]] = UNSET
    quality: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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

        quality = self.quality

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["Value"] = value
        if parameters is not UNSET:
            field_dict["Parameters"] = parameters
        if quality is not UNSET:
            field_dict["Quality"] = quality

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

        quality = d.pop("Quality", UNSET)

        transfer_coding_with_quality_header_value = cls(
            value=value,
            parameters=parameters,
            quality=quality,
        )

        transfer_coding_with_quality_header_value.additional_properties = d
        return transfer_coding_with_quality_header_value

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
