from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_value_header_value import NameValueHeaderValue


T = TypeVar("T", bound="MediaTypeHeaderValue")


@attr.s(auto_attribs=True)
class MediaTypeHeaderValue:
    """
    Attributes:
        char_set (Union[Unset, None, str]):
        parameters (Union[Unset, None, List['NameValueHeaderValue']]):
        media_type (Union[Unset, None, str]):
    """

    char_set: Union[Unset, None, str] = UNSET
    parameters: Union[Unset, None, List["NameValueHeaderValue"]] = UNSET
    media_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        char_set = self.char_set
        parameters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            if self.parameters is None:
                parameters = None
            else:
                parameters = []
                for parameters_item_data in self.parameters:
                    parameters_item = parameters_item_data.to_dict()

                    parameters.append(parameters_item)

        media_type = self.media_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if char_set is not UNSET:
            field_dict["CharSet"] = char_set
        if parameters is not UNSET:
            field_dict["Parameters"] = parameters
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.name_value_header_value import NameValueHeaderValue

        d = src_dict.copy()
        char_set = d.pop("CharSet", UNSET)

        parameters = []
        _parameters = d.pop("Parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = NameValueHeaderValue.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        media_type = d.pop("MediaType", UNSET)

        media_type_header_value = cls(
            char_set=char_set,
            parameters=parameters,
            media_type=media_type,
        )

        return media_type_header_value
