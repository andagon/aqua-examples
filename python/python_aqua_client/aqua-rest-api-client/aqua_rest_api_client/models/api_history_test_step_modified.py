from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_history_automation import ApiHistoryAutomation
    from ..models.api_history_field_changed import ApiHistoryFieldChanged


T = TypeVar("T", bound="ApiHistoryTestStepModified")


@attr.s(auto_attribs=True)
class ApiHistoryTestStepModified:
    """Contains the changes made to an existing test step. So far, only
    the test step name and id are included.

        Attributes:
            id (Union[Unset, int]): The id of the test step.
            current_name (Union[Unset, None, str]): The name of the test step.
            fields (Union[Unset, None, List['ApiHistoryFieldChanged']]): The list of changes to the fields
            automation (Union[Unset, None, ApiHistoryAutomation]): Contains the automation changes.
    """

    id: Union[Unset, int] = UNSET
    current_name: Union[Unset, None, str] = UNSET
    fields: Union[Unset, None, List["ApiHistoryFieldChanged"]] = UNSET
    automation: Union[Unset, None, "ApiHistoryAutomation"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        current_name = self.current_name
        fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            if self.fields is None:
                fields = None
            else:
                fields = []
                for fields_item_data in self.fields:
                    fields_item = fields_item_data.to_dict()

                    fields.append(fields_item)

        automation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.automation, Unset):
            automation = self.automation.to_dict() if self.automation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if current_name is not UNSET:
            field_dict["CurrentName"] = current_name
        if fields is not UNSET:
            field_dict["Fields"] = fields
        if automation is not UNSET:
            field_dict["Automation"] = automation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_history_automation import ApiHistoryAutomation
        from ..models.api_history_field_changed import ApiHistoryFieldChanged

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        current_name = d.pop("CurrentName", UNSET)

        fields = []
        _fields = d.pop("Fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ApiHistoryFieldChanged.from_dict(fields_item_data)

            fields.append(fields_item)

        _automation = d.pop("Automation", UNSET)
        automation: Union[Unset, None, ApiHistoryAutomation]
        if _automation is None:
            automation = None
        elif isinstance(_automation, Unset):
            automation = UNSET
        else:
            automation = ApiHistoryAutomation.from_dict(_automation)

        api_history_test_step_modified = cls(
            id=id,
            current_name=current_name,
            fields=fields,
            automation=automation,
        )

        return api_history_test_step_modified
