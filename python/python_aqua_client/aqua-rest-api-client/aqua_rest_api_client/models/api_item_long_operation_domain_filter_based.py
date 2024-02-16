from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_filter_update import ApiFilterUpdate


T = TypeVar("T", bound="ApiItemLongOperationDomainFilterBased")


@attr.s(auto_attribs=True)
class ApiItemLongOperationDomainFilterBased:
    """
    Attributes:
        type (str):
        project_id (Union[Unset, int]): Project where to look in.
        folder_id (Union[Unset, int]): Folder where to look in. Zero means root folder (combined with Recursive=true
            means all items in project).
        recursive (Union[Unset, bool]): If true items in subfolders are considered as well.
        filter_ (Union[Unset, None, ApiFilterUpdate]): Contains the new filter expression.
        include_archived (Union[Unset, bool]): If true the archived items (matching other criteria) are included as
            well.
    """

    type: str
    project_id: Union[Unset, int] = UNSET
    folder_id: Union[Unset, int] = UNSET
    recursive: Union[Unset, bool] = UNSET
    filter_: Union[Unset, None, "ApiFilterUpdate"] = UNSET
    include_archived: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        project_id = self.project_id
        folder_id = self.folder_id
        recursive = self.recursive
        filter_: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict() if self.filter_ else None

        include_archived = self.include_archived

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Type": type,
            }
        )
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if folder_id is not UNSET:
            field_dict["FolderId"] = folder_id
        if recursive is not UNSET:
            field_dict["Recursive"] = recursive
        if filter_ is not UNSET:
            field_dict["Filter"] = filter_
        if include_archived is not UNSET:
            field_dict["IncludeArchived"] = include_archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_filter_update import ApiFilterUpdate

        d = src_dict.copy()
        type = d.pop("Type")

        project_id = d.pop("ProjectId", UNSET)

        folder_id = d.pop("FolderId", UNSET)

        recursive = d.pop("Recursive", UNSET)

        _filter_ = d.pop("Filter", UNSET)
        filter_: Union[Unset, None, ApiFilterUpdate]
        if _filter_ is None:
            filter_ = None
        elif isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ApiFilterUpdate.from_dict(_filter_)

        include_archived = d.pop("IncludeArchived", UNSET)

        api_item_long_operation_domain_filter_based = cls(
            type=type,
            project_id=project_id,
            folder_id=folder_id,
            recursive=recursive,
            filter_=filter_,
            include_archived=include_archived,
        )

        api_item_long_operation_domain_filter_based.additional_properties = d
        return api_item_long_operation_domain_filter_based

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
