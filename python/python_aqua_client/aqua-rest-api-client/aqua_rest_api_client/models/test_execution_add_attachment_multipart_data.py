import json
from io import BytesIO
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="TestExecutionAddAttachmentMultipartData")


@attr.s(auto_attribs=True)
class TestExecutionAddAttachmentMultipartData:
    """
    Attributes:
        file (Union[Unset, List[Optional[File]]]):
    """

    file: Union[Unset, List[Optional[File]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file: Union[Unset, List[Optional[FileJsonType]]] = UNSET
        if not isinstance(self.file, Unset):
            file = []
            for file_item_data in self.file:
                file_item = file_item_data.to_tuple() if file_item_data else None

                file.append(file_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.file, Unset):
            _temp_file = []
            for file_item_data in self.file:
                file_item = file_item_data.to_tuple() if file_item_data else None

                _temp_file.append(file_item)
            file = (None, json.dumps(_temp_file).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = []
        _file = d.pop("file", UNSET)
        for file_item_data in _file or []:
            _file_item = file_item_data
            file_item: Optional[File]
            if _file_item is None:
                file_item = None
            else:
                file_item = File(payload=BytesIO(_file_item))

            file.append(file_item)

        test_execution_add_attachment_multipart_data = cls(
            file=file,
        )

        test_execution_add_attachment_multipart_data.additional_properties = d
        return test_execution_add_attachment_multipart_data

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
