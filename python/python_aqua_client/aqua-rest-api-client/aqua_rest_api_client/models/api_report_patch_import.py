from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_file_upload_info import ApiFileUploadInfo


T = TypeVar("T", bound="ApiReportPatchImport")


@attr.s(auto_attribs=True)
class ApiReportPatchImport:
    """
    Attributes:
        patch_type (str):
        files_meta (Union[Unset, None, List['ApiFileUploadInfo']]): The list of report template files which should be
            imported.
            The files should be uploaded to the endpoint
            [UploadFile](#operation/File_UploadFile)
            first.
    """

    patch_type: str
    files_meta: Union[Unset, None, List["ApiFileUploadInfo"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patch_type = self.patch_type
        files_meta: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.files_meta, Unset):
            if self.files_meta is None:
                files_meta = None
            else:
                files_meta = []
                for files_meta_item_data in self.files_meta:
                    files_meta_item = files_meta_item_data.to_dict()

                    files_meta.append(files_meta_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PatchType": patch_type,
            }
        )
        if files_meta is not UNSET:
            field_dict["filesMeta"] = files_meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_file_upload_info import ApiFileUploadInfo

        d = src_dict.copy()
        patch_type = d.pop("PatchType")

        files_meta = []
        _files_meta = d.pop("filesMeta", UNSET)
        for files_meta_item_data in _files_meta or []:
            files_meta_item = ApiFileUploadInfo.from_dict(files_meta_item_data)

            files_meta.append(files_meta_item)

        api_report_patch_import = cls(
            patch_type=patch_type,
            files_meta=files_meta,
        )

        api_report_patch_import.additional_properties = d
        return api_report_patch_import

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
