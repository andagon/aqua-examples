from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_label_info import ApiLabelInfo


T = TypeVar("T", bound="ApiLabel")


@attr.s(auto_attribs=True)
class ApiLabel:
    """
    Attributes:
        id (Union[Unset, int]): Id of this label.
        version (Union[Unset, int]): Label version.
        name (Union[Unset, None, str]): Name of this label. The name is unique in combination with the base object type.
        description (Union[Unset, None, str]): Description of this label.
        sub_labels (Union[Unset, None, List['ApiLabelInfo']]): Contains a list of lables this label includes, making it
            a super label.
    """

    id: Union[Unset, int] = UNSET
    version: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    sub_labels: Union[Unset, None, List["ApiLabelInfo"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        version = self.version
        name = self.name
        description = self.description
        sub_labels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_labels, Unset):
            if self.sub_labels is None:
                sub_labels = None
            else:
                sub_labels = []
                for sub_labels_item_data in self.sub_labels:
                    sub_labels_item = sub_labels_item_data.to_dict()

                    sub_labels.append(sub_labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if version is not UNSET:
            field_dict["Version"] = version
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if sub_labels is not UNSET:
            field_dict["SubLabels"] = sub_labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_label_info import ApiLabelInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        version = d.pop("Version", UNSET)

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        sub_labels = []
        _sub_labels = d.pop("SubLabels", UNSET)
        for sub_labels_item_data in _sub_labels or []:
            sub_labels_item = ApiLabelInfo.from_dict(sub_labels_item_data)

            sub_labels.append(sub_labels_item)

        api_label = cls(
            id=id,
            version=version,
            name=name,
            description=description,
            sub_labels=sub_labels,
        )

        api_label.additional_properties = d
        return api_label

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
