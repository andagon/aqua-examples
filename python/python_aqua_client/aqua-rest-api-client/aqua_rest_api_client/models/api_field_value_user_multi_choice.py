from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiFieldValueUserMultiChoice")


@attr.s(auto_attribs=True)
class ApiFieldValueUserMultiChoice:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
        ids (Union[Unset, None, List[int]]): The list of user ids
        values (Union[Unset, None, List['ApiUserInfo']]): The list of users. Contains more information on each user.
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET
    ids: Union[Unset, None, List[int]] = UNSET
    values: Union[Unset, None, List["ApiUserInfo"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text
        ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.ids, Unset):
            if self.ids is None:
                ids = None
            else:
                ids = self.ids

        values: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            if self.values is None:
                values = None
            else:
                values = []
                for values_item_data in self.values:
                    values_item = values_item_data.to_dict()

                    values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldValueType": field_value_type,
            }
        )
        if text is not UNSET:
            field_dict["Text"] = text
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if values is not UNSET:
            field_dict["Values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        field_value_type = d.pop("FieldValueType")

        text = d.pop("Text", UNSET)

        ids = cast(List[int], d.pop("Ids", UNSET))

        values = []
        _values = d.pop("Values", UNSET)
        for values_item_data in _values or []:
            values_item = ApiUserInfo.from_dict(values_item_data)

            values.append(values_item)

        api_field_value_user_multi_choice = cls(
            field_value_type=field_value_type,
            text=text,
            ids=ids,
            values=values,
        )

        api_field_value_user_multi_choice.additional_properties = d
        return api_field_value_user_multi_choice

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
