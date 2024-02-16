from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestDataPreview")


@attr.s(auto_attribs=True)
class ApiTestDataPreview:
    """This model is used when generating a "preview" of test data i.e. request server to provide
    actual data for all formulas included in the data.

        Attributes:
            values (Union[Unset, None, List[List[str]]]): Content of test data matrix.
                Outer array represent rows, inner arrays represent cells in the row.
    """

    values: Union[Unset, None, List[List[str]]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        values: Union[Unset, None, List[List[str]]] = UNSET
        if not isinstance(self.values, Unset):
            if self.values is None:
                values = None
            else:
                values = []
                for values_item_data in self.values:
                    values_item = values_item_data

                    values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if values is not UNSET:
            field_dict["Values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        values = []
        _values = d.pop("Values", UNSET)
        for values_item_data in _values or []:
            values_item = cast(List[str], values_item_data)

            values.append(values_item)

        api_test_data_preview = cls(
            values=values,
        )

        return api_test_data_preview
