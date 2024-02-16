from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_label_info import ApiLabelInfo


T = TypeVar("T", bound="ApiLabelUpdate")


@attr.s(auto_attribs=True)
class ApiLabelUpdate:
    """Represents a new label.

    Attributes:
        id (Union[Unset, int]): Id of this label.
        name (Union[Unset, None, str]): Name of this label. The name is unique in combination with the base object type.
        description (Union[Unset, None, str]): Description of this label.
        version (Union[Unset, int]): Current Version of this label.
        sub_labels (Union[Unset, None, List['ApiLabelInfo']]): Contains a list of lables this label includes, making it
            a super label.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    version: Union[Unset, int] = UNSET
    sub_labels: Union[Unset, None, List["ApiLabelInfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        version = self.version
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
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if version is not UNSET:
            field_dict["Version"] = version
        if sub_labels is not UNSET:
            field_dict["SubLabels"] = sub_labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_label_info import ApiLabelInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        version = d.pop("Version", UNSET)

        sub_labels = []
        _sub_labels = d.pop("SubLabels", UNSET)
        for sub_labels_item_data in _sub_labels or []:
            sub_labels_item = ApiLabelInfo.from_dict(sub_labels_item_data)

            sub_labels.append(sub_labels_item)

        api_label_update = cls(
            id=id,
            name=name,
            description=description,
            version=version,
            sub_labels=sub_labels,
        )

        return api_label_update
