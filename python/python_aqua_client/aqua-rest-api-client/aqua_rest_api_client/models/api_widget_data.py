from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiWidgetData")


@attr.s(auto_attribs=True)
class ApiWidgetData:
    """Base class for all widget data classes.

    Attributes:
        data_type (str):
    """

    data_type: str

    def to_dict(self) -> Dict[str, Any]:
        data_type = self.data_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "DataType": data_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_type = d.pop("DataType")

        api_widget_data = cls(
            data_type=data_type,
        )

        return api_widget_data
