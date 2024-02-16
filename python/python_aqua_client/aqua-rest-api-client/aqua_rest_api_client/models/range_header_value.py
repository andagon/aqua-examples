from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_item_header_value import RangeItemHeaderValue


T = TypeVar("T", bound="RangeHeaderValue")


@attr.s(auto_attribs=True)
class RangeHeaderValue:
    """
    Attributes:
        unit (Union[Unset, None, str]):
        ranges (Union[Unset, None, List['RangeItemHeaderValue']]):
    """

    unit: Union[Unset, None, str] = UNSET
    ranges: Union[Unset, None, List["RangeItemHeaderValue"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        unit = self.unit
        ranges: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            if self.ranges is None:
                ranges = None
            else:
                ranges = []
                for ranges_item_data in self.ranges:
                    ranges_item = ranges_item_data.to_dict()

                    ranges.append(ranges_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if unit is not UNSET:
            field_dict["Unit"] = unit
        if ranges is not UNSET:
            field_dict["Ranges"] = ranges

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.range_item_header_value import RangeItemHeaderValue

        d = src_dict.copy()
        unit = d.pop("Unit", UNSET)

        ranges = []
        _ranges = d.pop("Ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = RangeItemHeaderValue.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        range_header_value = cls(
            unit=unit,
            ranges=ranges,
        )

        return range_header_value
