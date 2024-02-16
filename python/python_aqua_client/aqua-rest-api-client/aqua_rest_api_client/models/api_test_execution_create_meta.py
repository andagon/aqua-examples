from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_edit_layout import ApiEditLayout
    from ..models.api_field import ApiField


T = TypeVar("T", bound="ApiTestExecutionCreateMeta")


@attr.s(auto_attribs=True)
class ApiTestExecutionCreateMeta:
    """Contains the metadata which is necessary for creating a new execution.

    Attributes:
        fields (List['ApiField']): Contains all available fields together with their metadata.
        edit_layout (ApiEditLayout):
    """

    fields: List["ApiField"]
    edit_layout: "ApiEditLayout"

    def to_dict(self) -> Dict[str, Any]:
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()

            fields.append(fields_item)

        edit_layout = self.edit_layout.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Fields": fields,
                "EditLayout": edit_layout,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_edit_layout import ApiEditLayout
        from ..models.api_field import ApiField

        d = src_dict.copy()
        fields = []
        _fields = d.pop("Fields")
        for fields_item_data in _fields:
            fields_item = ApiField.from_dict(fields_item_data)

            fields.append(fields_item)

        edit_layout = ApiEditLayout.from_dict(d.pop("EditLayout"))

        api_test_execution_create_meta = cls(
            fields=fields,
            edit_layout=edit_layout,
        )

        return api_test_execution_create_meta
