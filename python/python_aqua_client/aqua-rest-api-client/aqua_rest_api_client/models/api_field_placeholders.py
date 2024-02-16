from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_placeholder import ApiFieldPlaceholder


T = TypeVar("T", bound="ApiFieldPlaceholders")


@attr.s(auto_attribs=True)
class ApiFieldPlaceholders:
    """Contains the placeholder fields of a test case.

    Attributes:
        fields (Union[Unset, None, List['ApiFieldPlaceholder']]): The list of fields that can be used as replacement
            placeholders in the TestCase
    """

    fields: Union[Unset, None, List["ApiFieldPlaceholder"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            if self.fields is None:
                fields = None
            else:
                fields = []
                for fields_item_data in self.fields:
                    fields_item = fields_item_data.to_dict()

                    fields.append(fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if fields is not UNSET:
            field_dict["Fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_placeholder import ApiFieldPlaceholder

        d = src_dict.copy()
        fields = []
        _fields = d.pop("Fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ApiFieldPlaceholder.from_dict(fields_item_data)

            fields.append(fields_item)

        api_field_placeholders = cls(
            fields=fields,
        )

        return api_field_placeholders
