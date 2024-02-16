from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProjectTemplateDictionaryUsage")


@attr.s(auto_attribs=True)
class ApiProjectTemplateDictionaryUsage:
    """Represents a usage of dictionary by a custom field.

    Attributes:
        item_type (Union[Unset, ApiItemType]): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        field_id (Union[Unset, None, str]): Id of the field
        field_title (Union[Unset, None, str]): Field title
    """

    item_type: Union[Unset, ApiItemType] = UNSET
    field_id: Union[Unset, None, str] = UNSET
    field_title: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        field_id = self.field_id
        field_title = self.field_title

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if field_title is not UNSET:
            field_dict["FieldTitle"] = field_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        field_id = d.pop("FieldId", UNSET)

        field_title = d.pop("FieldTitle", UNSET)

        api_project_template_dictionary_usage = cls(
            item_type=item_type,
            field_id=field_id,
            field_title=field_title,
        )

        return api_project_template_dictionary_usage
