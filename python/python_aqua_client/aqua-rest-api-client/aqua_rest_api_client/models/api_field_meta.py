from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_edit_meta import ApiFieldEditMeta


T = TypeVar("T", bound="ApiFieldMeta")


@attr.s(auto_attribs=True)
class ApiFieldMeta:
    """Contains the meta-information of a specific field.

    Attributes:
        field_type (str):
        id (Union[Unset, None, str]): The id of the field. The field id is identical to the internal property name.
            Therefore, it is
            only unique in scope of the same project and item type.
        title (Union[Unset, None, str]): Title of this field, as visible in the UI. Can be customized by in project
            configuration.
        is_custom (Union[Unset, bool]): True if this field is a custom field.
        is_groupable_in_charts (Union[Unset, bool]): True if the field can be used as GroupBy or XAxis property on a
            chart (dashbaord).
        supports_field_rules (Union[Unset, bool]): Indicates whether this field supports field rules.
        supported_filter_operations (Union[Unset, None, List[str]]): Contains a list of all filter operators which are
            supported
            for this field.
        is_filterable (Union[Unset, bool]): Indicates whether it is possible to filter by this field e.g.
            in item lists.
        is_sortable (Union[Unset, bool]): Indicates whether it is possible to sort by this field e.g.
            in item lists.
        is_affectable (Union[Unset, bool]): Indicates whether it is possible to affect this field by field rules.
        is_groupable (Union[Unset, bool]): Indicates whether it is possible to group by this field e.g.
            in item lists.
        is_active (Union[Unset, bool]): Indicates whether the field is currently enabled or disabled.
        supports_batch_update (Union[Unset, bool]): Indicates whether the field supports batch updates in general.
            Depending on the
            concrete items and the configured workflow, it might still not be possible to change
            a value even if the field supports batch updates in general.
        edit_meta (Union[Unset, None, ApiFieldEditMeta]): Contains the information for a specific field of an item
            including
            the field's value.
    """

    field_type: str
    id: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    is_custom: Union[Unset, bool] = UNSET
    is_groupable_in_charts: Union[Unset, bool] = UNSET
    supports_field_rules: Union[Unset, bool] = UNSET
    supported_filter_operations: Union[Unset, None, List[str]] = UNSET
    is_filterable: Union[Unset, bool] = UNSET
    is_sortable: Union[Unset, bool] = UNSET
    is_affectable: Union[Unset, bool] = UNSET
    is_groupable: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    supports_batch_update: Union[Unset, bool] = UNSET
    edit_meta: Union[Unset, None, "ApiFieldEditMeta"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type
        id = self.id
        title = self.title
        is_custom = self.is_custom
        is_groupable_in_charts = self.is_groupable_in_charts
        supports_field_rules = self.supports_field_rules
        supported_filter_operations: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.supported_filter_operations, Unset):
            if self.supported_filter_operations is None:
                supported_filter_operations = None
            else:
                supported_filter_operations = self.supported_filter_operations

        is_filterable = self.is_filterable
        is_sortable = self.is_sortable
        is_affectable = self.is_affectable
        is_groupable = self.is_groupable
        is_active = self.is_active
        supports_batch_update = self.supports_batch_update
        edit_meta: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_meta, Unset):
            edit_meta = self.edit_meta.to_dict() if self.edit_meta else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "FieldType": field_type,
            }
        )
        if id is not UNSET:
            field_dict["Id"] = id
        if title is not UNSET:
            field_dict["Title"] = title
        if is_custom is not UNSET:
            field_dict["IsCustom"] = is_custom
        if is_groupable_in_charts is not UNSET:
            field_dict["IsGroupableInCharts"] = is_groupable_in_charts
        if supports_field_rules is not UNSET:
            field_dict["SupportsFieldRules"] = supports_field_rules
        if supported_filter_operations is not UNSET:
            field_dict["SupportedFilterOperations"] = supported_filter_operations
        if is_filterable is not UNSET:
            field_dict["IsFilterable"] = is_filterable
        if is_sortable is not UNSET:
            field_dict["IsSortable"] = is_sortable
        if is_affectable is not UNSET:
            field_dict["IsAffectable"] = is_affectable
        if is_groupable is not UNSET:
            field_dict["IsGroupable"] = is_groupable
        if is_active is not UNSET:
            field_dict["IsActive"] = is_active
        if supports_batch_update is not UNSET:
            field_dict["SupportsBatchUpdate"] = supports_batch_update
        if edit_meta is not UNSET:
            field_dict["EditMeta"] = edit_meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_edit_meta import ApiFieldEditMeta

        d = src_dict.copy()
        field_type = d.pop("FieldType")

        id = d.pop("Id", UNSET)

        title = d.pop("Title", UNSET)

        is_custom = d.pop("IsCustom", UNSET)

        is_groupable_in_charts = d.pop("IsGroupableInCharts", UNSET)

        supports_field_rules = d.pop("SupportsFieldRules", UNSET)

        supported_filter_operations = cast(List[str], d.pop("SupportedFilterOperations", UNSET))

        is_filterable = d.pop("IsFilterable", UNSET)

        is_sortable = d.pop("IsSortable", UNSET)

        is_affectable = d.pop("IsAffectable", UNSET)

        is_groupable = d.pop("IsGroupable", UNSET)

        is_active = d.pop("IsActive", UNSET)

        supports_batch_update = d.pop("SupportsBatchUpdate", UNSET)

        _edit_meta = d.pop("EditMeta", UNSET)
        edit_meta: Union[Unset, None, ApiFieldEditMeta]
        if _edit_meta is None:
            edit_meta = None
        elif isinstance(_edit_meta, Unset):
            edit_meta = UNSET
        else:
            edit_meta = ApiFieldEditMeta.from_dict(_edit_meta)

        api_field_meta = cls(
            field_type=field_type,
            id=id,
            title=title,
            is_custom=is_custom,
            is_groupable_in_charts=is_groupable_in_charts,
            supports_field_rules=supports_field_rules,
            supported_filter_operations=supported_filter_operations,
            is_filterable=is_filterable,
            is_sortable=is_sortable,
            is_affectable=is_affectable,
            is_groupable=is_groupable,
            is_active=is_active,
            supports_batch_update=supports_batch_update,
            edit_meta=edit_meta,
        )

        return api_field_meta
