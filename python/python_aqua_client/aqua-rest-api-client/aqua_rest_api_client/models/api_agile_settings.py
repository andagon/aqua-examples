from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_agile_backlog import ApiAgileBacklog


T = TypeVar("T", bound="ApiAgileSettings")


@attr.s(auto_attribs=True)
class ApiAgileSettings:
    """Provides settings for Agile

    Attributes:
        backlog (Union[Unset, None, ApiAgileBacklog]): Provides settings for backlog in Agile
    """

    backlog: Union[Unset, None, "ApiAgileBacklog"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        backlog: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.backlog, Unset):
            backlog = self.backlog.to_dict() if self.backlog else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if backlog is not UNSET:
            field_dict["Backlog"] = backlog

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_agile_backlog import ApiAgileBacklog

        d = src_dict.copy()
        _backlog = d.pop("Backlog", UNSET)
        backlog: Union[Unset, None, ApiAgileBacklog]
        if _backlog is None:
            backlog = None
        elif isinstance(_backlog, Unset):
            backlog = UNSET
        else:
            backlog = ApiAgileBacklog.from_dict(_backlog)

        api_agile_settings = cls(
            backlog=backlog,
        )

        return api_agile_settings
