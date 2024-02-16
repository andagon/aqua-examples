from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiItemArrangement")


@attr.s(auto_attribs=True)
class ApiItemArrangement:
    """Represents the filter, sorting and search information

    Attributes:
        filter_ (Union[Unset, None, str]): The filter syntax is as follows:
            on the first place should be the FieldId followed by the operator and if the operator expects an value followed
            by the value.
            [["Priority", "=", "High"], "and", ["DateCreatedDateTime", ">=", "2018-01-01"]]
            The values for different field types should be defined as follows:

                String: the value as string
                Decimal: the value as number
                Datetime: a string defining the date and time in the following format: yyyy-MM-ddTHH:mm:ssK or
                yyyy-MM-ddTHH:mm:ss.fffK. The K represents optional time zone information (Z for UTC or a time zone offset).
                E.g.: 2018-03-15T21:42:42, 2018-03-15T21:42:42.123, 2018-03-15T21:42:42.123Z, 2018-03-15T21:42:42.123+02:00.
                Dictionary: the id of the field value as number
                MultiChoiceDictionary: a list of numbers where each number is a field value id. E.g.: [1,2]
                User: the user id as number.
                MultiChoiceUser: a list of numbers where each number is a user id. E.g.: [1,2]
                TimeSpan: the value of the time span as number in seconds.
                Sprint: the id of the sprint as number.

            The [field meta data](#operation/ProjectMeta_GetProjectFieldMeta) can be used to check which filter operators
            are supported for which fields.
        sorting (Union[Unset, None, str]): The sorting syntax is as follows:
            [["Significane", "desc"], ["Status", "asc]].
            The [field meta data](#operation/ProjectMeta_GetProjectFieldMeta) can be used to check which fields support
            sorting.
        search (Union[Unset, None, str]): A fulltext search will be performed with this term and only matching
            items will be included in the result
        time_zone_offset (Union[Unset, None, int]): The time zone offset, in minutes, of the client. Used for date
            filter operations
    """

    filter_: Union[Unset, None, str] = UNSET
    sorting: Union[Unset, None, str] = UNSET
    search: Union[Unset, None, str] = UNSET
    time_zone_offset: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        filter_ = self.filter_
        sorting = self.sorting
        search = self.search
        time_zone_offset = self.time_zone_offset

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["Filter"] = filter_
        if sorting is not UNSET:
            field_dict["Sorting"] = sorting
        if search is not UNSET:
            field_dict["Search"] = search
        if time_zone_offset is not UNSET:
            field_dict["TimeZoneOffset"] = time_zone_offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filter_ = d.pop("Filter", UNSET)

        sorting = d.pop("Sorting", UNSET)

        search = d.pop("Search", UNSET)

        time_zone_offset = d.pop("TimeZoneOffset", UNSET)

        api_item_arrangement = cls(
            filter_=filter_,
            sorting=sorting,
            search=search,
            time_zone_offset=time_zone_offset,
        )

        return api_item_arrangement
