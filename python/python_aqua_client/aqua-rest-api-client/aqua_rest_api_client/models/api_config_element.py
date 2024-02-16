from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_config_element_entry import ApiConfigElementEntry


T = TypeVar("T", bound="ApiConfigElement")


@attr.s(auto_attribs=True)
class ApiConfigElement:
    """
    Attributes:
        data_path (Union[Unset, None, str]): Path of the config element. Lowercase letters divided by dots are expected
            here
            e.g. "this.is.sample.path".
        locked (Union[Unset, bool]): True if the config element is locked.
            The flag is considered only for non-user entries (project or global).
        project_id (Union[Unset, None, int]): Id of the project this config element belongs to.
            Can be null - then represents global configuration (system-wide).
        user_id (Union[Unset, None, int]): Id of the owner user. Can be null, then represents a default
            configuration (either project or global level).
        entries (Union[Unset, None, List['ApiConfigElementEntry']]): Entries in this config element.
    """

    data_path: Union[Unset, None, str] = UNSET
    locked: Union[Unset, bool] = UNSET
    project_id: Union[Unset, None, int] = UNSET
    user_id: Union[Unset, None, int] = UNSET
    entries: Union[Unset, None, List["ApiConfigElementEntry"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_path = self.data_path
        locked = self.locked
        project_id = self.project_id
        user_id = self.user_id
        entries: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            if self.entries is None:
                entries = None
            else:
                entries = []
                for entries_item_data in self.entries:
                    entries_item = entries_item_data.to_dict()

                    entries.append(entries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_path is not UNSET:
            field_dict["DataPath"] = data_path
        if locked is not UNSET:
            field_dict["Locked"] = locked
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if entries is not UNSET:
            field_dict["Entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_config_element_entry import ApiConfigElementEntry

        d = src_dict.copy()
        data_path = d.pop("DataPath", UNSET)

        locked = d.pop("Locked", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        user_id = d.pop("UserId", UNSET)

        entries = []
        _entries = d.pop("Entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ApiConfigElementEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        api_config_element = cls(
            data_path=data_path,
            locked=locked,
            project_id=project_id,
            user_id=user_id,
            entries=entries,
        )

        api_config_element.additional_properties = d
        return api_config_element

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
