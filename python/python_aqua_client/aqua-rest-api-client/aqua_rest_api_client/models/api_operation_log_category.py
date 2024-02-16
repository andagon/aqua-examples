from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_operation_log_category_scope import ApiOperationLogCategoryScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiOperationLogCategory")


@attr.s(auto_attribs=True)
class ApiOperationLogCategory:
    """A category for system log entries.

    Attributes:
        name (Union[Unset, None, str]): The name of the category.
        scope (Union[Unset, ApiOperationLogCategoryScope]): The scope of a system log category.
            This enum has the following values:
              - `Global` System log entries of this category apply to the
            whole system.
              - `Project` System log entries of this category are specific
            for a certain project.
    """

    name: Union[Unset, None, str] = UNSET
    scope: Union[Unset, ApiOperationLogCategoryScope] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        scope: Union[Unset, str] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if scope is not UNSET:
            field_dict["Scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        _scope = d.pop("Scope", UNSET)
        scope: Union[Unset, ApiOperationLogCategoryScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = ApiOperationLogCategoryScope(_scope)

        api_operation_log_category = cls(
            name=name,
            scope=scope,
        )

        return api_operation_log_category
