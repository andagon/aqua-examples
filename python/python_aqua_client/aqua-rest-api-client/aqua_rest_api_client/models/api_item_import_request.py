from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_file_upload_info import ApiFileUploadInfo


T = TypeVar("T", bound="ApiItemImportRequest")


@attr.s(auto_attribs=True)
class ApiItemImportRequest:
    """Request for importing files from a previously uploaded excel file
    Suggested usage: first,import file with ignoreIncorrectRow set to false, to see if Import works and get any errors
    If any errors occur, display errors and let user decide if an import while skipping errors is desired.
    If he decides for an import with skipping erors, repeat the request with ignoreIncorrectRow set to true, the same
    fileMeta can be reused to avoid uploading the file again.

        Attributes:
            file_meta (Union[Unset, None, ApiFileUploadInfo]): Contains metadata for an uploaded image.
            ignore_incorrect_row (Union[Unset, bool]): Controls the behavior for errors on import.
                When set to false, the import will process all rows and log the errors into
                ApiImportLongRunningTaskInfo.FailedItems, which can be retrieved via /api/System/LongOperation. The successful
                items will NOT be saved.
                When set to true the import will process all rows and successful items will be saved. NOT ERRORS WILL BE LOGGED.
    """

    file_meta: Union[Unset, None, "ApiFileUploadInfo"] = UNSET
    ignore_incorrect_row: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        file_meta: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.file_meta, Unset):
            file_meta = self.file_meta.to_dict() if self.file_meta else None

        ignore_incorrect_row = self.ignore_incorrect_row

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if file_meta is not UNSET:
            field_dict["fileMeta"] = file_meta
        if ignore_incorrect_row is not UNSET:
            field_dict["ignoreIncorrectRow"] = ignore_incorrect_row

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_file_upload_info import ApiFileUploadInfo

        d = src_dict.copy()
        _file_meta = d.pop("fileMeta", UNSET)
        file_meta: Union[Unset, None, ApiFileUploadInfo]
        if _file_meta is None:
            file_meta = None
        elif isinstance(_file_meta, Unset):
            file_meta = UNSET
        else:
            file_meta = ApiFileUploadInfo.from_dict(_file_meta)

        ignore_incorrect_row = d.pop("ignoreIncorrectRow", UNSET)

        api_item_import_request = cls(
            file_meta=file_meta,
            ignore_incorrect_row=ignore_incorrect_row,
        )

        return api_item_import_request
