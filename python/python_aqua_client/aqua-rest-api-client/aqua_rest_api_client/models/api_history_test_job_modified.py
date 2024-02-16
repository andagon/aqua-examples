from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_history_field_changed import ApiHistoryFieldChanged


T = TypeVar("T", bound="ApiHistoryTestJobModified")


@attr.s(auto_attribs=True)
class ApiHistoryTestJobModified:
    """Contains the changes made to an existing test job.

    Attributes:
        id (Union[Unset, int]): The id of the test job.
        test_case_id (Union[Unset, None, str]): Formatted id of the related test case .
        fields (Union[Unset, None, List['ApiHistoryFieldChanged']]): The list of changes to the fields
    """

    id: Union[Unset, int] = UNSET
    test_case_id: Union[Unset, None, str] = UNSET
    fields: Union[Unset, None, List["ApiHistoryFieldChanged"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        test_case_id = self.test_case_id
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
        if id is not UNSET:
            field_dict["Id"] = id
        if test_case_id is not UNSET:
            field_dict["TestCaseId"] = test_case_id
        if fields is not UNSET:
            field_dict["Fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_history_field_changed import ApiHistoryFieldChanged

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        test_case_id = d.pop("TestCaseId", UNSET)

        fields = []
        _fields = d.pop("Fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ApiHistoryFieldChanged.from_dict(fields_item_data)

            fields.append(fields_item)

        api_history_test_job_modified = cls(
            id=id,
            test_case_id=test_case_id,
            fields=fields,
        )

        return api_history_test_job_modified
