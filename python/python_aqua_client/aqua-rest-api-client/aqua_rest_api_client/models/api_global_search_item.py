from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_item_type import ApiItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiGlobalSearchItem")


@attr.s(auto_attribs=True)
class ApiGlobalSearchItem:
    """Represents an item for a global search

    Attributes:
        id (Union[Unset, int]): Id of item
        name (Union[Unset, None, str]): Name of item
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
        project_name (Union[Unset, None, str]): Name of the project which contains this item
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    item_type: Union[Unset, ApiItemType] = UNSET
    project_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        project_name = self.project_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if project_name is not UNSET:
            field_dict["ProjectName"] = project_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ApiItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ApiItemType(_item_type)

        project_name = d.pop("ProjectName", UNSET)

        api_global_search_item = cls(
            id=id,
            name=name,
            item_type=item_type,
            project_name=project_name,
        )

        return api_global_search_item
